import json
import os
import sys
import xml.etree.ElementTree as etree

sys.path.append('D:\\PythonPro\\AFluentPython\\')

'''
工厂模式解析json、xml文件

'''
# 类JSONDataExtractor解析json文件: parsed_data()方法返回一个包含所有数据的字典(dict)
# 装饰器property 用于使parsed_data()变得更像一个普通的属性而非方法

class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


# factory function
def dataextraction_factory(filepath):

    if filepath.endswith('json'):       # endwiths() 判断字符串是否以指定后缀结尾
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f'Cannot extract data from {filepath}')

    return extractor(filepath)


'''
    extract_data_from是dataextraction_factory的一个函数装饰器，增加了异常处理机制
'''
def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def show_jsondata():
    json_factory = extract_data_from("data\\movies.json")            # 保证异常机制的有效性
    json_data = json_factory.parsed_data
    print(f"Found: {len(json_data)} movies")

    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")

        director = movie['director']
        if director:
            print(f"director: {director}")
        
        cast = movie['cast']
        if cast:
            print(f"cast: {cast}")

        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
    

def show_xmldata():
    xml_dir = 'data\\person.xml'
    xml_factory = extract_data_from(xml_dir)
    xml_data = xml_factory.parsed_data
    # ElementTree.parse.findall()  用于寻找所有姓为Liar的person元素
    liars = xml_data.findall(f".//person[lastName='Liar']")     # 寻找所有姓为Liar的person元素

    for liar in liars:
        firstname = liar.find('firstName').text         # 去标签<firstname>的内容text
        print(f"firstname: {firstname}")

        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')

        [print(f"phone number ({p.attrib['type']}): ", p.text) for p in liar.find('phoneNumbers')]
        print()

        print("Address: ")
        [print(f"streetAddress: {add.find('streetAddress').text} \
        \ncity: {add.find('city').text}\
        \nstate: {add.find('state').text}\
        \npostalCode: {add.find('postalCode').text}")\
         for add in liar.findall('address')]
        print()


def main():
    json_dir = 'data\\movies.json'
    json_factory = JSONDataExtractor(json_dir)
    json_data = JSONDataExtractor(json_factory)

    # print(f'json_datas: {json_datas}')

    # xml_dir = 'data\\person.xml'
    # xml_datas = XMLDataExtractor(xml_dir).parsed_data
    # # print(xml_datas['persons'])
    # for i in xml_datas['persons']:
    #     print(i)


if __name__ == '__main__':
    # main()
    print("+++++++++parse json++++++++")
    show_jsondata()

    print()
    print("+++++++++parse xml++++++++")
    show_xmldata()

    



        

    



    