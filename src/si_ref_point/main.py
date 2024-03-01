""" Generate the SI reference point TTL files
"""

import argparse
import logging
import hashlib
import si_ref_point.cuq.CUQ_TBox as CUQ_TBox
import si_ref_point.cuq.Quantities_ABox as Quantities_ABox
import si_ref_point.cuq.Units_ABox as Units_ABox
import si_ref_point.cuq.Constants_ABox as Constants_ABox
import si_ref_point.cuq.Prefixes_ABox as Prefixes_ABox
import si_ref_point.cuq.Decisions_ABox as Decisions_ABox
import si_ref_point.resbod.ResBod_TBox as ResBod_TBox
import si_ref_point.resbod.ResBod_ABox_CGPM as ResBod_ABox_CGPM
import si_ref_point.resbod.ResBod_ABox_CIPM as ResBod_ABox_CIPM
import si_ref_point.resbod.ResBod_ABox_CCTF as ResBod_ABox_CCTF
from si_ref_point import __version__
import os
import datetime
from zipfile import ZipFile
import subprocess


def get_parser():
    """ Dedicated function to collect command line parameters, so it can
    autogenerate doc too
    """
    parser = argparse.ArgumentParser(
        description="Generate SI reference point TTL files")
    parser.add_argument(
        '-z', '--zipfile', action='store_true',
        help="Generate zip file")
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='debug')
    parser.add_argument(
        '--gen_ontology_viz', action='store_true',
        help="Generate ontology markdown using the ontospy pachage")
    parser.add_argument(
        '--version', action='version',
        version='%(prog)s' + __version__)
    parser.add_argument(
        '--only', type=str,
        help='Generate only ttl with names containing this string')
    parser.add_argument(
        '--generate_RDF', action='store_true',
        help='Generate (single) RDF output')
    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default=os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             "..", "..", "TTL")),
        help="Output directory for TTL output")
    parser.add_argument(
        '--jsonld_output_dir',
        type=str,
        default=os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             "..", "..", "JSON-LD")),
        help="Output directory for JSON-LD output")
    return parser


def main():
    args = get_parser().parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    file_generator = {
        'si': CUQ_TBox.main,
        'units': Units_ABox.main,
        'quantities': Quantities_ABox.main,
        'constants': Constants_ABox.main,
        'prefixes': Prefixes_ABox.main,
        'decisions': Decisions_ABox.main,
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
            with open(filedest) as fp:
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
            githash = subprocess.check_output(["git", "describe"]).strip().decode()
        except:  # noqa
            githash = __version__

        for srl in serializations:
            zipname = '{}-si-app-{}-{}.zip'.format(timetag,
                                                   srl['ext'],
                                                   githash)
            logging.info(f'generating {zipname}')
            with ZipFile(zipname, 'w') as zf:
                for label, generator in file_generator.items():
                    srl_file = label + "." + srl['ext']
                    zf.write(os.path.join(srl['dir'], srl_file),
                             arcname=srl_file)
                    hash_file = label + ".sha256"
                    zf.write(os.path.join(srl['dir'], hash_file),
                             arcname=hash_file)

    # Generate ontology documentation markdown files
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
