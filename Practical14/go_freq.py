#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2024/05/20 17:24:41
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt
import xml.sax
import xml.sax.handler
from xml.sax.xmlreader import AttributesImpl
import datetime
import xml.dom.minidom

# define functions
def count_go_terms_dom(xml_path:str):
    # Use DOM API to calculate the frequency
    DOMTree = xml.dom.minidom.parse(xml_path)
    obo = DOMTree.documentElement
    terms = obo.getElementsByTagName("term")
    counter = {"biological_process":0, "molecular_function":0, "cellular_component":0}

    for term in terms:
        if term.getElementsByTagName("namespace")[0].firstChild.nodeValue == 'biological_process':
            counter["biological_process"] += 1
        elif term.getElementsByTagName("namespace")[0].firstChild.nodeValue == "molecular_function":
            counter["molecular_function"] += 1
        elif term.getElementsByTagName("namespace")[0].firstChild.nodeValue == "cellular_component":
            counter["cellular_component"] += 1
    return counter

class GO_handler(xml.sax.ContentHandler):
    # define custom ContentHandler class
    def __init__(self) -> None:
        self.counter = {  # Counter dict
            "biological_process":0,
            "molecular_function":0,
            "cellular_component":0
        }
        self.start_time = 0
        self.end_time = 0
        self.process_time = 0
        self.currentElement = ""
        self.current_text = []  # This is for string buffer

    def startDocument(self) -> None:
        self.start_time = datetime.datetime.now()
    
    def endDocument(self) -> None:
        self.end_time = datetime.datetime.now()
        self.process_time = self.end_time - self.start_time
    
    def startElement(self, name: str, attrs: AttributesImpl) -> None:
        # When read start tag, this method will be called.
        if name == "namespace":
            self.currentElement = name
        self.current_text = []
    
    def endElement(self, name: str) -> None:
        # When read end tag, this method will be called.
        content = ''.join(self.current_text)
        if self.currentElement == "namespace" and content in self.counter.keys():
            self.counter[content] += 1
            self.currentElement = None
    
    def characters(self, content: str) -> None:
        # When read content(text), this method will be called.
        self.current_text.append(content)

def count_go_terms_sax(file_path:str):
    # Using SAX API to calculate the frequency
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = GO_handler()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    return handler

def draw_bar(dict:dict, title:str):
    # Draw bar figure
    plt.bar(x=dict.keys(), height=dict.values())
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    # XML file path
    file_path = "./go_obo.xml"
    # DOM API
    start_time_dom = datetime.datetime.now()
    print("Start analysis by DOM")
    result = count_go_terms_dom(file_path)
    end_time_dom = datetime.datetime.now()
    process_time_dom = end_time_dom - start_time_dom
    print(f"Complete in {process_time_dom.seconds}s with DOM") # Processing time
    print(result)
    draw_bar(result, "DOM result")
    # SAX API
    print("Start analysis by SAX")
    sax_handler = count_go_terms_sax(file_path)
    print(f"Complete in {sax_handler.process_time.seconds}s with SAX") # Processing time
    print(sax_handler.counter)
    draw_bar(sax_handler.counter, "SAX result")

    # DOM use 11 seconds, SAX use 3 seconds SAX is faster than DOM