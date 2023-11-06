#******************************************************
#*
#*  CS1010S Re-Practical Exam
#*  AY2016/2017, Semester 2
#*  Name: Ricco Lim Jin Yu A0269596A
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

"""
--- 2 hours (120 minutes) left ---
Start 2218
Pause 2242
(24 minutes used)

--- 1 hour 36 minutes (96 minutes) left ---
Start 1242
Pause 1247
(5 minutes used)

--- 1 hour 31 minutes (91 minutes) left ---
Start 1408
End   1523
(1 hour 14 minutes (74 minutes) used)

--- 14 minutes left ---
"""

#------------#
# Question 1 #
#------------#

def check_digit(digits, table):
    checksum = 0
    for num in digits:
        if not num.isdigit():
            continue
        checksum += int(num)
    return table[checksum%len(table)]
        

nus_matric = {
    0: 'Y',
    1: 'X',
    2: 'W',
    3: 'U',
    4: 'R',
    5: 'N',
    6: 'M',
    7: 'L',
    8: 'J',
    9: 'H',
    10: 'E',
    11: 'A',
    12: 'B'
}
# Uncomment to test
##print(check_digit("0113093", nus_matric))
##print(check_digit("0129969", nus_matric))


def weighted_check_digit(digits, table, weights):
    multiplier = tuple(weights)
    checksum = 0
    for i in range(len(digits)):
        digit = digits[i]
        if not digit.isdigit(): continue
        checksum += int(digit) * int(multiplier[i])
    return table[checksum%len(table)]

sg_nric = dict(enumerate("JZIHGFEDCBA"))
sg_weights = "2765432"

# Uncomment to test
##print(weighted_check_digit("9702743", sg_nric, sg_weights))
##print(weighted_check_digit("9875133", sg_nric, sg_weights))


#------------#
# Question 2 #
#------------#

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


def oversub_avg(fname, year):
    file = filter(lambda x: x[0] == year, read_csv(fname))
    res = {}
    for row in file:
        year, month, bidding, vclass, quota, success, received, prem = row
        rate = int(received) / int(success)
        if vclass not in res: res[vclass] = {}
        res[vclass]["Total"] = res[vclass].get("Total", 0) + rate
        res[vclass]["Count"] = res[vclass].get("Count", 0) + 1
    for vclass, val in res.items():
        ave = round(val['Total'] / val['Count'], 3)
        res[vclass] = ave
    return res
        
    
        


# Uncomment to test
##print(oversub_avg("coe.csv", "2013"))
##print(oversub_avg("coe.csv", "2015"))


def most_oversub(fname, year):
    file = tuple(filter(lambda x: x[0] == year, read_csv(fname)))
    res = {}
    current_bidding_no = file[0][2]
    current_bids = []
    for row in file:
        year, month, bidding, vclass, quota, success, received, prem = row
        if vclass not in res: res[vclass] = 0
        rate = int(received) / int(success)
        if bidding == current_bidding_no:
            current_bids.append((vclass, rate))
        else:
            highest = max(current_bids, key = lambda x: x[1])[0]
            res[highest] += 1
            
            current_bidding_no = bidding
            current_bids = [(vclass, rate)]
    highest = max(current_bids, key = lambda x: x[1])[0]
    res[highest] += 1
    return res

# Uncomment to test
##print(most_oversub("coe.csv", "2013"))     
##print(most_oversub("coe.csv", "2015")) 



#------------#
# Question 3 #
#------------#

class Monster:
    def __init__(self, name, scariness_value):
        self.name = name
        self.scareval = scariness_value
        self.energy = 0
        self.door = None
    def get_name(self):
        return self.name
    def get_energy(self):
        return self.energy
    def get_location(self):
        if not self.door:
            return f"{self.get_name()} is on the Scream Floor"
        return f"{self.get_name()} is in {self.door.name}"
    def enter(self, door):
        if self.door == door:
            return f"{self.get_name()} has already entered {door.name}"
        elif self.door:
            return f"{self.get_name()} is currently in {self.door.name}"
        self.door = door
        door.monsters.append(self)
        return f"{self.get_name()} enters {door.name}"
    def scare(self):
        if not self.door:
            return f"{self.get_name()} has not entered any door"
        curr_door = self.door
        all_monsters = curr_door.monsters.copy()
        totaleffectivescariness = 0

        for monster in all_monsters:
            totaleffectivescariness += monster.scareval / curr_door.prev.get(monster, 1)
        
        energy = totaleffectivescariness - curr_door.braveval
        curr_door.braveval += len(all_monsters)
        monsternames = curr_door.get_monsters()
        curr_door.monsters.clear()

        
        for monster in all_monsters:
            monster.door = None
            curr_door.prev[monster] = curr_door.prev.get(monster, 1) + 1
        if energy <= 0:
            return f"{monsternames} failed to obtain energy from {curr_door.name}"
        indiv_energy = energy/len(all_monsters)
        for monster in all_monsters: monster.energy += indiv_energy
        return f"{monsternames} got {energy} energy from {curr_door.name}"        
class Door:
    def __init__(self, name, bravery_value):
        self.name = name
        self.braveval = bravery_value
        self.monsters = []
        self.prev = {}
        self.scarecount = 0
    def get_bravery(self):
        return self.braveval
    def get_monsters(self):
        return ", ".join(sorted(list(map(lambda x: x.get_name(), self.monsters))))
    
sully = Monster("Sully", 12)
mike = Monster("Mike", 1)
randall = Monster("Randall", 8)

mary = Door("Mary's Room", 1)
ted = Door("Ted's Room", 1)
boo = Door("Boo's Room", 21)





## helper function. Do NOT modify. No need to paste on Coursemology
def leaderboard(*monsters):
    return "\n".join("{}: {}".format(m.get_name(),
                                     round(m.get_energy(), 2)) for m in
                     sorted(monsters, key=lambda x:float(x.get_energy()), reverse=True))



# Sample run test case
def test_q3():
    sully = Monster("Sully", 12)
    mike = Monster("Mike", 1)
    randall = Monster("Randall", 8)

    mary = Door("Mary's Room", 1)
    ted = Door("Ted's Room", 1)
    boo = Door("Boo's Room", 21)
        
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 0
Mike: 0
Randall: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=sully.get_energy(); print(_ == 0, '\tsully.get_energy():\t', _)
    _=sully.get_location(); print(_ == "Sully is on the Scream Floor", '\tsully.get_location():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.get_location(); print(_ == "Sully is in Mary's Room", '\tsully.get_location():\t', _)
    _=mary.get_monsters(); print(_ == "Sully", '\tmary.get_monsters():\t', _)
    _=sully.scare(); print(_ == "Sully got 11.0 energy from Mary's Room", '\tsully.scare():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 11.0
Mike: 0
Randall: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=mary.get_bravery(); print(_ == 2, '\tmary.get_bravery():\t', _)
    _=sully.get_location(); print(_ == "Sully is on the Scream Floor", '\tsully.get_location():\t', _)
    _=randall.scare(); print(_ == "Randall has not entered any door", '\trandall.scare():\t', _)
    _=randall.enter(mary); print(_ == "Randall enters Mary's Room", '\trandall.enter(mary):\t', _)
    _=randall.scare(); print(_ == "Randall got 6.0 energy from Mary's Room", '\trandall.scare():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.enter(ted); print(_ == "Sully is currently in Mary's Room", '\tsully.enter(ted):\t', _)
    _=mary.get_bravery(); print(_ == 3, '\tmary.get_bravery():\t', _)
    _=sully.scare(); print(_ == "Sully got 3.0 energy from Mary's Room", '\tsully.scare():\t', _)
    _=mary.get_bravery(); print(_ == 4, '\tmary.get_bravery():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.scare(); print(_ == "Sully failed to obtain energy from Mary's Room", '\tsully.scare():\t', _)
    _=randall.enter(mary); print(_ == "Randall enters Mary's Room", '\trandall.enter(mary):\t', _)
    _=randall.scare(); print(_ == "Randall failed to obtain energy from Mary's Room", '\trandall.scare():\t', _)
    _=mary.get_bravery(); print(_ == 6, '\tmary.get_bravery():\t', _)
    _=randall.get_location(); print(_ == "Randall is on the Scream Floor", '\trandall.get_location():\t', _)
    _=sully.enter(ted); print(_ == "Sully enters Ted's Room", '\tsully.enter(ted):\t', _)
    _=mike.enter(ted); print(_ == "Mike enters Ted's Room", '\tmike.enter(ted):\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 14.0
Randall: 6.0
Mike: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=ted.get_monsters(); print(_ == "Mike, Sully", '\tted.get_monsters():\t', _)
    _=ted.get_bravery(); print(_ == 1, '\tted.get_bravery():\t', _)
    _=mike.scare(); print(_ == "Mike, Sully got 12.0 energy from Ted's Room", '\tmike.scare():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 20.0
Mike: 6.0
Randall: 6.0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=ted.get_bravery(); print(_ == 3, '\tted.get_bravery():\t', _)
    _=sully.enter(ted); print(_ == "Sully enters Ted's Room", '\tsully.enter(ted):\t', _)
    _=mike.enter(ted); print(_ == "Mike enters Ted's Room", '\tmike.enter(ted):\t', _)
    _=randall.enter(ted); print(_ == "Randall enters Ted's Room", '\trandall.enter(ted):\t', _)
    _=randall.scare(); print(_ == "Mike, Randall, Sully got 11.5 energy from Ted's Room", '\trandall.scare():\t', _)
    _=ted.get_bravery(); print(_ == 6, '\tted.get_bravery():\t', _)
    _=sully.enter(boo); print(_ == "Sully enters Boo's Room", '\tsully.enter(boo):\t', _)
    _=mike.enter(boo); print(_ == "Mike enters Boo's Room", '\tmike.enter(boo):\t', _)
    _=randall.enter(boo); print(_ == "Randall enters Boo's Room", '\trandall.enter(boo):\t', _)
    _=sully.scare(); print(_ == "Mike, Randall, Sully failed to obtain energy from Boo's Room", '\tsully.scare():\t', _)
    _=mike.get_energy(); print(_ == 9.833333333333334, '\tmike.get_energy():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 23.83
Mike: 9.83
Randall: 9.83""", '\tleaderboard(sully, mike, randall):\t', _)

# Uncomment to test
test_q3()

