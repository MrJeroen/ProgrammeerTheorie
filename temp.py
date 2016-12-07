from list import Array
from score import Score
import pickle

with open ('algo2.py', 'rb') as fp:
    itemlist = pickle.load(fp)


new_array = Array(itemlist)
#print new_array
score = Score(new_array)

print score
