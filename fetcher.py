#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import sys
import os

from libgreader import GoogleReader, ClientAuthMethod, Feed
from slugify import slugify

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
        feed = reader.getSubscriptionList()[int(args.fetch)]

        # create output directory
        if args.dir is None:
            directory = slugify(feed.title)
        else:
            directory = args.dir
        print "* Output directory: %s *" % directory
        if not os.path.isdir(directory):
            os.makedirs(directory)

        # fetch the feed
        fetch(reader, feed)
    else:
        for i, feed in enumerate(reader.getSubscriptionList()):
            print "[%d] %s" % (i, feed.title)


if __name__ == "__main__":
    main()
