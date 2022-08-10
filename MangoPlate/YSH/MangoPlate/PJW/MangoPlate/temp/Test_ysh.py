# -*- coding: utf-8 -*-

from collections import Counter

from konlpy.corpus import kolaw
from konlpy.tag import Hannanum
from konlpy.utils import concordance, pprint
from matplotlib import pyplot


def draw_zipf(count_list, filename, color='blue', marker='o'):
    sorted_list = sorted(count_list, reverse=True)
    pyplot.plot(sorted_list, color=color, marker=marker)
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.savefig(filename)


# doc = kolaw.open('constitution.txt').read()
a = open('C:\\Users\\Kosmo\\Desktop\\Test\\Test.txt',encoding='utf-8')
doc = a.read()
pos = Hannanum().pos(doc)
cnt = Counter(pos)
print('nchars :', len(doc))
print('ntokens :', len(doc.split()))
print('nmorphs :', len(set(pos)))
print('\nTop 10 frequent morphemes: '); pprint(cnt.most_common(10))
#print('\nLocation of "맛있다" in the document: ')
#concordance(u'맛있다', doc, show=True)

'''
print('nchars  :', len(doc))
print('ntokens :', len(doc.split()))
print('nmorphs :', len(set(pos)))
print('\nTop 20 frequent morphemes:'); pprint(cnt.most_common(20))
print('\nLocations of "대한민국" in the document:')
concordance(u'대한민국', doc, show=True)
'''
# draw_zipf(cnt.values(), 'zipf.png')