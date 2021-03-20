import collections
import time
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

import time

def transform(x):
    print (f' Processing record record {x.name}')
    time.sleep(1)
    result = {'name':  x.name,  'age':  2017 - x.born}
    print(f' Done processing record {x.name}')
    return  result

start = time.time()

result = tuple(map(transform, scientists))

end = time.time()

print(f'\nTime to complete: {end - start:.2f}s\n')
pprint(result)

pprint(result)



# results:
# (Scientist(name=' Ada Lovelace', field='math', born=1815, nobel=False),
#  Scientist(name=' Emmy Noether', field='math', born=1882, nobel=False),
#  Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
#  Scientist(name=' Tu-Youyou', field='chemistry', born=1930, nobel=True),
#  Scientist(name=' Ada-Yonath', field=' chemistry', born=1939, nobel=True),
#  Scientist(name=' Vera Rubin', field='astronomy', born=1928, nobel=False),
#  Scientist(name='Sally Ride', field='physics', born=1951, nobel=False))

#  Processing record record  Ada Lovelace
#  Done processing record  Ada Lovelace
#  Processing record record  Emmy Noether
#  Done processing record  Emmy Noether
#  Processing record record Marie Curie
#  Done processing record Marie Curie
#  Processing record record  Tu-Youyou
#  Done processing record  Tu-Youyou
#  Processing record record  Ada-Yonath
#  Done processing record  Ada-Yonath
#  Processing record record  Vera Rubin
#  Done processing record  Vera Rubin
#  Processing record record Sally Ride
#  Done processing record Sally Ride
#  Time to complete: 7.03s
# ({'age': 202, 'name': ' Ada Lovelace'},
#  {'age': 135, 'name': ' Emmy Noether'},
#  {'age': 150, 'name': 'Marie Curie'},
#  {'age': 87, 'name': ' Tu-Youyou'},
#  {'age': 78, 'name': ' Ada-Yonath'},
#  {'age': 89, 'name': ' Vera Rubin'},
#  {'age': 66, 'name': 'Sally Ride'})