##########################################
# Question 1a: Alien numbers [ 5 Marks ] #
##########################################

def ET_number(num, mapping):
    # One of the corner cases is when we need to generate the number 0
    if num == 0:
        return mapping[0]
    base = len(mapping)
    alien_num = ''
    count = 0
    while num > 0:
        alien_num = mapping[num%base] + alien_num
        num = num//base
        count += 1
    return alien_num

def test1a():
    print("=====Test 1a=====")
    # checking if simple decimal numbers can be produced
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for switching some digits
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79')
    # checking for different bases
    print(ET_number(10, ('0','1','2','3','4','5')) == '14')
    print(ET_number(6, ('0','4')) == '440')
    print(ET_number(5, ('1', '0')) == '010')
    print(ET_number(10, ('a', 'b', 'c')) == 'bab')

#test1a()

#################################################
# Question 1b: Largest alien number [ 5 Marks ] #
#################################################

def val(alien_num, digits):
        val = 0
        for i in alien_num:
            val = val*len(digits) + digits[i]
        return val

def max_ET_number(ET_numbers, mapping):
    max_index = 0
    digits = {}
    count = 0
    for num in mapping:
        digits[num] = count
        count += 1
    # we are going to track the max ET number via its index
    index = 0
    for i in ET_numbers:
        if val(ET_numbers[max_index], digits) < val(i, digits):
            max_index = index
        index += 1
    return ET_numbers[max_index]  

def test1b():
    print("=====Test 1b=====")
    # checking for normal decimal
    print(max_ET_number(('1','2','3','4','5'), ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for swapped digits
    print(max_ET_number(('12','34','42','58'), ('0','1','8','3','5','4','6','7','2','9')) == '42')
    print(max_ET_number(('19','20','21','22','23'), ('0','2','1','3','4','5','6','7','8','9')) == '19')
    # different bases
    print(max_ET_number(('14','15'),('0','1','2','3','5','4'))=='14')
    print(max_ET_number(('707','700','770'),('0','7'))=='770')
    print(max_ET_number(('0', '4', '40', '44', '400', '404', '440', '444', '4000', '4004', '4040'),('0','4'))=='4040')
    print(max_ET_number(('317','311','713','413'),('7','1','3','4'))=='413')
    print(max_ET_number(('aba', 'abc', 'ca', 'cb'), ('a', 'b', 'c')) == 'cb')

#test1b()

############################
# Question 2: Tesla stocks #
############################

import csv
import datetime

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

######################################################
# Question 2a: Retrieving tweets by date [ 3 Marks ] #
######################################################
def get_tweet_by_date(date):
    res = []
    file = filter(lambda x: datetime.datetime.strptime(x[-1], "%m/%d/%Y" ) == datetime.datetime.strptime(date, "%m/%d/%Y" ), read_csv("tweets.csv")[1:])
    for row in file: res.append(row[2])
    return tuple(res)

def test2a():
    print("=====Test 2a=====")
    print(get_tweet_by_date('12/21/2019') == ('Great show  https://t.co/12rguHHpgz', 'Holiday gift ideas https://t.co/uBBofvkYAI'))
    print(get_tweet_by_date('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness'))
    print(get_tweet_by_date('12/12/2001') == ())
    print(get_tweet_by_date('5/21/2021') == ()) 

#test2a()

#############################################################
# Question 2b: Effect of tweets on stock prices [ 3 Marks ] #
#############################################################
def tweet_effect(date):
    tweets = get_tweet_by_date(date)
    if not tweets: return None
    stocks = []
    currdate = datetime.datetime.strptime(date, "%m/%d/%Y")
    fivedays = datetime.datetime.strptime(date, "%m/%d/%Y") + datetime.timedelta(days = 5)
    file = filter(lambda x: currdate <= datetime.datetime.strptime(x[0], "%m/%d/%Y") <= fivedays, read_csv("TSLA.csv")[1:])
    for row in file:
        stocks.append(float(row[1]))
    return (*tweets, stocks)
        

    
def test2b():
    print("=====Test 2b=====")
    print(tweet_effect('5/8/2013') == ("Just want to say thanks to customers & investors that took a chance on Tesla through the long, dark night. We wouldn't be here without you.", [55.790001, 69.400002, 76.760002, 87.800003]))
    print(tweet_effect('3/23/2017') == None)
    print(tweet_effect('7/14/2019') == ('To Infinity and Beyond! https://t.co/dgysTBqWfV', [253.5, 252.380005, 254.860001, 253.539993, 258.179993]))

#test2b()

##########################################
# Question 2c: Money tweets [ 4 Marks ]  #
##########################################

def money_tweets(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    file = tuple(filter(lambda x: start_date <= datetime.datetime.strptime(x[0], "%m/%d/%Y") <= end_date, read_csv("TSLA.csv")[1:]))
    date_price = {}
    for row in file:
        date, price = row[0], float(row[1])
        date_price[date] = price
    fluc = {}
    for date in date_price:
        x = tweet_effect(date)
        if x:
            fluc[date] = x[-1]
    for date, val in fluc.items():
        fluc[date] = max(val) - min(val)
    return fluc
    highest = max(fluc.items(), key = lambda x: x[1])
    return(get_tweet_by_date(highest[0]), highest[1])

def test2c():
    print("=====Test 2c=====")
    print(money_tweets('5/12/2020', '5/21/2020') == (('Ice cream sundae in a martini glass https://t.co/zAVFlOsYkM', 'Super exciting day coming up! https://t.co/7ZdFsJE9zR', 'https://t.co/lQWpSwtRj7'), 22.669983000000002))
    print(money_tweets('4/29/2020', '5/1/2020') == (('FREE AMERICA NOW', 'Give people their freedom back! https://t.co/iG8OYGaVZ0', 'Bravo Texas! https://t.co/cVkDewRqGv'), 99.19000299999993))

#test2c()

############################################
# Question 3: TOY TRAIN                    #
############################################

class carriage:
    def __init__(self, x, y):
        self.start = (x, y)
        self.x = x
        self.y = y
        self.attached_to = None
        self.attached_by = None
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_pos(self):
        return (self.get_x(), self.get_y())
    def attach(self, car):
        if car.attached_by or self.attached_to: return "Can't attach."
        elif ((self.get_x() == car.get_x() and abs(self.get_y() - car.get_y()) == 1) or\
              (self.get_y() == car.get_y() and abs(self.get_x() - car.get_x()) == 1)):
            self.attached_to = car
            car.attached_by = self
            return "Attached."
        return "Can't attach."

class engine (carriage):
    def __init__(self, x, y):
        super().__init__(x, y)

    def allcars(self):
        res = []
        pullingon = self.attached_to
        while pullingon:
            res.append(pullingon)
            pullingon = pullingon.attached_to
        return res
    
    def move(self, track):
        directions = {"u": (0, 1), "d": (0, -1), "l": (-1, 0), "r": (1, 0)}
        for direction in track:
            subcars = (self.allcars())
            curr_points = map(lambda x: (x.get_x(), x.get_y()), subcars)
            movement = directions[direction]
            new_x = self.x + movement[0]
            new_y = self.y + movement[1]
            if (new_x, new_y) in curr_points: return "Collision!"
            subcars.insert(0, self)
            for i in range(1, len(subcars)):
                car = subcars[-i]
                to_follow = subcars[-i-1]
                car.x, car.y = to_follow.x, to_follow.y
            self.x, self.y = new_x, new_y
        return
                    

c0 = carriage(1,0)
c1 = carriage(1,1)
c2 = carriage(1,2)
c3 = carriage(2,2)
c4 = carriage(3,4)
e  = engine(2,3)

# Checking for get_x and get_y functions
print(c1.get_x() == 1)
print(c3.get_y() == 2)
# Checking for get_pos function
print(c0.get_pos() == (1,0))

# Attaching carraiges together to build the train
print(e.attach(c3) == "Attached.")
print(c3.attach(c2) == "Attached.")
print(c2.attach(c1) == "Attached.")

# c1 and c4 are not adjacent
print(c1.attach(c4) == "Can't attach.")

print(c1.attach(c0) == "Attached.")
print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 3), (2, 2), (1, 2), (1, 1), (1, 0)))
print(e.move('uuu') == None)
print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 6), (2, 5), (2, 4), (2, 3), (2, 2)))
print(e.move('r') == None)
print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 6), (2, 6), (2, 5), (2, 4), (2, 3)))


def test3():
    print("=====Test 3=====")
    c0 = carriage(1,0)
    c1 = carriage(1,1)
    c2 = carriage(1,2)
    c3 = carriage(2,2)
    c4 = carriage(3,4)
    e  = engine(2,3)

    # Checking for get_x and get_y functions
    print(c1.get_x() == 1)
    print(c3.get_y() == 2)
    # Checking for get_pos function
    print(c0.get_pos() == (1,0))

    # Attaching carraiges together to build the train
    print(e.attach(c3) == "Attached.")
    print(c3.attach(c2) == "Attached.")
    print(c2.attach(c1) == "Attached.")

    # c1 and c4 are not adjacent
    print(c1.attach(c4) == "Can't attach.")
    
    print(c1.attach(c0) == "Attached.")

    # Checking for movement
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 3), (2, 2), (1, 2), (1, 1), (1, 0)))
    print(e.move('uuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 6), (2, 5), (2, 4), (2, 3), (2, 2)))
    print(e.move('r') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 6), (2, 6), (2, 5), (2, 4), (2, 3)))
    print(e.move('uuuuuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 12), (3, 11), (3, 10), (3, 9), (3, 8)))
    print(e.move('rdll') == "Collision!")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    print(e.move('ldrr') == "Collision!")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    print(e.move('d') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 10), (4, 11), (4, 12), (3, 12), (3, 11)))

#test3()
