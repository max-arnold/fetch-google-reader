#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import sys

from libgreader import GoogleReader, ClientAuthMethod, Feed


def authenticate(username, password):
    auth = ClientAuthMethod(username, password)
    return GoogleReader(auth)

def fetch(reader, feed):
    print "Feed to fetch:", feed

def main():
    parser = argparse.ArgumentParser(description='Google Reader RSS archive fetcher')
    parser.add_argument('-u', '--username', dest='username', help='user name')
    parser.add_argument('-p', '--password', dest='password', help='account password')
    parser.add_argument('-f', '--fetch', dest='fetch', help='feed number to fetch')
    parser.add_argument('-d', '--dir', dest='dir', help='directory name to store feed contents')
    args = parser.parse_args()

    if None in (args.username, args.password):
        print "* Please specify username and password *\n"
        parser.print_help()
        sys.exit(1)

    reader = authenticate(args.username, args.password)
    # fetch list of feeds
    reader.buildSubscriptionList()

    if args.fetch:
        fetch(reader, reader.getSubscriptionList()[int(args.fetch)])
    else:
        for i, feed in enumerate(reader.getSubscriptionList()):
            print "[%d] %s" % (i, feed.title)


if __name__ == "__main__":
    main()
