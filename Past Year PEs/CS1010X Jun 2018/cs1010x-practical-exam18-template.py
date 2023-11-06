import csv
from math import sqrt

##############
# Question 1 #
##############


###################
# Q1a - In circle #
###################

def digit_product(n):
    res = 1
    for digit in str(n):
        res *= int(digit)
    return res

def test1a():
    print('=== Q1a ===')
    print(digit_product(1111)==1)
    print(digit_product(123)==6)
    print(digit_product(123041)==0)

#test1a()



########################
# Q1b - Furthest Apart #
########################

def max_digit_product(n,k):
    strn = str(n)
    res = 1
    while k > 0:
        largest = max(strn)
        res *= int(largest)
        index = strn.index(largest)
        strn = strn[:index] + strn[index+1:]
        k -= 1
    return res

def test1b():
    print('=== Q1b ===')
    print(max_digit_product(11123,1)==3)
    print(max_digit_product(11123,2)==6)
    print(max_digit_product(1111111,5)==1)
    print(max_digit_product(189113451,2)==72)

#test1b()


###########################
# Q2 - Show me the Money! #
###########################
# These functions are provided for you
# Do not make any changes to them

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)
def count_NA_employment(data):
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):
    return len(list(filter(lambda x: x[5] == "NA", data)))

#######
# Q2A #
#######

def parse_data(filename):
    file = read_csv(filename)[1:]
    temp = {}
    for row in file:
        year, university, school, degree, var, val = row
        year = int(year)
        key = (year, university, school, degree)
        if key not in temp: temp[key] = {}
        temp[key][var] = float(val)
    res = []
    for key, val in temp.items():
        entry = list(key) + [val.get("employment_rate_overall", "NA"), val.get("basic_monthly_median", "NA")]
        res.append(entry)
    return res
        
        

def count_NA_employment(data):   # Helper for testing
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):       # Helper for testing
    return len(list(filter(lambda x: x[5] == "NA", data)))

def test2a():
    print('=== Q2a ===')
    print(len(parse_data("employment.csv"))==179)
    print(count_NA_employment(parse_data("employment.csv"))==1)
    print(count_NA_salary(parse_data("employment.csv"))==1)

#test2a()

#######
# Q2B #
#######

def compute_employment_rate(filename,university,degree,start,end):
    file = filter(lambda x: x[1] == university and\
                  x[3] == degree and\
                  start <= x[0] <= end,\
                  parse_data(filename))
    res = []
    for row in file:
        res.append(row[-2])
    res = tuple(filter(lambda x: isinstance(x, float), res))
    if not res: return "NA"
    res = sum(res)/len(res)
    return res
        

def test2b():
    print('=== Q2b ===')
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)==100.0)
    print(compute_employment_rate("employment.csv",'Nanyang Technological University', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2014,2014)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Computing (Computer Science)",2014,2018)==93.8)

#test2b()

#######
# Q2C #
#######

def top_k_degree(filename,start,end,k):
    file = filter(lambda x: start <= x[0] <= end, parse_data(filename))
    temp = {}
    for row in file:
        year, uni, sch, deg, emp, sal = row
        key = (deg, uni)
        if key not in temp: temp[key] = {}
        if sal != "NA": temp[key][year] = sal
    res = []
    for degree, sal in temp.items():
        lst = sorted(list(sal.items()), key = lambda x: x[0])
        if len(lst) != (end-start+1): continue
        for i in range(len(lst)-1):
            curr = lst[i]
            nxt = lst[i+1]
            if nxt[1] <= curr[1]: break
            entry = [degree, (sum(map(lambda x: x[1], lst))/len(lst))]
            res.append(entry)
    return list(map(lambda x: list(x[0]), sorted(res, key = lambda x: x[1], reverse = True)[:k]))
    

def test2c():
    print('=== Q2c ===')
    print(top_k_degree("employment.csv",2014,2015,3)==\
          [['Business and Computing', 'Nanyang Technological University'],\
           ['Bachelor of Engineering (Computer Engineering)', 'National University of Singapore'], \
           ['Bachelor of Business Administration (Hons)', 'National University of Singapore']])
    print(top_k_degree("employment.csv",2014,2018,3)==[])

#test2c()

################################
# Q3 - Social Network Security #
################################

privacy_settings = ["private", "friends", "FOF", "public"]
# private = no one can read
# friends = friends can read
# FOF = friends of friends can read
# public = anyone can read

class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.posts = []
        self.pendingapproval = []
        self.last_privacy = ("public",)
    def request(self, user):
        if self in user.pendingapproval: return False
        elif user in self.pendingapproval:
            self.pendingapproval.remove(user)
            self.friends.append(user)
            user.friends.append(self)
        else: user.pendingapproval.append(self)
        return True
    def accept(self, user):
        if user not in self.pendingapproval: return False
        self.pendingapproval.remove(user)
        self.friends.append(user)
        user.friends.append(self)
        return True
    def is_friend(self, user):
        return user in self.friends
    def unfriend(self, user):
        if user not in self.friends: return False
        self.friends.remove(user)
        user.friends.remove(self)
        return True
    def post(self, message, *privacy_setting):
        if not privacy_setting: privacy_setting = self.last_privacy
        elif privacy_setting[0] not in privacy_settings: return "Bad privacy setting"
        self.posts.append((message, privacy_setting[0]))
        self.last_privacy = privacy_setting
    def check_FOF(self, user):
        if self in user.friends: return True
        for friend in self.friends:
            if user in friend.friends: return True
        return False
    def read_posts(self, user):
        if user == self: return list(map(lambda x: x[0], self.posts))
        res = []
        for post in user.posts:
            if (post[1] == "private"): continue 
            elif (post[1] == "public") or\
                 ((post[1] == "friends") and (self in user.friends)) or\
                 ((post[1] == "FOF") and (self.check_FOF(user))):
                res.append(post[0])
        return res
    def update_privacy(self, message, privacy_setting):
        if privacy_setting not in privacy_settings: return "Bad privacy setting"
        posts = tuple(map(lambda x: x[0], self.posts))
        if message not in posts: return "Message not found"
        index = posts.index(message)
        self.posts[index] = (self.posts[index][0], privacy_setting)
            

def test3():
    print('=== Q3 ===')
    ben = User("Ben")
    oana = User("Oana")
    chenhao = User("Chenhao")
    clement = User("Clement")

    print(ben.is_friend(oana)==False)
    print(ben.is_friend(chenhao)==False)
    print(ben.accept(oana)==False)

    print(oana.request(ben)==True)
    print(oana.request(chenhao)==True)
    print(oana.request(chenhao)==False)
    print(oana.is_friend(ben)==False)
    print(oana.is_friend(chenhao)==False)

    print(ben.accept(oana)==True)
    print(chenhao.request(oana)==True)
    print(oana.is_friend(ben)==True)
    print(oana.is_friend(chenhao)==True)

    ben.post("CS1010X is fun")
    ben.post("No tutorials next week","FOF")
    ben.post("Did you remember to order pizza?","friends")
    ben.post("Exam grading will be done on Tuesday.")
    ben.post("Finals will be very difficult","private")

    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    ben.post("Finals will be very difficult")
    ben.update_privacy("Finals will be very difficult","public")
    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])

    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Finals will be very difficult'])
    print(clement.read_posts(ben) == ['CS1010X is fun', 'Finals will be very difficult'])

    ben.update_privacy("Finals will be very difficult","friends")
    print(ben.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben)== ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    ben.update_privacy("Finals will be very difficult","friends")
    print(
    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

    print(oana.unfriend(chenhao)==True)
    print(oana.unfriend(chenhao)==False)
    print(oana.is_friend(chenhao)==False)

    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

#test3()
