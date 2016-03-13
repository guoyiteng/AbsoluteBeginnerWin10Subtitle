import HTMLprocess
import requests
import XMLprocess
from xml.parsers.expat import ParserCreate
import srt
import os

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
        xml = requests.get(URL).text
        handler = XMLprocess.DefaultSaxHandler()
        XMLparser = ParserCreate()
        XMLparser.StartElementHandler = handler.start_element
        XMLparser.CharacterDataHandler = handler.char_data
        XMLparser.Parse(xml)
        subtitle = []
        for idx, line in enumerate(handler.subs):
            subtitle.append(srt.Subtitle(index=idx, start=line['start'], end=line['end'], content=line['content'].replace('\n', '')))
        f.write(srt.compose(subtitle))


html = ''
with open('./MVA.html', 'r', encoding='utf-8') as f:
    html = f.read()
parser = HTMLprocess.MyHTMLParser()
parser.feed(html)
for i in range(80):
    print(i)
    writeCaption('https://cp-mlxprod-static.microsoft.com/012328-1008/en-us/content/content_%s/video_cc.xml' % parser.urlid[i], i+1)
