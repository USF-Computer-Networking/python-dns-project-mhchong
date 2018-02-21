
import argparse as ap
import socket


def parse_args():
    parser = ap.ArgumentParser("DNS lookup utlity")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', help='domain name (example: google.com)')
    group.add_argument('-i', help='ip address of a domain or host')
    return parser.parse_args()

if __name__ == '__main__':
    #p = parse_args()
    # data = socket.gethostbyname_ex('google.com')
    data = socket.getfqdn('216.58.194.206')
    print(data)