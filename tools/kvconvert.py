#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ** This is experimental quick script, don't use it for production. **
# Converts a kvtml eg. http://edu.kde.org/contrib/kvtml/gretools.kvtml
# into FlashLearner compatible format.
# 														-- ideamonk at gmail.com

import sys

kv = sys.stdin.xreadlines()
for i in xrange (75):
    crap = kv.readline()

while True:
    try:
        chunk = kv.readline()
        wtype,chunk = chunk.split('''t="''',1)[1].split('''"><o>''',1)
        word,chunk = chunk.split('''</o><t>''',1)
        definition,chunk = chunk.split('''</t>''',1)
        print "%s:%s:s%s" % (wtype,word,definition)
    except:
        break
