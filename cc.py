#!/usr/bin/python3

import sys
import re
from termcolor import colored


if len(sys.argv) != 2:
    print('USAGE: cc [command]')
    sys.exit(1)

command = sys.argv[1]

commands = {
    'tcpdump': {
        # timestamp
        '(\d{2}:\d{2}:\d{2}.\d{6})': 'yellow',        

        # protocols
        '(IP|TCP|UDP|ICMP|FTP)': 'blue',

        # IPv4 addresses
        '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})': 'red',

        # IPv4 number ports
        '(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.)(\d{1,5})(?::| )': 'green',

        # IPv4 name ports
        #'\.(ftp|tcp|udp)': 'green'
    }
}

mappings = commands[command]

for line in sys.stdin:
    colored_line = line
    for match_string, color in mappings.items():
        items = re.findall(match_string, line)
        for item in items:
            colored_line = colored_line.replace(item, colored(item, color))

    print(colored_line, end='')

