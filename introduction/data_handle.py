# -*- coding: utf-8 -*-
"""
@Env 
@Time 2025/3/9 上午11:55
@Author yzpang
@Function: 处理数据
"""
import pandas as pd


def handle_train():
    df = pd.read_csv('../data/train.txt', sep='\t', encoding='utf-8', names=['text', 'label'])
    text_df = df['text']
    text_df.to_csv('text.txt', sep='\t', encoding='utf-8', index=False, header=None)


if __name__ == '__main__':
    handle_train()

