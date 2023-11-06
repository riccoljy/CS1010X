#################
# Q1a - Shuffle #
#################

def shuffle(a, times):
    if times == 0: return a
    new_a = []
    length = len(a)
    if length%2==0:
        half = length//2-1
    else:
        half = length//2
    for i in range(half):
        new_a.append(a[i])
        new_a.append(a[i+half+1])
    new_a.append(a[half])
    if len(a)%2==0: new_a.append(a[-1])
    return shuffle(new_a, times-1)
    

def test1a():
    print('=== Q1a ===')
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 1)==[1, 5, 2, 6, 3, 7, 4, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 2)==[1, 3, 5, 7, 2, 4, 6, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 3)==[1, 2, 3, 4, 5, 6, 7, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 1)==[1, 5, 2, 6, 3, 7, 4])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 2)==[1, 3, 5, 7, 2, 4, 6])
 
#test1a()


##########################
# Q1b - Back to Original #
##########################

def back_to_original(a):
    new_a = shuffle(a, 1)
    counter = 1
    while new_a != a:
        new_a = shuffle(new_a, 1)
        counter += 1
    return counter

def test1b():
    print('=== Q1b ===')    
    print(back_to_original([1, 2, 3, 4, 5, 6, 7, 8])==3)
    print(back_to_original([1, 2, 3, 4, 5])==4)
    print(back_to_original([1, 1, 1, 1])==1)
 
#test1b()

##############
# Question 2 #
##############

import csv
from datetime import datetime

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

def get_dates_for_hashtag(filename, hashtag):
    file = filter(lambda x: hashtag in x[3], read_csv(filename))
    res = set()
    for row in file:
        res.add(row[0])
    return list(res)
                

def test2a():
    print("===2a===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ObamacareFail")	
    tweets.sort()
    print(tweets == ['16-10-25', '16-10-29', '16-10-31'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ElectionDay")
    tweets.sort()
    print(tweets == ['16-08-09', '16-11-08'])
    print(get_dates_for_hashtag("donald-tweets.csv", "China")==[]) 

#test2a()

###############
# Question 2b #
###############

from datetime import datetime

def active_hour(filename,start_date,end_date):
    start_date, end_date = datetime.strptime(start_date, "%y-%m-%d"), datetime.strptime(end_date, "%y-%m-%d")
    file = filter(lambda x: start_date <= datetime.strptime(x[0], "%y-%m-%d") and datetime.strptime(x[0], "%y-%m-%d") <= end_date, read_csv(filename)[1:])
    res = {}
    for row in file:
        hour = datetime.strptime(row[1], "%X").hour
        res[hour] = res.get(hour, 0) + 1
    if not res: return []
    res = sorted(list(res.items()), key = lambda x: x[1])
    highest = res[-1][1]
    res = filter(lambda x: x[1] == highest, res)
    return sorted(list(map(lambda x: x[0], res)))
    
    
def test2b():
    print("===2b===")
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-08")==[21])
    print(active_hour("donald-tweets.csv", "16-08-23", "16-11-06")==[1])
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-06")==[0, 23])

#test2b()

###############
# Question 2c #
###############

def top_k(filename,k,start_date,end_date):
    start_date, end_date = datetime.strptime(start_date, "%y-%m-%d"), datetime.strptime(end_date, "%y-%m-%d")
    file = filter(lambda x: start_date <= datetime.strptime(x[0], "%y-%m-%d") and datetime.strptime(x[0], "%y-%m-%d") <= end_date, read_csv(filename)[1:])
    res = []
    for row in file:
        tweet, likes = row[2], int(row[4])
        res.append((tweet, likes))
    res = sorted(res, key = lambda x: x[1], reverse = True)[:k]
    return list(map(lambda x: x[0], res))
    
    
def test2c():
    print("===2c===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])

#test2c()


##############
# Question 3 #
##############
 
class Student:

    allcourses = {}
    
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_courses(self, *courses):
        for course in courses:
            self.courses.append(course)
            if course not in Student.allcourses: Student.allcourses[course] = []
            Student.allcourses[course].append(self)         

    def drop_courses(self, *courses):
        for course in courses:
            if course in self.courses:
                self.courses.remove(course)
                Student.allcourses[course].remove(self)

    def get_courses(self):
        return self.courses
            
    def common_courses(self,other):
        res = []
        for course in self.courses:
            if course in other.courses: res.append(course)
        return res        

    def is_coursemate(self,other):
        for course in self.courses:
            if course in other.courses: return True
        return False

    def common_friends(self,other):
        res = set()
        for course in self.courses:
            friends = Student.allcourses[course]
            if other in friends: return []
            for friend in friends:
                if friend.is_coursemate(other):
                    res.add(friend)
        return list(map(lambda x: x.name, res))

    def six_degrees(self,other):
        if self.is_coursemate(other): return 1
        elif self.common_friends(other): return 2
        for course in self.courses:
            coursemates = Student.allcourses[course]
            for student in coursemates:
                if student.common_friends(other): return 3
        
        


benj = Student("Ben Junior")
benj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS2016", "GEM2455")
tanj = Student("Tan Junior")
tanj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS3243")
amanda = Student("Amanda See")
amanda.add_courses("GEM1010", "CS1014",  "CS1231", "CS2017", "GEM2455")
ad = Student("Ad Lee")
ad.add_courses("CS1010", "CS1000", "CS2010", "CS2040", "CS1207")
ayush = Student("Ayush")
ayush.add_courses("MA1016", "MA1014", "MA2050", "MA2016")

print(benj.is_coursemate(tanj))
print(benj.is_coursemate(amanda))
print(benj.is_coursemate(ad))
print(benj.is_coursemate(ayush))
print(benj.common_courses(tanj))
print(benj.common_courses(amanda)) # Found interesting girl in class!
print(benj.common_courses(ad))
print(benj.common_courses(ayush))

amanda.drop_courses("CS1014", "GEM2455") # She disappears from our class :'(
amanda.add_courses("CS3243")
print(benj.is_coursemate(amanda))
print(benj.common_courses(amanda)) # Girl disappears
print(amanda.get_courses()) # What is she taking now? 

##print(benj.six_degrees(amanda)) # How can we get to know her?
print(benj.common_friends(amanda))
print(amanda.common_courses(tanj))

tanj.drop_courses("CS3243")
##print(benj.six_degrees(amanda)==None) 
print(benj.common_friends(amanda))

amanda.add_courses("MA2050")
ayush.add_courses("CS1000")
##print(benj.six_degrees(amanda)==3)
    
# sample execution
def test3():
    print("===3===")
    benj = Student("Ben Junior")
    benj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS2016", "GEM2455")
    tanj = Student("Tan Junior")
    tanj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS3243")
    amanda = Student("Amanda See")
    amanda.add_courses("GEM1010", "CS1014",  "CS1231", "CS2017", "GEM2455")
    ad = Student("Ad Lee")
    ad.add_courses("CS1010", "CS1000", "CS2010", "CS2040", "CS1207")
    ayush = Student("Ayush")
    ayush.add_courses("MA1016", "MA1014", "MA2050", "MA2016")

    print(benj.is_coursemate(tanj))
    print(benj.is_coursemate(amanda))
    print(benj.is_coursemate(ad))
    print(benj.is_coursemate(ayush)==False)
    print(benj.common_courses(tanj)==['CS1010', 'CS1014', 'CS2010', 'CS2060'])
    print(benj.common_courses(amanda)==['CS1014', 'GEM2455']) # Found interesting girl in class!
    print(benj.common_courses(ad)==['CS1010', 'CS2010'])
    print(benj.common_courses(ayush)==[])

    amanda.drop_courses("CS1014", "GEM2455") # She disappears from our class :'(
    amanda.add_courses("CS3243")
    print(benj.is_coursemate(amanda)==False)
    print(benj.common_courses(amanda)==[]) # Girl disappears
    print(amanda.get_courses()==['GEM1010', 'CS1231', 'CS2017', 'CS3243']) # What is she taking now? 

    print(benj.six_degrees(amanda)==2) # How can we get to know her?
    print(benj.common_friends(amanda)==['Tan Junior'])
    print(amanda.common_courses(tanj)==['CS3243'])

    tanj.drop_courses("CS3243")
    print(benj.six_degrees(amanda)==None) 
    print(benj.common_friends(amanda)==[])

    amanda.add_courses("MA2050")
    ayush.add_courses("CS1000")
    print(benj.six_degrees(amanda)==3)

    
#test3()
