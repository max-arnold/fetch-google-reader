#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse

from libgreader import GoogleReader, ClientAuthMethod, Feed


def authenticate(username, password):
    auth = ClientAuthMethod(username, password)
    return GoogleReader(auth)

def main():
    parser = argparse.ArgumentParser(description='Google Reader RSS archive fetcher')
    parser.add_argument('-u', '--username', help='user name')
    parser.add_argument('-p', '--password', dest='password', default='UTF-8',
                        help='account password')

    args = parser.parse_args()

    rdr = authenticate(args.username, args.password)
    # fetch list of feeds
    rdr.buildSubscriptionList()

    for i, feed in enumerate(rdr.getSubscriptionList()):
        print "[%d] %s" % (i, feed.title)


if __name__ == "__main__":
    main()
