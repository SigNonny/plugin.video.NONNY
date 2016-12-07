# -*- coding: utf-8 -*-

import urlparse,sys
from resources.lib import videoSource

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')
url = params.get('url')

if action == None:
	videoSource.indexer().root()

elif action == 'addBookmark':
	from lamlib import bookmarks
	bookmarks.add(url)

elif action == 'deleteBookmark':
	from lamlib import bookmarks
	bookmarks.delete(url)

elif action == 'bookmarks':
	videoSource.indexer.bookmarks()

elif action == 'youtube':
	videoSource.indexer().youtube(url)

elif action == 'videos':
	videoSource.indexer().videos(url)

elif action == 'play':
	videoSource.indexer().play(url)