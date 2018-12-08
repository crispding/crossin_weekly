# -*- coding: utf-8 -*-

import jieba
from collections import Counter

with open('sanguo-utf8.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = jieba.lcut(text)
words_valid = []
excludes = [
    '将军', '却说', '二人', '不可', '荆州', '不能', '如此', '商议', '如何', '主公', '军士', '左右',
    '军马', '引兵', '次日', '大喜', '天下', '东吴', '于是', '今日', '不敢', '魏兵', '陛下', '人马',
    '都督', '一人', '不知', '汉中', '众将', '只见', '后主', '蜀兵'
]

for word in words:
    if len(word) < 2:
        continue
    if word in excludes:
        continue
    if word.endswith('曰'):
        word = word[:-1]
    if "诸葛亮" in word or '孔明' in word:
        word = '孔明'
    elif "关公" in word or "云长" in word:
        word = "关羽"
    elif "玄德" in word or '皇叔' in word:
        word = "刘备"
    elif "孟德" in word or "曹丞相" in word:
        word = '曹操'
    words_valid.append(word)

ct = Counter(words_valid)
top_10 = ct.most_common(10)
print(top_10)
