from html.parser import HTMLParser

from nodes import *

class ParseHtml(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag: ", tag)

        attrMap = {}
        for attr in attrs:
            print("   attrs:", attr)
            attrMap[attr[0]] = attr[1]
            



    def handle_endtag(self, tag): 
        print("Encounterd an end tag: ", tag)

    def handle_data(self, data):
        print("Encounterd data: ", data)
