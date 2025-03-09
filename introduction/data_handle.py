# -*- coding: utf-8 -*-
"""
@Env 
@Time 2025/3/9 上午11:55
@Author yzpang
@Function: 处理数据
"""
import json

import pandas as pd


def handle_train():
    df = pd.read_csv('../data/train.txt', sep='\t', encoding='utf-8', names=['text', 'label'])
    text_df = df['text']
    text_df.to_csv('text.txt', sep='\t', encoding='utf-8', index=False, header=None)


def generate_json():
    df = pd.read_csv('../data/train.txt', sep='\t', encoding='utf-8', names=['text', 'label'])
    json_list = []
    text_list = df['text'].tolist()
    index_json = {"index": {}}
    for text in text_list[:5]:
        # 添加index行
        json_list.append(json.dumps(index_json, ensure_ascii=False))
        # 添加doc行
        doc = {"remark": text, "description": text}
        json_list.append(json.dumps(doc, ensure_ascii=False))
    print(json_list)
    with open('../data/train.json', 'w', encoding='utf-8') as f:
        for item in json_list:
            f.write(item + "\n")


if __name__ == '__main__':
    # handle_train()
    generate_json()
