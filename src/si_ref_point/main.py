""" Generate the SI reference point TTL files """

import argparse
import logging
import hashlib
#import si_ref_point.cuq.cuq_tbox as cuq_tbox        # as example if the package is installed
import si_ref_point.cuq.cuq_tbox as cuq_tbox
import si_ref_point.cuq.quantities_abox as quantities_abox
import si_ref_point.cuq.units_abox as units_abox
import si_ref_point.cuq.constants_abox as constants_abox
import si_ref_point.cuq.prefixes_abox as prefixes_abox
import si_ref_point.cuq.decisions_abox as decisions_abox
import si_ref_point.resbod.ResBod_TBox as ResBod_TBox
import si_ref_point.resbod.ResBod_ABox_CGPM as ResBod_ABox_CGPM
import si_ref_point.resbod.ResBod_ABox_CIPM as ResBod_ABox_CIPM
import si_ref_point.resbod.ResBod_ABox_CCTF as ResBod_ABox_CCTF
from si_ref_point.settings import TTL_FILES_FOLDER, JSONLD_FILES_FOLDER
#from si_ref_point import __version__
import git
import os
import datetime
from zipfile import ZipFile


def get_parser():
    """ Dedicated function to collect command line parameters, so it can
    autogenerate doc too
    """
    parser = argparse.ArgumentParser(
        description="Generate SI reference point serialized files")
    parser.add_argument(
        '-z', '--zipfile', action='store_true',
        help="Generate zip file")
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='debug')
    parser.add_argument(
        '--gen_ontology_viz', action='store_true',
        help="Generate ontology markdown using the ontospy pachage")
    # parser.add_argument(
    #     '--version', action='version',
    #     version='%(prog)s' + __version__)
    parser.add_argument(
        '--only', type=str,
        help='Generate only ttl with names containing this string')
    parser.add_argument(
        '--generate_RDF', action='store_true',
        help='Generate (single) RDF output')
    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default=TTL_FILES_FOLDER,
        help="Output directory for TTL output")
    parser.add_argument(
        '--jsonld_output_dir',
        type=str,
        default=JSONLD_FILES_FOLDER,
        help="Output directory for JSON-LD output")
    return parser


def main():
    args = get_parser().parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    file_generator = {
        'si': cuq_tbox.main,
        'units': units_abox.main,
        'quantities': quantities_abox.main,
        'constants': constants_abox.main,
        'prefixes': prefixes_abox.main,
        'decisions': decisions_abox.main,
        'bodies': ResBod_TBox.main,
        'cgpm': ResBod_ABox_CGPM.main,
        'cipm': ResBod_ABox_CIPM.main,
        'cctf': ResBod_ABox_CCTF.main,
    }
    output = {}
    for label, generator in file_generator.items():
        if args.only and args.only not in label:
            continue
        logging.info(f"generating {label} graph")
        # Generator will return a rdflib.Graph object
        output[label] = generator()
        logging.info("..done")

    serializations = [{"fmt": "ttl",
                       "dir": args.output_dir,
                       "ext": "ttl"},
                      {"fmt": "json-ld",
                       "dir": args.jsonld_output_dir,
                       "ext": "jsonld"}]

    # Serialize all graphs in their respective output files
    for srl in serializations:
        if not os.path.exists(srl['dir']):
            os.makedirs(srl['dir'])
        for label, graph in output.items():
            filedest = os.path.join(srl['dir'],label + '.' + srl['ext'])
            graph.serialize(format=srl['fmt'], destination=filedest)

            # generate hash for file and write it alongside
            h = hashlib.new('sha256')
            with open(filedest, encoding="UTF8") as fp:
                h.update(fp.read().encode())
            hashstr = h.hexdigest()
            hashdest = os.path.join(srl['dir'], label + '.sha256')
            with open(hashdest, 'w') as fp:
                fp.write(hashstr)

    logging.info(f"TTL files wrote in {args.output_dir}")
    if args.generate_RDF:
        output['si'].serialize(
            format='xml',
            destination=os.path.join(args.output_dir, 'si.xml'))

    # compress into archive
    if args.zipfile:
        if args.only:
            logging.warning(
                "Only selected ttl files generated -> no zip output")
            raise SystemExit
        now = datetime.datetime.now()
        timetag = now.strftime('%Y%m%dT%H%M%S')
        try:
            # Replaced to work in the tests
            # githash = subprocess.check_output(["git", "describe"]).strip().decode()
            repo = git.Repo(search_parent_directories=True)
            githash = repo.head.object.hexsha[:8]
        except:  # noqa
            githash = "nohash"

        zipname = '{}-si-app-{}.zip'.format(timetag, githash)
        logging.info(f'generating {zipname}')
        with ZipFile(zipname, 'w') as zf:
            for srl in serializations:
                for label, generator in file_generator.items():
                    srl_file = label + "." + srl['ext']
                    zf.write(os.path.join(srl['dir'], srl_file),
                             arcname=os.path.join(srl['fmt'].upper(), srl_file))
                    hash_file = label + ".sha256"
                    zf.write(os.path.join(srl['dir'], hash_file),
                             arcname=os.path.join(srl['fmt'].upper(), hash_file))

    # Generate ontology documentation Markdown files
    if args.gen_ontology_viz:
        import ontospy
        from ontospy.gendocs.viz.viz_markdown import MarkdownViz
        doc_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "..", "docs", "vocabulary_viz"))

        if not os.path.exists(doc_path):
            os.makedirs(doc_path)
        g = ontospy.Ontospy(os.path.join(args.output_dir, 'si.ttl'))
        v = MarkdownViz(g)
        v.build(output_path=doc_path)
        logging.info(
            f"Markdown files for vocabulary output in {doc_path}")


if __name__ == "__main__":
    main()
