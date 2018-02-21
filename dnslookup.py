'''
    Author      : Marcus Chong
    Description : A simple Python program to allow the user
                  to look up the hostname of a given ip address
                  or look up the ip address of a given hostname
                  based on the DNS Protocol
'''

import argparse as ap
import socket

def parse_args():
    parser = ap.ArgumentParser("DNS lookup utlity")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', help='domain name (example: google.com)')
    group.add_argument('-i', help='ip address of a domain or host')
    return parser.parse_args()

if __name__ == '__main__':
    p = parse_args()

    if p.d:
        data = socket.gethostbyname(p.d)
        print(data)
    elif p.i:
        data = socket.getfqdn(p.i)
        print(data)