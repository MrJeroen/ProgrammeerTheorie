from plot3 import Plot3
import pickle
from list import Array
from score import Score
from main import room_list

with open ('algo1.py', 'rb') as fp:
    schedule = pickle.load(fp)

array = Array(schedule)
score = Score(array)

occupation_degree = []
occupation_seats = []
for rooms in room_list:
    occupation_degree.append(((20.0 - (room_list[rooms].occupation)) / 20.0) *100)
    occupation_seats.append(((room_list[rooms].seats - (room_list[rooms].occupation))/ (room_list[rooms].seats*1.0))*100)
    print room_list[rooms].seats
    print room_list[rooms].occupation

print occupation_seats
print occupation_degree
#Plot3(occupation_degree,"Occupation of classrooms")
