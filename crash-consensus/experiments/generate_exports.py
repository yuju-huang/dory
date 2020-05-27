#!/usr/bin/env python3
import socket
import collections
from sys import argv

## Configuration
# Map deployment id to physical machine
servers = collections.OrderedDict([
    (1, 'machine1'),
    (2, 'machine2'),
    (3, 'machine3'),
    (4, 'machine4'),
    (5, 'machine1'),
    (6, 'machine2'),
    (7, 'machine3'),
    (8, 'machine4'),
    (9, 'machine1'),
])

## End of configuration

deployed_servers = int(argv[1])
dory_registry_ip = argv[2]
starting_port = int(argv[3])
instance_num = int(argv[4]) # Starts from zero
get_hostname_only = True if len(argv) == 6 else False

ids = list(servers.keys())[0:deployed_servers]

my_id = list(servers.keys())[instance_num]
my_hostname = servers[my_id]

if get_hostname_only:
    print(my_hostname)
    exit(0)

print("export EXPER_PORT={}".format(starting_port + list(servers.values())[0:instance_num].count(my_hostname)))
print("export SID={}".format(my_id))
print("export IDS={}".format(','.join(map(str, ids))))
print("export DORY_REGISTRY_IP={}".format(dory_registry_ip))