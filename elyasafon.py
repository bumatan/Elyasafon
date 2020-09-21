import argparse
import project_types
import sys

####### Parsing #######
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Parse connect commands
connect_parser = subparsers.add_parser("connect", help='TODO')
connect_parser.add_argument('connection_type', choices=project_types.connection_type, help='The type of connection to use.')
connect_parser.add_argument('index', choices=range(1, project_types.num_of_ports + 1), type=int,  help='The port the device connected to.')

# Parse release commands
release_parser = subparsers.add_parser("release", help='TODO')
release_parser.add_argument('connection_type', choices=project_types.connection_type,  help='The type of connection to use.')

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

####### Run command #######
