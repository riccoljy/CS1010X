##############
# Question 1 #
##############

"""
Timestamps
Start 0910
Pause 0920
(10 minutes(

Resume 1048
Stop 1059
(11 minutes)

Resume 1455
Stop 1510
(15 minutes)

Resume 0907
Pause 0918
(11 minutes)

Resume 0904
Pause 0919
(15 minutes)

--Left 58 mins--
Resume 1032
Pause 1034
(2 minutes)

--Left 56 minutes--
Resume 1538
End 1545
(7 minutes)

Total used/left: 1 h 11 minutes /49 minutes
"""
def l33tify(string, code):
    res = ""
    for letter in string:
        res += code.get(letter, letter)
    return res


l33t_dict = {
    'a': '4',
    'b': '8',
    'c': '(',
    'e': '3',
    'g': '[',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'x': '%',
    'z': '2',
    }

# Uncomment to test
##print(l33tify("pheer my leet skills", l33t_dict))
##print(l33tify("python is cool", l33t_dict))


def advance_l33tify(string, code):
    temp = code.copy()
    string = string.lower()
    res = ""
    for letter in string:
        if letter not in code:
            res += letter
            continue
        replacement = temp[letter][0]
        temp[letter] = temp[letter][1:]+temp[letter][:1]
        res += replacement
    return res


adv_l33t_dict = {
    'a': ['4', '/-\\', '/_\\', '@', '/\\'],
    'b': ['8', '|3', '13', '|}', '|:', '|8', '18', '6', '|B'],
    'c': ['<', '{', '[', '('],
    'd': ['|)', '|}', '|]'],
    'e': ['3'],
    'f': ['|=', 'ph', '|#', '|"'],
    'g': ['[', '-', '[+', '6'],
    'h': ['|-|', '[-]', '{-}', '|=|', '[=]', '{=}'],
    'i': ['1', '|'],
    'j': ['_|', '_/', '_7', '_)'],
    'k': ['|<', '1<'],
    'l': ['|_', '|', '1'],
    'm': ['|\\/|', '^^', '/\\/\\'],
    'n': ['|\\|', '/\\/', '/V', '][\\\\]['],
    'o': ['0', '()', '[]', '{}'],
    'p': ['|o', '|O', '|>', '|*', '|°', '|D', '/o'],
    'q': ['O_', '9', '(', ')', ''],
    'r': ['|2', '12', '.-', '|^'],
    's': ['5', '$', '§'],
    't': ['7', '+', '7`', "'|'"],
    'u': ['|_|', '\\_\\', '/_/', '\\_/', '(_)'],
    'v': ['\\/'],
    'w': ['\\/\\/', '(/\\)', '\\^/', '|/\\|'],
    'x': ['%', '*', '><', '}{', ')('],
    'y': ['`/', '¥'],
    'z': ['2', '7_', '>_']
    }

# Uncomment to test
##print(advance_l33tify("Bow b4 me 4 I am root!!!", adv_l33t_dict))
##print(advance_l33tify("Mississippi", adv_l33t_dict))


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

def yearly_average(fname, year):
    file = filter(lambda x: x[0] == year, read_csv(fname))
    res = {}
    for row in file:
        year, month, telco, coverage_month = row
        if telco not in res:
            res[telco] = {"Total coverage": 0, "Count": 0}
        res[telco]["Total coverage"] += float(coverage_month)
        res[telco]["Count"] += 1
    for telco in res:
        telco_dict = res[telco]
        res[telco] = round(telco_dict["Total coverage"] / telco_dict["Count"], 4)
    return res
    
        


# Uncomment to test
##print(yearly_average("3g-coverage.csv", "2015"))
##print(yearly_average("3g-coverage.csv", "2013"))

def best_telco(fname, year):
    file = filter(lambda x: x[0] == year, read_csv(fname))
    temp = {}
    for row in file:
        year, month, telco, coverage_month = row
        if month not in temp:
            temp[month] = {}
        temp[month][telco] = float(coverage_month)
    res = {}
    for key, val in temp.items():
        telcos = val.items()
        
        for telco in telcos:
            if telco[0] not in res: res[telco[0]] = 0

        highest = max(telcos, key = lambda x: x[1])[0]
        res[highest] += 1
    return res

# Uncomment to test
##print(best_telco("3g-coverage.csv", "2015"))
##print(best_telco("3g-coverage.csv", "2013"))



##############
# Question 3 #
##############

class Villain:
    def __init__(self, name):
        self.name = name
        self.evil = 0
        self.gadgets = []
        self.proficiency = {}
    def get_evilness(self):
        return self.evil
    def gadgets_owned(self):
        return tuple(map(lambda x: x.name, self.gadgets))
    def get_proficiency(self, gadget):
        if gadget in self.proficiency:
            return f"{self.name}'s proficiency with {gadget.name} is {self.proficiency[gadget]}"
        self.proficiency[gadget] = 0
        return f"{self.name} is not proficient with {gadget.name}"
    def do_evil(self, action, gadget):
        if gadget not in self.gadgets:
            return f"{self.name} does not have {gadget.name}"
        self.evil += gadget.val + self.proficiency.get(gadget, 0)
        gadget.val -= 1
        if gadget.val < 0: gadget.val = 0
        self.proficiency[gadget] = self.proficiency.get(gadget, 0) + 1
        return f"{self.name} {action} with {gadget.name}"
    def steals(self, gadget):
        if gadget in self.gadgets:
            return f"{self.name} already has {gadget.name}"
        self.gadgets.append(gadget)
        gadget.val = gadget.orival
        prev_owner = gadget.owner
        gadget.owner = self
        if prev_owner:
            prev_owner.evil //= 2
            prev_owner.gadgets.remove(gadget)
            return f"{self.name} steals {gadget.name} from {prev_owner.name}"
        return f"{self.name} steals {gadget.name}"
    def envy(self, other):
        if isinstance(other, Gadget):
            if not other.owner:
                return f"{self.name} envies {other.name}"
            elif other.owner == self:
                return f"{self.name} already has {other.name}"   
            return f"{self.name} envies {other.owner.name}'s {other.name}"
        elif isinstance(other, Villain):
            if other == self:
                return f"{self.name} cannot envy himself"  
            elif other.evil == self.evil:
                return f"Nobody is envious"
            elif self.evil > other.evil:
                higher = self
                lower = other
            else:
                higher = other
                lower = self
            return f"{lower.name} envies {higher.name}"              
        

class Gadget:
    def __init__(self, name, awesomeness_value):
        self.name = name
        self.orival = awesomeness_value
        self.val = self.orival
        self.owner = None
    def get_description(self):
        return f"{self.name} has level {self.val} awesomeness"
    def owned_by(self):
        if self.owner: return f"{self.name} belongs to {self.owner.name}"
        return f"{self.name} is unowned"


gru = Villain("Gru")
vector = Villain("Vector")
freeze_ray = Gadget("Freeze Ray", 5)
lava_gun = Gadget("Lava Lamp Gun", 3)
print(gru.get_evilness())
print(gru.gadgets_owned())
print(freeze_ray.get_description())
print(freeze_ray.owned_by())
print(gru.steals(freeze_ray))
print(gru.gadgets_owned())
print(freeze_ray.owned_by())
print(gru.get_proficiency(freeze_ray))
print(gru.do_evil("robs a bank", freeze_ray))
print(gru.get_evilness())
print(gru.get_proficiency(freeze_ray))
print(freeze_ray.get_description())
print(gru.do_evil("steals candy", freeze_ray))
print(gru.get_proficiency(freeze_ray))
print(gru.get_evilness())
print(freeze_ray.get_description())
print(gru.envy(freeze_ray))
print(vector.envy(freeze_ray))
print(gru.envy(vector))
print(vector.steals(freeze_ray))
print(gru.get_evilness())
print(freeze_ray.get_description())
print(freeze_ray.owned_by())
print(gru.gadgets_owned())






# Sample run test case
def test_q3():
    gru = Villain("Gru")
    vector = Villain("Vector")
    freeze_ray = Gadget("Freeze Ray", 5)
    lava_gun = Gadget("Lava Lamp Gun", 3)
    
    _=gru.get_evilness(); print(_ == 0, '\tgru.get_evilness():\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == (), '\tgru.gadgets_owned():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 5 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray is unowned", '\tfreeze_ray.owned_by():\t', _)    
    _=gru.steals(freeze_ray); print(_ == "Gru steals Freeze Ray", '\tgru.steals(freeze_ray):\t', _)    
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == ('Freeze Ray',), '\tgru.gadgets_owned():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray belongs to Gru", '\tfreeze_ray.owned_by():\t', _)    
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru is not proficient with Freeze Ray", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=gru.do_evil("robs a bank", freeze_ray); print(_ == "Gru robs a bank with Freeze Ray", '\tgru.do_evil("robs a bank", freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 5, '\tgru.get_evilness():\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru's proficiency with Freeze Ray is 1", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 4 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=gru.do_evil("steals candy", freeze_ray); print(_ == "Gru steals candy with Freeze Ray", '\tgru.do_evil("steals candy", freeze_ray):\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru's proficiency with Freeze Ray is 2", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 10, '\tgru.get_evilness():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 3 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=gru.envy(freeze_ray); print(_ == "Gru already has Freeze Ray", '\tgru.envy(freeze_ray):\t', _)
    _=vector.envy(freeze_ray); print(_ == "Vector envies Gru's Freeze Ray", '\tvector.envy(freeze_ray):\t', _)
    _=gru.envy(vector); print(_ == "Vector envies Gru", '\tgru.envy(vector):\t', _)
    _=vector.steals(freeze_ray); print(_ == "Vector steals Freeze Ray from Gru", '\tvector.steals(freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 5, '\tgru.get_evilness():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 5 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray belongs to Vector", '\tfreeze_ray.owned_by():\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == (), '\tgru.gadgets_owned():\t', _)
    _=vector.do_evil("freezes Miami", freeze_ray); print(_ == "Vector freezes Miami with Freeze Ray", '\tvector.do_evil("freezes Miami", freeze_ray):\t', _)
    _=vector.get_evilness(); print(_ == 5, '\tvector.get_evilness():\t', _)
    _=gru.envy(vector); print(_ == "Nobody is envious", '\tgru.envy(vector):\t', _)
    _=gru.envy(lava_gun); print(_ == "Gru envies Lava Lamp Gun", '\tgru.envy(lava_gun):\t', _)
    _=gru.do_evil("steals Freeze Ray", lava_gun); print(_ == "Gru does not have Lava Lamp Gun", '\tgru.do_evil("steals Freeze Ray", lava_gun):\t', _)
    _=gru.envy(lava_gun); print(_ == "Gru envies Lava Lamp Gun", '\tgru.envy(lava_gun):\t', _)
    _=gru.steals(lava_gun); print(_ == "Gru steals Lava Lamp Gun", '\tgru.steals(lava_gun):\t', _)
    _=gru.do_evil("steals the Queen\'s crown", lava_gun); print(_ == "Gru steals the Queen's crown with Lava Lamp Gun", '\tgru.do_evil("steals the Queen\'s crown", lava_gun):\t', _)
    _=gru.get_evilness(); print(_ == 8, '\tgru.get_evilness():\t', _)
    _=gru.steals(freeze_ray); print(_ == "Gru steals Freeze Ray from Vector", '\tgru.steals(freeze_ray):\t', _)
    _=vector.get_evilness(); print(_ == 2, '\tvector.get_evilness():\t', _)
    _=gru.get_evilness(); print(_ == 8, '\tgru.get_evilness():\t', _)
    _=gru.envy(vector); print(_ == "Vector envies Gru", '\tgru.envy(vector):\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == ('Freeze Ray', 'Lava Lamp Gun'), '\tgru.gadgets_owned():\t', _)
    _=gru.do_evil("freezes Vector", freeze_ray); print(_ == "Gru freezes Vector with Freeze Ray", '\tgru.do_evil("freezes Vector", freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 15, '\tgru.get_evilness():\t', _)

# Uncomment to test
test_q3()
