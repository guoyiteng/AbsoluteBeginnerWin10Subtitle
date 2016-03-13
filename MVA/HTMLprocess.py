#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self._urlid = []

    def handle_starttag(self, tag, attrs):
        if 'class' in list(dict(attrs).keys()) and 'id' in list(dict(attrs).keys()) and dict(attrs)['class'].startswith('course-components syllabusLevel-1 prereq-satisfied'):
            self._urlid.append(dict(attrs)['id'])
            self._urlid[-1] = self._urlid[-1][9:]
            self._isAsse = False
        if 'class' in list(dict(attrs).keys()) and 'title' in list(dict(attrs).keys()) and dict(attrs)['class'] == 'corse-item-name module-level-assessment':
            self._urlid.pop()

    @property
    def urlid(self):
        return self._urlid