import collections
import concurrent.futures
import os
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

def transform(x):
    print (f' Process {os.getpid()} working record {x.name}')
    time.sleep(1)
    result = {'name':  x.name,  'age':  2017 - x.born}
    print (f' Process {os.getpid()} done processing record {x.name}')
    return  result

if __name__ == '__main__':
    pprint(scientists)
    print()
    
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(transform, scientists)


    end = time.time()

    print(f'\nTime to complete: {end - start:.2f}s\n')
    pprint(tuple(result))



# (Scientist(name=' Ada Lovelace', field='math', born=1815, nobel=False),
#  Scientist(name=' Emmy Noether', field='math', born=1882, nobel=False),
#  Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
#  Scientist(name=' Tu-Youyou', field='chemistry', born=1930, nobel=True),
#  Scientist(name=' Ada-Yonath', field=' chemistry', born=1939, nobel=True),
#  Scientist(name=' Vera Rubin', field='astronomy', born=1928, nobel=False),
#  Scientist(name='Sally Ride', field='physics', born=1951, nobel=False))

#  Process 6338 working record  Ada Lovelace
#  Process 6340 working record  Emmy Noether
#  Process 6337 working record Marie Curie
#  Process 6339 working record  Tu-Youyou
#  Process 6341 working record  Ada-Yonath
#  Process 6342 working record  Vera Rubin
#  Process 6344 working record Sally Ride
#  Process 6338 done processing record  Ada Lovelace
#  Process 6337 done processing record Marie Curie
#  Process 6340 done processing record  Emmy Noether
#  Process 6339 done processing record  Tu-Youyou
#  Process 6341 done processing record  Ada-Yonath
#  Process 6342 done processing record  Vera Rubin
#  Process 6344 done processing record Sally Ride

# Time to complete: 1.18s

# ({'age': 202, 'name': ' Ada Lovelace'},
#  {'age': 135, 'name': ' Emmy Noether'},
#  {'age': 150, 'name': 'Marie Curie'},
#  {'age': 87, 'name': ' Tu-Youyou'},
#  {'age': 78, 'name': ' Ada-Yonath'},
#  {'age': 89, 'name': ' Vera Rubin'},
#  {'age': 66, 'name': 'Sally Ride'})