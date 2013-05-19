#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import argparse
import sys
import os

from libgreader import GoogleReader, ClientAuthMethod, Feed
from slugify import slugify

def authenticate(username, password):
    auth = ClientAuthMethod(username, password)
    return GoogleReader(auth)

def item_directory(item):
    date = datetime.fromtimestamp(item.time)
    slug = slugify(item.title, max_length=180, word_boundary=True)
    return '%s-%s' % (date.strftime('%Y-%m-%d'), slug)

def save(item, directory):
    itemdir = '%s/%s' % (directory, item_directory(item))
    if not os.path.isdir(itemdir):
        os.makedirs(itemdir)
    filename = '%s/index.html' % itemdir
    print "---> %s" % filename
    fp = open(filename, 'wb')
    fp.write('<h3><a href="{0}">{1}</a></h3>\n'.format(item.url, item.title).encode('utf-8'))
    fp.write(item.content.encode('utf-8'))
    fp.close()

def fetch(feed, directory, starred=False, load_limit=100):
    count = 0
    until = None
    while True:
        feed.loadItems(loadLimit=load_limit, until=until)
        if feed.countItems() == 0:
            break
        count += feed.countItems()
        until = feed.items[-1].time - 1

        for item in feed.items:
            if not starred or item.starred:
                save(item, directory)
    return count

def main():
    parser = argparse.ArgumentParser(description='Google Reader RSS archive fetcher')
    parser.add_argument('-u', '--username', dest='username', help='user name')
    parser.add_argument('-p', '--password', dest='password', help='account password')
    parser.add_argument('-f', '--feed', dest='feed', help='feed number to fetch')
    parser.add_argument('-s', '--starred', dest='starred', action='store_true',
                        default=False, help='store only starred items')
    parser.add_argument('-d', '--dir', dest='dir', help='directory name to store feed contents')
    args = parser.parse_args()

    if None in (args.username, args.password):
        print "* Please specify username and password *\n"
        parser.print_help()
        sys.exit(1)

    reader = authenticate(args.username, args.password)
    # fetch list of feeds
    reader.buildSubscriptionList()

    if args.feed:
        feed = reader.getSubscriptionList()[int(args.feed)]

        # create output directory
        if args.dir is None:
            directory = slugify(feed.title, max_length=60, word_boundary=True)
        else:
            directory = args.dir
        print "* Output directory: %s *" % directory
        if not os.path.isdir(directory):
            os.makedirs(directory)

        # fetch the feed
        fetch(feed, directory, starred=args.starred)
    else:
        # enumerate feeds
        print "* Please specify feed number (-f, --feed) to fetch: *"
        for i, feed in enumerate(reader.getSubscriptionList()):
            print "[{0}] {1} [{2}]".format(i, feed.title, feed.feedUrl).encode('utf-8')


if __name__ == "__main__":
    main()
