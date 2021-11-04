'''
factory 工厂模式
'''
import sys
import os
import json


class A:
    pass


def main():
    a = A()
    b = A()

    print(id(a) == id(b))
    print(a, b)


class JSONParser:
    def parse(self, raw_data):
        return json.loads(raw_data)  # str 2 dict


class XMLParser:
    def parse(self, raw_data):
        return xml2dict(raw_data)


def new_parser(type, **kwargs):
    if type == 'json':
        return JSONParser()
    elif type == 'xml':
        return XMLParser()


if __name__ == '__main__':
    parser = new_parser('json')
    with open('hello.json') as fp:
        data = parser.parse(fp.read())
    print(data)
    
    