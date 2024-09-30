""" Wrapper to launch fastAPI/uvicorn app
"""
import argparse
import uvicorn
import json

def get_parser():
    """ Dedicated function to collect command line parameters, so it can
    autogenerate doc too
    """
    parser = argparse.ArgumentParser(
        description="Launch SI test API")
    parser.add_argument(
        '-p', '--port', type=int, default=5000,
        help="Web server port")
    parser.add_argument(
        '--host', type=str, default="0.0.0.0", # 0.0.0.0 is needed to make the server visible on a local network
        help="Web server host")
    parser.add_argument(
        '--log_level', type=str, default="info",
        help="Log level")
    return parser

def main():
    args = get_parser().parse_args()
    uvicorn.run('si_ref_point.test_api.api_main:app',
                port=args.port,
                log_level=args.log_level,
                host=args.host)

if __name__ == "__main__":
    main()
