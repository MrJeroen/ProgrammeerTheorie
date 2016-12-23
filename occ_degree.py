from plot3 import Plot3
import pickle
from list import Array
from score import Score
from main import room_list

# Open a list is the best schedule.
with open ('stoch100k3lists.py', 'rb') as fp:
    schedule = pickle.load(fp)

array = Array(schedule)
score = Score(array)

# Create lists for the y axis of the bar charts.
occupation_degree = []
occupation_seats = []

for rooms in room_list:
    # calculate the values of the y-axis for occupation of seats and timeslots
    occupation_degree.append(((20.0 - (room_list[rooms].occupation)) / 20.0) *100)
    occupation_seats.append((((room_list[rooms].seat_occ))/(room_list[rooms].seats*20.0))*100)

# Create a bar chart of the occupation degree of timeslots.
Plot3(occupation_degree, "Occupation degree of timeslots")
# Create a bar chart of the occupation degree of seats
#Plot3(occupation_seats, "Occupation degree of seats")
