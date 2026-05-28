""" Generate the SI reference point TTL/JSON-LD files """

import argparse
import logging
import hashlib
import si_ref_point.tboxes.si_tbox as cuq_tbox
import si_ref_point.aboxes.quantities_abox as quantities_abox
import si_ref_point.aboxes.units_abox as units_abox
import si_ref_point.aboxes.constants_abox as constants_abox
import si_ref_point.aboxes.prefixes_abox as prefixes_abox
import si_ref_point.aboxes.decisions_abox as decisions_abox
import si_ref_point.tboxes.rb_tbox as rb_tbox
import si_ref_point.aboxes.rb_abox_cgpm as rb_abox_cgpm
import si_ref_point.aboxes.rb_abox_cipm as rb_abox_cipm
import si_ref_point.aboxes.rb_abox_cctf as rb_abox_cctf
from si_ref_point.settings import PKG_ROOT
import git
import os
import datetime
from pathlib import Path
from zipfile import ZipFile
from rdflib import Graph

file_generator = {
    'si': cuq_tbox.main,
    'units': units_abox.main,
    'quantities': quantities_abox.main,
    'constants': constants_abox.main,
    'prefixes': prefixes_abox.main,
    'decisions': decisions_abox.main,
    'bodies': rb_tbox.main,
    'cgpm': rb_abox_cgpm.main,
    'cipm': rb_abox_cipm.main,
    'cctf': rb_abox_cctf.main,
}

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
        '-o', '--output_dir', type=Path,
        default=".",
        help="Output directory. Defaults to current working directory")
    parser.add_argument(
        '--ttl_output_subdir',
        type=str,
        default="TTL",
        help="Optional output subdirectory for TTL output")
    parser.add_argument(
        '--jsonld_output_subdir',
        type=str,
        default="JSONLD",
        help="Optional output directory for JSON-LD output")
    return parser


def load_graphs(only_this=None):
    output = {}
    for label, generator in file_generator.items():
        if only_this and only_this not in label:
            continue
        logging.info(f"generating {label} graph")
        # Generator will return a rdflib.Graph object
        output[label] = generator()
        logging.info("..done")
    return output

def generate_hash_file(tgtfile: Path):
    """ generate hash for file and write it next to it, with a different ext
    """
    h = hashlib.new('sha256')
    with open(tgtfile, encoding="UTF8") as fp:
        h.update(fp.read().encode())
    hashstr = h.hexdigest()
    hashdest = tgtfile.with_suffix('.sha256')
    with open(hashdest, 'w') as fp:
        fp.write(hashstr)

def serialize_graphs(graphs={}, fmt="ttl", ext="ttl", tgtdir: Path=None,
                     generate_hash=False):
    if not tgtdir.exists():
        os.makedirs(tgtdir)
    for label, g in graphs.items():
        tgtfile = tgtdir / (label + '.' + ext)
        g.serialize(format=fmt, destination=tgtfile)
        if generate_hash:
            generate_hash_file(tgtfile)

def non_interactive(ttl_path):
    output = load_graphs()
    serialize_graphs(graphs=output, fmt="ttl", ext="ttl", tgtdir=ttl_path)


def main():
    args = get_parser().parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    output = load_graphs(only_this=args.only)

    ttl_dir = args.output_dir / args.ttl_output_subdir
    jsonld_dir = args.output_dir / args.jsonld_output_subdir

    serializations = [{"fmt": "ttl",
                       "dir": ttl_dir,
                       "ext": "ttl"},
                      {"fmt": "json-ld",
                       "dir": jsonld_dir,
                       "ext": "jsonld"}]

    # Serialize all graphs in their respective output files
    for srl in serializations:
        serialize_graphs(graphs=output, fmt=srl['fmt'], ext=srl['ext'],
                         tgtdir=srl['dir'], generate_hash=True)

    # Generate full graphs outputs
    # Just merging graphs in memory could lead to blank-nodes collisions, so
    # instead parse the TTL files we just wrote as suggested here
    # https://rdflib.readthedocs.io/en/7.1.1/merging.html

    full_graph = Graph()
    logging.info(f"generating full sirp graph")
    for ttl_file in file_generator.keys():
        full_graph.parse(ttl_dir / (ttl_file + ".ttl"))
    for srl in serializations:
        filedest = Path(srl['dir']) / ('sirp_full.' + srl['ext'])
        full_graph.serialize(format=srl['fmt'], destination=filedest)
        generate_hash_file(filedest)
    logging.info("..done")

    logging.info(f"TTL and JSON-LD files written to ./{ttl_dir}/ and ./{jsonld_dir}/, respectively")
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
            repo = git.Repo(PKG_ROOT, search_parent_directories=True)
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
