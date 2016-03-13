# -*- coding: utf-8 -*-

import HTML
import requests
import os

def createURL(href):
    return 'https://channel9.msdn.com' + href + '/captions?f=webvtt&l=en'

def createURLList(nameList, URLList):
    for name in nameList:
        URLList.append(createURL(name))
    return URLList

def triNum(num):
    num = str(num)
    if len(num) == 1:
        return '00'+num
    if len(num) == 2:
        return '0' + num
    if len(num) == 3:
        return num

def writeCaption(URL, index):
    directory = './UWP-' + triNum(index) + '/subtitles'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open('./UWP-' + triNum(index) + '/subtitles/Captions.srt', 'w', encoding='utf-8') as f:
        r = requests.get(URL)
        f.write(r.text)

if __name__ == '__main__':
    URLList = []
    for i in range(8):
        parser = HTML.MyHTMLParser()
        r = requests.get('https://channel9.msdn.com/Series/Windows-10-development-for-absolute-beginners?page=' + str(i+1))
        parser.feed(r.text)
        URLList = createURLList(parser.name, URLList)
    for idx, url in enumerate(URLList):
        writeCaption(url, idx + 1)