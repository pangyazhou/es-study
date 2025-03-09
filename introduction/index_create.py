# -*- coding: utf-8 -*-
"""
@Env 
@Time 2025/3/9 上午11:36
@Author yzpang
@Function: 创建索引
"""
import httpx
import requests
import json
import pandas as pd


ES_URL = 'http://localhost:9200'
INDEX_SETTING_DATA = json.load(open('index_setting.json'))


def delete_index(index):
    """
    删除索引
    :param index:
    :return:
    """
    response = httpx.delete(f'{ES_URL}/{index}')
    print("Response JSON: ", response.json())


def create_index(index, data):
    """
    创建索引,配置Setting和Mapping
    :param index:
    :param data:
    :return:
    """
    response = httpx.put(f'{ES_URL}/{index}', json=data)
    print("Response JSON: ", response.json())


def insert_doc(index, doc):
    """
    插入单条文档
    :param index:
    :param doc:
    :return:
    """
    response = httpx.post(f'{ES_URL}/{index}/_doc', json=doc)
    print("Response JSON: ", response.json())


def insert_docs(index, filename):
    """
    批量插入文档
    :param filename:
    :param index:
    :return:
    """
    df = pd.read_csv(filename, sep='\t', encoding='utf-8', names=['text', 'label'])
    text_list = df['text'].tolist()
    doc = {}
    for text in text_list[:300]:
        doc['remark'] = text
        doc['description'] = text
        insert_doc(index, doc)


def insert_batch(index, filename):
    df = pd.read_csv(filename, sep='\t', encoding='utf-8', names=['text', 'label'])
    text_list = df['text'].tolist()
    bulk_data = []
    # 构建批量文档列表
    for text in text_list:
        index_data = {"index": {"_index": index}, "_type": "_doc"}
        doc = {"remark": text, "description": text}
        bulk_data.append(json.dumps(index_data))
        bulk_data.append(json.dumps(doc))
    bulk_data = "\n".join(bulk_data) + "\n"
    # 调用批量插入接口
    headers = {'Content-Type': 'application/json'}
    requests.post(f'{ES_URL}/_bulk', headers=headers, data=bulk_data)


if __name__ == '__main__':
    index_name = 'demo-index'
    file_name = "../data/train.txt"
    delete_index(index_name)
    create_index(index_name, INDEX_SETTING_DATA)
    insert_batch(index_name, file_name)
