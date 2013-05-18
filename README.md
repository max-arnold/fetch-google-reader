Backup full-text RSS content from Google Reader
-----------------------------------------------

Google Reader will be shut down soon: http://googlereader.blogspot.com/2013/03/powering-down-google-reader.html

For years, you have probably collected several useful RSS subscriptions which are no longer online.
They are still readable via Google Reader and this small tool will allow you to backup them offline forever.

It stores article content avalable via Reader API in html format (no images or styles).

Usage:

1. Install fetch-google-reader

```
pip install git+git://github.com/max-arnold/fetch-google-reader.git
```

2. Create directory to store your subscriptions

```
mkdir rss-backup
cd rss-backup
```

3. List your subscriptions
   
```
fetch-greader.py -u YOUR-USERNAME@gmail.com -p YOUR-PASSWORD

* Please specify feed number (-f, --feed) to fetch: *
[0] Atomized
[1] Both Sides of the Table
[2] Hacker News
[3] Signal vs. Noise
[4] хабрахабр: главная / захабренные
```

4. Fetch all items from specific feed (add --starred to store only starred items)

```
fetch-greader.py -u YOUR-USERNAME@gmail.com -p YOUR-PASSWORD -f 0

* Output directory: atomized *
---> atomized/2011-05-24-i-hate-google-everything/index.html
---> atomized/2011-01-19-toggle-between-root-non-root-in-emacs-with-tramp/index.html
---> atomized/2010-10-19-ipad/index.html
---> atomized/2010-09-01-im-not-going-back/index.html
---> atomized/2010-08-31-they-cant-go-back/index.html
---> atomized/2010-08-28-a-hudson-github-build-process-that-works/index.html
---> atomized/2010-08-18-frame-tiling-and-centering-in-emacs/index.html
---> atomized/2010-08-17-scratch-buffers-for-emacs/index.html
---> atomized/2010-07-01-reading-apress-pdf-ebooks-on-an-ipad/index.html
```

Items are stored in subdirectory named after item title, you can override this with --dir argument.


habrahabr.ru article
--------------------

http://habrahabr.ru/post/180111/
