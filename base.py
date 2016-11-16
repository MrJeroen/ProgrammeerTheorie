class Courses(object):
    def __init__(self, name, hc, wc, wc_students, pr, pr_students, students):
        self.name = name
        self.hc = hc
        self.wc = wc
        self.wc_students = wc_students
        self.pr = pr
        self.pr_students = pr_students
        self.students = students

    def totaal_activiteiten(self):
         total = int(self.hc) + int(self.wc) + int(self.pr)
         return total

    def type_activiteit(self):
        if int(self.hc) > 0:
            harry = 'hc'
            return harry
        if int(self.wc) > 0:
            hagrid = 'wc'
            return hagrid
        if int(self.pr) > 0:
            ron = 'pr'
            return ron

class Lessons(object):
    def __init__(self, name, group_name, amount, sort):
        self.name = name
        self.group_name = group_name
        self.sort = sort
        self.amount = amount
        #self.group_stud = group_stud
    # def info():
    #     print self.name

class Students(object):
    def __init__(self, id, vak1, vak2, vak3, vak4, vak5):
        self.id = id
        self.vak1 = vak1
        self.vak2 = vak2
        self.vak3 = vak3
        self.vak4 = vak4
        self.vak5 = vak5

class Room(object):
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats
