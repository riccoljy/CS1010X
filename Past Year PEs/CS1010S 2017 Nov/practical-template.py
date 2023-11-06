###
### Question 1
###

"""
--- 2 hours (120 minutes) ---
Start 2323
Pause 2334
(11 minutes)

-- 1 hour 49 minutes (109 minutes) ---
Resume 1118
Pause


"""

# Q1A
def brake_at(dest, speed):
    while speed:
        speed //= 2
        dest -= speed
    return dest


# Q1B
def braking_points(curr, dest, speed):
    t = 0
    r = []
    while (speed):
        print(t, curr, speed) # for visualization
        # can we maintain the current speed?
        if curr + speed > brake_at(dest, speed):
            # no, we have to reduce
            speed //= 2
            r.append(curr)
        curr += speed
        t += 1
    print(t, curr, speed) # for visualization
    if curr > dest:
        return [] # oops we have exceeded our destination
    else:
        return r

# Tests
def test_q1a():
    print(brake_at(89, 4))
    print(brake_at(89, 10))
    print(brake_at(89, 20))


def test_q1b():
    print(braking_points(44, 89, 10))
    print(braking_points(71, 89, 20))
    print(braking_points(71, 89, 22))


# Uncomment to test
##test_q1a()
##test_q1b()

    

###
### Question 2
###

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


### Your answer here.
# Q2A
def monthly_avg(fname, currency, year, component):
    file = read_csv(fname)
    comp_index = file[0].index(component)
    file = filter(lambda x: x[0] == str(year) and currency == x[3], file)
    res = {}
    for row in file:
        month = row[1]
        comp = float(row[comp_index])
        if month not in res:
            res[month] = []
        res[month].append(comp)
    for month in res:
        res[month] = round(sum(res[month])/len(res[month]), 4)
    return res
    


# Q2B
def highest_gain(fname, year, component):
    file = read_csv(fname)
    comp_index = file[0].index(component)
    file = filter(lambda x: x[0] == str(year), file)
    temp = {}
    for row in file:
        month = row[1]
        curr = row[3]
        comp = float(row[comp_index])
        if month not in temp:
            temp[month] = {}
        if curr not in temp[month]:
            temp[month][curr] = []
        temp[month][curr].append(comp)
    for month, curr_dict in temp.items():
        for curr, lst in curr_dict.items():
            low = min(lst)
            high = max(lst)
            gain = round((high/low-1)*100, 2)
            temp[month][curr] = gain
    for month, curr_dict in temp.items():
        temp[month] = max(curr_dict.items(), key = lambda x: x[1])
    return temp
            

        


## BONUS Q2C ##
def max_single_sell(fname, currency, component):
    file = read_csv(fname)
    comp_index = file[0].index(component)
    file = filter(lambda x: x[3] == currency, file)
    valdict = {}
    for row in file:
        year, month, day = row[:3]
        date = "-".join((year, month, day))
        val = float(row[comp_index])
        valdict[date] = val
    valdict = sorted(list(valdict.items()), key = lambda x: -x[1])
    res = []
    monthdict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,\
                 "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    while True:
        sell_y, sell_m, sell_d = valdict[0][0].split("-")
        buy_y, buy_m, buy_d = valdict[-1][0].split("-")
        buy_y, sell_y, buy_d, sell_d = int(buy_y), int(sell_y), int(buy_d), int(sell_d)
        sell_m, buy_m = monthdict[sell_m], monthdict[buy_m]
        sell_val, buy_val = float(valdict[0][1]), float(valdict[-1][1])
        if ((sell_y < buy_y) or\
           (sell_y == buy_y and sell_m < buy_m) or\
           (sell_y == buy_y and sell_m == buy_m and sell_d < buy_d)):
            diff1 = buy_val - float(valdict[1][1])
            diff2 = float(valdict[-2][1]) - sell_val
            if diff1>diff2: valdict.pop()
            else: valdict.pop(0)
        else:
            return (valdict[-1][0], valdict[0][0], valdict[0][1] - valdict[-1][1])
# Tests
def test_q2a():
    print(monthly_avg('crypto.csv', 'ETH', 2017, 'Close') == \
        {'Nov': 296.4443, 'Oct': 306.2474, 'Sep': 293.0473, 
         'Aug': 301.6094, 'Jul': 224.1239, 'Jun': 313.7343, 
         'May': 125.7494, 'Apr': 50.3367, 'Mar': 34.7916, 
         'Feb': 12.3711, 'Jan': 10.2013})

    print(monthly_avg('crypto.csv', 'BTC', 2013, 'High') == \
        {'Dec': 856.4419, 'Nov': 569.307, 'Oct': 161.9442, 
         'Sep': 134.164, 'Aug': 116.0023, 'Jul': 93.869, 
         'Jun': 111.3007, 'May': 123.949, 'Apr': 143.4667})


def test_q2b():
    print(highest_gain('crypto.csv', 2017, "Volume") == \
        {'Nov': ('XPR', 695.17), 'Oct': ('XPR', 3485.19), 
         'Sep': ('LTC', 1792.14), 'Aug': ('XPR', 5524.07), 
         'Jul': ('LTC', 1354.52), 'Jun': ('XPR', 1071.13), 
         'May': ('ETH', 2302.35), 'Apr': ('XPR', 4537.85), 
         'Mar': ('XPR', 7003.02), 'Feb': ('ETH', 1049.67), 
         'Jan': ('XPR', 1975.93)})
 
    print(highest_gain('crypto.csv', 2013, "Market Cap") == \
        {'Dec': ('XPR', 272.37), 'Nov': ('LTC', 1862.94), 
         'Oct': ('BTC', 88.94), 'Sep': ('XPR', 171.23), 
         'Aug': ('XPR', 109.9), 'Jul': ('BTC', 59.08), 
         'Jun': ('LTC', 52.22), 'May': ('LTC', 48.27), 
         'Apr': ('BTC', 7.15)})


def test_q2c():
    print(max_single_sell('crypto.csv', 'ETH', 'Close'))
    print(max_single_sell('crypto.csv', 'BTC', 'Close'))
    print(max_single_sell('crypto.csv', 'DASH', 'Close'))


##test_q2a()
##test_q2b()
##test_q2c()




###
### Question 3
###

### Your answer here.
class Entity:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.master = None
    def get_name(self):
        return self.name
    def get_master(self):
        return self.master.name if self.master else None
    def get_damage(self):
        return self.damage
    def attack(self, other):
        if other == self:
            return f"{self.get_name()} cannot attack itself"
        elif other == self.master:
            return f"{self.get_name()} cannot attack its master"
        elif self.master and other in self.master.slaves:
            return f"{self.get_name()} cannot attack its master's slave"
        return f"{self.get_name()} deals {self.get_damage()} damage to {other.get_name()}"
class Overmind(Entity):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.slaves = []
    def get_damage(self):
        return sum(map(lambda x: x.get_damage(), self.slaves)) + self.damage
    def get_slaves(self):
        direct = set(map(lambda x: x.get_name(), self.slaves))
        sub = set()
        for slave in self.slaves:
            if isinstance(slave, Overmind):
                sub = sub.union(set(map(lambda x: x.get_name(), slave.slaves)))
        return tuple(sub.union(direct))
    def attack(self, other):
        if other in self.slaves:
            return f"{self.get_name()} cannot attack its slave"
        return super().attack(other)
    def mind_control(self, other):
        if other == self:
            return f"{self.get_name()} cannot mind-control itself"
        elif other in self.slaves or other.master in self.slaves:
            return f"{other.get_name()} is already a slave of {self.get_name()}"
        elif other == self.master:
            return f"{self.get_name()} cannot mind-control its master"
        elif other.master == self.master != None or\
             (other.master and self.master in other.master.slaves) or\
             (self.master and other.master in self.master.slaves):
            return f"{self.get_name()} and {other.get_name()} have the same master"
        old = other.master
        other.master = self
        self.slaves.append(other)
        if old:
            old.slaves.remove(other)
            return f"{self.get_name()} over-mind-controls {other.get_name()} from {old.get_name()}"
        return f"{self.get_name()} mind-controls {other.get_name()}"
    
demodog    = Entity('Demodog', 10)
demogorgon = Entity('Demogorgon', 50)
dartagnan  = Entity("D'artagnan", 20)
mindflayer = Overmind('Mindflayer', 25)
mindreader = Overmind('Mindreader', 5)
eleven = Overmind('Eleven', 5)
print(demodog.attack(demodog))
print(demodog.attack(demogorgon))
print(demodog.get_master())
print(mindreader.mind_control(demodog))
print(mindreader.mind_control(demogorgon))
print(mindreader.get_slaves())
print(demodog.get_master())
print(mindreader.attack(demodog))
print(demodog.attack(mindreader))
print(demodog.attack(demogorgon))
print(mindflayer.attack(eleven))
print(mindflayer.mind_control(mindreader))
print(mindflayer.attack(eleven))
print(mindflayer.mind_control(demodog))
print(mindreader.mind_control(mindflayer))
print(mindflayer.mind_control(dartagnan))
print(mindreader.mind_control(dartagnan))
print(mindflayer.get_slaves())
print(eleven.mind_control(mindreader))
print(eleven.get_slaves())
print(eleven.attack(mindflayer))

print(mindflayer.attack(eleven))


# Tests
def test_q3():
    demodog    = Entity('Demodog', 10)
    demogorgon = Entity('Demogorgon', 50)
    dartagnan  = Entity("D'artagnan", 20)
    mindflayer = Overmind('Mindflayer', 25)
    mindreader = Overmind('Mindreader', 5)
    eleven = Overmind('Eleven', 5)

    _=demodog.attack(demodog); print(_ == "Demodog cannot attack itself", '\tdemodog.attack(demodog):\t', _)
    _=demodog.attack(demogorgon); print(_ == "Demodog deals 10 damage to Demogorgon", '\tdemodog.attack(demogorgon):\t', _)
    _=demodog.get_master(); print(_ == None, '\tdemodog.get_master():\t', _)
    _=mindreader.mind_control(mindreader); print(_ == "Mindreader cannot mind-control itself", '\tmindreader.mind_control(mindreader):\t', _)
    _=mindreader.mind_control(demodog); print(_ == "Mindreader mind-controls Demodog", '\tmindreader.mind_control(demodog):\t', _)
    _=mindreader.mind_control(demogorgon); print(_ == "Mindreader mind-controls Demogorgon", '\tmindreader.mind_control(demogorgon):\t', _)
    _=mindreader.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon'), '\tmindreader.get_slaves():\t', _)
    _=demodog.get_master(); print(_ == "Mindreader", '\tdemodog.get_master():\t', _)
    _=mindreader.attack(demodog); print(_ == "Mindreader cannot attack its slave", '\tmindreader.attack(demodog):\t', _)
    _=demodog.attack(mindreader); print(_ == "Demodog cannot attack its master", '\tdemodog.attack(mindreader):\t', _)
    _=demodog.attack(demogorgon); print(_ == "Demodog cannot attack its master's slave", '\tdemodog.attack(demogorgon):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 25 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindflayer.mind_control(mindreader); print(_ == "Mindflayer mind-controls Mindreader", '\tmindflayer.mind_control(mindreader):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 90 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindflayer.mind_control(demodog); print(_ == "Demodog is already a slave of Mindflayer", '\tmindflayer.mind_control(demodog):\t', _)
    _=mindreader.mind_control(mindflayer); print(_ == "Mindreader cannot mind-control its master", '\tmindreader.mind_control(mindflayer):\t', _)
    _=mindflayer.mind_control(dartagnan); print(_ == "Mindflayer mind-controls D'artagnan", '\tmindflayer.mind_control(dartagnan):\t', _)
    _=mindreader.mind_control(dartagnan); print(_ == "Mindreader and D'artagnan have the same master", '\tmindreader.mind_control(dartagnan):\t', _)
    _=mindflayer.get_slaves(); print(tuple(sorted(_)) == ("D'artagnan", 'Demodog', 'Demogorgon', 'Mindreader'), '\tmindflayer.get_slaves():\t', _)
    _=eleven.mind_control(mindreader); print(_ == "Eleven over-mind-controls Mindreader from Mindflayer", '\televen.mind_control(mindreader):\t', _)
    _=eleven.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon', 'Mindreader'), '\televen.get_slaves():\t', _)
    _=eleven.attack(mindflayer); print(_ == "Eleven deals 70 damage to Mindflayer", '\televen.attack(mindflayer):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 45 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindreader.attack(mindflayer); print(_ == "Mindreader deals 65 damage to Mindflayer", '\tmindreader.attack(mindflayer):\t', _)
    _=eleven.mind_control(dartagnan); print(_ == "Eleven over-mind-controls D'artagnan from Mindflayer", '\televen.mind_control(dartagnan):\t', _)
    _=mindflayer.get_slaves(); print(tuple(sorted(_)) == (), '\tmindflayer.get_slaves():\t', _)
    _=mindreader.mind_control(mindflayer); print(_ == "Mindreader mind-controls Mindflayer", '\tmindreader.mind_control(mindflayer):\t', _)
    _=mindreader.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon', 'Mindflayer'), '\tmindreader.get_slaves():\t', _)
    _=eleven.get_slaves(); print(tuple(sorted(_)) == ("D'artagnan", 'Demodog', 'Demogorgon', 'Mindflayer', 'Mindreader'), '\televen.get_slaves():\t', _)
    _=mindflayer.mind_control(mindreader); print(_ == "Mindflayer cannot mind-control its master", '\tmindflayer.mind_control(mindreader):\t', _)
    _=mindflayer.mind_control(dartagnan); print(_ == "Mindflayer and D'artagnan have the same master", '\tmindflayer.mind_control(dartagnan):\t', _)
# Uncomment to test question 3
##test_q3()


