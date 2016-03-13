#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint
import io  
import sys


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self._name = []

    def handle_starttag(self, tag, attrs):
        if 'class' in list(dict(attrs).keys()) and 'href' in list(dict(attrs).keys()) and dict(attrs)['class'] == 'title':
            self._name.append(dict(attrs)['href'])

    @property
    def name(self):
        return self._name