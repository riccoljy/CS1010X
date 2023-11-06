from math import *

"""
--- 2 hours (120 minutes) ---
Start 1758
Pause 1815
(17 minutes)

--- 1 hour 43 minutes (103 minutes)
Start 0859
Pause 0919
(20 minutes)

--- 1 hour 23 minutes (83 minutes)
Start 1951
Pause 2034
(43 minutes)

-- 40 minutes ---
Start 2241
Pause


End 0904

"""
###############
# Question 1a #
###############
def smallest(*lst):
    if len(lst)==1 and lst[0] == 0: return 0
    lst = list(lst)
    res = ""
    while lst:
        if res != "":
            smallest = min(lst)
        else:
            smallest = min(filter(lambda x: x != 0, lst))
        lst.remove(smallest)
        res += str(smallest)
    return int(res)

def test1a():
    print('=== Q1a ===')
    print(smallest(9,1,3)==139)
    print(smallest(1,3,9,0,0)==10039)
    print(smallest(2,1,1,3,9,0)==101239)
 
##test1a() 

###############
# Question 1b #
###############
def second_smallest(*lst):
    smallest_num = str(smallest(*lst))
    def swap(intnum):
        copy = list(intnum)
        for i in range(1, len(intnum)):
            copy[-i], copy[-i-1] = copy[-i-1], copy[-i]
            res = "".join(copy)
            if res != intnum:
                return res
        return None
    res = swap(smallest_num)
    if res == None: return None
    return int(res)
    
def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3)==193)
    print(second_smallest(1,3,9,0,0)==10093)
    print(second_smallest(2,1,1,3,9,0)==101293)
    print(second_smallest(1,1,1)==None)
     
##test1b() 

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

###############
# Question 2a #
###############

def most_common_major(filename, year):
    file = filter(lambda x: x[0] == str(year), read_csv(filename))
    table = {}
    for row in file:
        year, sex, course, num = row
        if num.isdigit():
            table[course] = table.get(course, 0) + int(num)
    if not table: return None
    return max(table.items(), key = lambda x: x[1])[0]

def test2a():
    print('=== Q2a ===')
    print(most_common_major("graduates-by-first-degree.csv", 1993)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2000)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2010)=="Engineering Sciences")

##test2a()

###############
# Question 2b #
###############

def new_courses(filename,start_year,end_year):
    res = []
    old = filter(lambda x: int(x[0]) <= start_year, read_csv(filename)[1:])
    old_courses = []
    for row in old:
        year, sex, course, num = row
        if num.isdigit() and course not in old_courses:
            old_courses.append(course)
    newer = filter(lambda x: start_year < int(x[0]) <= end_year, read_csv(filename)[1:])
    res = {}
    for row in newer:
        year, sex, course, num = row
        if num.isdigit() and num != '0' and course not in old_courses and course not in res:
            res[course] = int(year)
    return list(res.items())
            

def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)==[('Education', 1995), ('Mass Communication', 1997)]
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)==[('Applied Arts', 2003), ('Services', 2008)]
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020)==[('Education', 1995), ('Mass Communication', 1997), ('Applied Arts', 2003), ('Services', 2008)])

#test2b()

###############
# Question 2c #
###############

def topk_growing_major(filename,k,start_year,end_year):
    file = filter(lambda x: start_year == int(x[0]) or int(x[0]) == end_year, read_csv(filename)[1:])
    coursedict = {}
    for row in file:
        year, sex, course, num = row
        if not num.isdigit() or num == '0': continue
        year, num = int(year), int(num)
        if course not in coursedict: coursedict[course] = {}
        if year == start_year: coursedict[course][year] = coursedict[course].get(year, 0) + num
        elif year == end_year: coursedict[course][year] = coursedict[course].get(year, 0) + num
    coursedict = dict(filter(lambda x: len(x[1]) == 2, coursedict.items()))
    for key, val in coursedict.items():
        inc_perc = (val[end_year] - val[start_year])/val[start_year]*100
        coursedict[key] = inc_perc
    return list(map(lambda x: x[0], sorted(coursedict.items(), key = lambda x : x[1], reverse = True)[:k]))


def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)==['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences']
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010)==['Health Sciences', 'Education'])
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014)==['Health Sciences', 'Education', 'Law'])

#test2c()
    
##############
# Question 3 #
##############

##############
# Question 3 #
##############

class Timeline:
    def __init__(self):
        self.people = []     
    def born(self, name, year, lifespan):
        new = Person(name, year, lifespan)
        new.timeline = self
        self.people.append(new)
        return new
    def get_people(self, year):
        return list(map(lambda x: (x.name, x.identity), filter(lambda x: year in range(x.start_end[0], x.start_end[1]), self.people)))

class Person:
    def __init__(self, name, year, lifespan):
        self.natural_death = year+lifespan
        self.timeline = None
        self.lifespan = lifespan
        self.name = name
        self.identity = year
        self.start_end = [year, year+lifespan]
    def jump(self, from_year, to_year, identity):
        if from_year not in range(self.start_end[0], self.start_end[1]): return "Not alive"
        if identity != self.identity:
            index = self.timeline.get_people(from_year).index((self.name, identity))
            self = self.timeline.people[index]
        new = self.timeline.born(self.name, from_year, self.lifespan)
        new.start_end[0] = to_year
        new.natural_death = self.natural_death - from_year + to_year
        new.start_end[1] = new.natural_death
        self.start_end[1] = from_year
    def kill(self, year, person, identity):
        if year not in range(person.start_end[0], person.start_end[1]) or \
           year not in range(self.start_end[0], self.start_end[1]) or \
           person.identity != identity:
            return False
        person.start_end[1] = year
        return True

def test3():
    print('=== Q3 ===')
    t = Timeline()
    thor = t.born("Thor",518,5000)
    thanos = t.born("Thanos",1950,1000000)

    print(t.get_people(2017)==[('Thor', 518), ('Thanos', 1950)])
    print(thor.kill(2018,thanos,1950)) # whoops. Violence. :'(
    print(not thor.kill(2018,thanos,1950)) # Can't kill him twice!
    print(t.get_people(2018)==[('Thor', 518)]) # Thanos dead.
    
    thor.jump(2023,2013,518)
    thor.jump(2014,2024,2023)

    print(set(t.get_people(2013))==set([('Thor', 2023), ('Thor', 518), ('Thanos', 1950)]))
    print(set(t.get_people(2014))==set([('Thor', 518), ('Thanos', 1950)]))

    print(t.get_people(2022)==[('Thor', 518)])
    print(t.get_people(2023)==[])
    print(t.get_people(2024)==[('Thor', 2014)])

    thanos.jump(2014,2024,1950)
    print(set(t.get_people(2024))==set([('Thor', 2014), ('Thanos', 2014)]))

    # New Thor and old Thanos jumped so only old Thor left
    print(t.get_people(2014)==[('Thor', 518)]) 
    print(t.get_people(2017)==[('Thor', 518)])

    #Thanos is no longer around to die. 
    print(not thor.kill(2018,thanos,1950))


#test3()


             
