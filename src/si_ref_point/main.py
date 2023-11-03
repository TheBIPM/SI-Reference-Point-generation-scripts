""" Generate the SI reference point TTL files
"""

import argparse
import logging
import subprocess
import si_ref_point.cuq.CUQ_TBox as CUQ_TBox
import si_ref_point.cuq.Quantities_ABox as Quantities_ABox
import si_ref_point.cuq.Units_ABox as Units_ABox
import si_ref_point.cuq.Constants_ABox as Constants_ABox
import si_ref_point.cuq.Prefixes_ABox as Prefixes_ABox
import si_ref_point.cuq.generate_decisions_turtle as gen_decisions
import si_ref_point.resbod.ResBod_TBox as ResBod_TBox
import si_ref_point.resbod.ResBod_ABox_CGPM as ResBod_ABox_CGPM
import si_ref_point.resbod.ResBod_ABox_CIPM as ResBod_ABox_CIPM
import si_ref_point.resbod.ResBod_ABox_CCTF as ResBod_ABox_CCTF
from si_ref_point.settings import APIPATH
import os
import datetime
import gzip


def get_parser():
    """ Dedicated function to collect command line parameters, so it can
    autogenerate doc too
    """
    parser = argparse.ArgumentParser(
        description="Generate SIreference point TTL files")
    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default="./API",
        help="Output directory for API")
    return parser


def main():
    args = get_parser().parse_args()

    logging.info("generating si.ttl")
    CUQ_TBox.main()
    logging.info("..done")

    logging.info("generating quantities.ttl")
    Quantities_ABox.main()
    logging.info("..done")

    logging.info("generating units.ttl")
    Units_ABox.main()
    logging.info("..done")

    logging.info("generating constants.ttl")
    Constants_ABox.main()
    logging.info("..done")

    logging.info("generating prefixes.ttl")
    Prefixes_ABox.main()
    logging.info("..done")

    logging.info("generating decisions.ttl")
    gen_decisions.main()
    logging.info("..done")

    logging.info("generating bodies.ttl")
    ResBod_TBox.main()
    logging.info("..done")

    logging.info("generating cgpm.ttl")
    ResBod_ABox_CGPM.main()
    logging.info("..done")

    logging.info("generating cipm.ttl")
    ResBod_ABox_CIPM.main()
    logging.info("..done")

    logging.info("generating cctf.ttl")
    ResBod_ABox_CCTF.main()
    logging.info("..done")

    # compress into archive
    # export git_hash=$(git log --pretty=format:'%h' -n 1)
    now = datetime.datetime.now()
    timetag = now.strftime('%Y%m%dT%H:%M')

