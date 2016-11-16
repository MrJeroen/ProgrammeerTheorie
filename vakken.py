import csv

with open('studenten_roostering.csv', 'rt') as vak:
    vakken = csv.reader(vak, delimiter = ',')
    var = 'sturen en bewegen'
    counter = 0
    for lines in vakken:
        for courses in lines:
            if var in courses:
                counter += 1
    print counter
    print lines
