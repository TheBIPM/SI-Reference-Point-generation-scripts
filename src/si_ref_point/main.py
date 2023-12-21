""" Generate the SI reference point TTL files
"""

import argparse
import logging
import si_ref_point.cuq.CUQ_TBox_Extension as CUQ_TBox_Extension
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
        '--version', action='version',
        version='%(prog)s' + __version__)
    parser.add_argument(
        '--only', type=str,
        help='Generate on ttl with names containing this string')
    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default="./API",
        help="Output directory for API")
    return parser


def main():
    args = get_parser().parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    file_generator = {
        #'si': CUQ_TBox.main,
        'si': CUQ_TBox_Extension.main,
        'quantities': Quantities_ABox.main,
        'units': Units_ABox.main,
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

    # Serialize all graphs in their respective turtle files
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    for label, graph in output.items():
        graph.serialize(format='ttl',
                        destination=os.path.join(args.output_dir,
                                                 label + '.ttl'))

    # compress into archive
    if args.zipfile:
        if args.only:
            logging.warning(
                "Only selected ttl files generated -> no zip output")
            raise SystemExit
        now = datetime.datetime.now()
        timetag = now.strftime('%Y%m%dT%H%M%S')
        try:
            githash = __version__.split('+')[1].split('.')[0]
        except IndexError:
            githash = __version__
        zipname = '{}-si-app-turtle-{}.zip'.format(timetag, githash)
        logging.info(f'generating {zipname}')
        with ZipFile(zipname, 'w') as zf:
            for label, generator in file_generator.items():
                ttl_file = label + ".ttl"
                zf.write(os.path.join(args.output_dir, ttl_file),
                         arcname=ttl_file)
