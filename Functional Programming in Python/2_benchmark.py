import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist',[
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name=' Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name=' Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name=' Tu-Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name=' Ada-Yonath', field=' chemistry', born=1939, nobel=True),
    Scientist(name=' Vera Rubin', field='astronomy',born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

pprint(scientists)
print()

def transform(x):
    return  {'name':  x.name,  'age':  2017 - x.born}

result = tuple(map(transform, scientists))

pprint(result)

# result:
# (Scientist(name=' Ada Lovelace', field='math', born=1815, nobel=False),
#  Scientist(name=' Emmy Noether', field='math', born=1882, nobel=False),
#  Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
#  Scientist(name=' Tu-Youyou', field='chemistry', born=1930, nobel=True),
#  Scientist(name=' Ada-Yonath', field=' chemistry', born=1939, nobel=True),
#  Scientist(name=' Vera Rubin', field='astronomy', born=1928, nobel=False),
#  Scientist(name='Sally Ride', field='physics', born=1951, nobel=False))

# ({'age': 202, 'name': ' Ada Lovelace'},
#  {'age': 135, 'name': ' Emmy Noether'},
#  {'age': 150, 'name': 'Marie Curie'},
#  {'age': 87, 'name': ' Tu-Youyou'},
#  {'age': 78, 'name': ' Ada-Yonath'},
#  {'age': 89, 'name': ' Vera Rubin'},