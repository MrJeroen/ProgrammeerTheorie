# ProgrammeerTheorie
Lectures and Roosters
Jeroen Gomes, 10004504
Louise Dam, 10560661

VAKKEN.PY
In vakken.py the amount of students per course are counted.

BASE.PY
In base.py are all the classes of this project defined.

MAIN.PY
Base.py is called in main.py to create lists of all the objects.
Lists for courses, lessons, students and rooms.

LIST.PY
Base.py and main.py are called in list.py to create the schedule in a
numpy arrray from the list lessons.

SCORE.PY
Score.py takes an array made in list.py and counts the points a schedule gets.

ALGORITHMS.PY
Algorithms forms the base for all the algorithms.
It has all the different shuffle functions for the algorithms.

PLOT.PY
Plot.py can be called by the algorithms to draw frequency graph.

PLOT2.PY
Plot2.py can be called by the algorithms to draw a line graph of the
of the scores.

ALGORITME1.PY
Algoritme1 calls algorithms to create a certain amount of random schedule,
calculate their score and appended their score to a list so a frequency graph
can be drawn by plot.py of distribution of scores.
HOW TO RUN: standard iterations 100

ALGORITME2.PY
Algoritme2.py calls algorithms to get a random schedule as a base schedule.
From the base schedule steps are created, if a step is an improvement of the score
this new list will become the base list and the score will be appended to a list.
This list will be plotted in a line graph by plot2.py
HOW TO RUN: standard iterations 100

ALGORITME3.py
Algoritme3.py calls algorithms to get a random schedule as a base schedule.
From the base schedule a certain amount of steps are created, if the best step
is an improvement the step will be taken. The list of the best step will become
the base list and the score will be appened to a list of best scores.
This list will be plotted in a line graph by plot2.py
HOW TO RUN: standard iterations 100 for 10 possibilities

ALGORITME4.PY
Algoritme4.py calls algorithms to get a random schedule as base schedule.
From the base schedule a certain amount of steps are created, if the best step
is accepted by the temperature this step will be taken. The list of the best step
will become the base list and the score will be appened to a list of best scores.
This list will be plotted in a line graph by plot2.py
HOW TO RUN: standard iterations 100 for 10 possibilities

USED PACKAGES
To run the code the packages numpy and matplotlib must be installed.
