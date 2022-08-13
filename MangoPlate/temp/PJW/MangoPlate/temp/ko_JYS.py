from re import X
from konlpy.tag import Okt
from collections import Counter

filename = "댓글.txt"
f = open(filename, 'r', encoding='utf-8')
news =  f.read()

okt = Okt()
noun = okt.nouns(news)
for i,x in enumerate(noun):
    if len(x)<2:
        noun.pop(i)

count = Counter(noun)

noun_list = count.most_common(100)
for x in noun_list:
    print(x)