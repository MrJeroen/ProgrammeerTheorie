from list import Array
from score import Score
import pickle

with open ('algo3.py', 'rb') as fp:
    itemlist = pickle.load(fp)

new_array = Array(itemlist)
score = Score(new_array)

print score
