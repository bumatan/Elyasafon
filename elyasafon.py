import argparse
import sys
import project_types
import device_manager

####### Parsing #######
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

# Parse connect commands
connect_parser = subparsers.add_parser("connect", help='TODO')
connect_parser.add_argument('connection_type', choices=project_types.connection_types, help='The type of connection to use.')
connect_parser.add_argument('index', choices=range(1, project_types.num_of_ports + 1), type=int,  help='The port the device connected to.')

# Parse release commands
release_parser = subparsers.add_parser("release", help='TODO')
release_parser.add_argument('connection_type', choices=project_types.connection_types,  help='The type of connection to use.')

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

####### Run command #######
d_manager = device_manager.device_manager()
if args.command == 'connect':
    d_manager.connect(args.connection_type, args.index)
    print('Your device is now connected')
if args.command == 'release':
    d_manager.release(args.connection_type)
    print('Your device is now released')
