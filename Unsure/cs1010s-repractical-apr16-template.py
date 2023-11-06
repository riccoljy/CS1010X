from calendar import isleap
#******************************************************
#*
#*  CS1010S Re-Practical Exam
#*  AY2015/2016, Semester 2
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

###
### Question 1
###

### Your answer here.
def num_swaps(candies):
    if not candies: return 0
    highest = candies[0], candies.count(candies[0])
    for letter in candies[1:]:
        count = candies.count(letter)
        if count > highest[1]:
            highest = letter, count
    return len(candies) - highest[1]
        

def num_trades(candies, rules):
    count = 0
    for letter in candies:
        minicount = 0
        if letter == 'b': continue
        while letter != 'b':
            minicount += 1
            if minicount > len(rules):
                return float("inf")
            count += 1
            letter = rules[letter]
    return count


### test cases
def test1a():
    print(num_swaps("rbygo"))
    print(num_swaps("rrbbbg"))
    print(num_swaps("rrrbbbggy"))

def test1b():        
    print(num_trades('rrbbgg', {'r':'b', 'b':'y', 'y':'g', 'g':'o', 'o':'r'}))
    print(num_trades('rbbryy', {'r':'b', 'b':'r', 'y':'r'}))
    print(num_trades('rygop',
                     {'r':'b', 'b':'b', 'y':'b', 'g':'b', 'o':'b', 'p':'b'}))


def test_bonus():
    print(num_trades('rrbbgg', {'r':'b', 'b':'r', 'y':'g', 'g':'y'}))
    print(num_trades('rbbb', {'r':'y', 'b':'r', 'y':'g', 'g':'g'}))

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
def highest_rainfall(fname, start, stop):
    file = filter(lambda x: start <= int(x[0]) < stop, read_csv(fname)[1:])
    res = {}
    for row in file:
        year, month, total, highest, *_ = row
        if float(highest) >= res.get(year, (month, float(highest)))[1]:
            res[year] = (month, float(highest))
    return res


def rainy(fname, start, stop):
    file = filter(lambda x: start <= int(x[0]) < stop, read_csv(fname)[1:])
    temp = {}
    for row in file:
        year, num = int(row[0]), int(row[4])
        temp[year] = temp.get(year, 0) + num
    res = {}
    for year in temp:
        if isleap(year):
            res[year] = round(temp[year]/366*100, 2)
        else:
            res[year] = round(temp[year]/365*100, 2)
    return res
        
    

### test cases
def test2a():
    print(highest_rainfall('rainfall.csv', 2001, 2011))
    print(highest_rainfall('rainfall.csv', 1980, 1986))

def test2b():
    print(rainy('rainfall.csv', 1975, 1981))
    print(rainy('rainfall.csv', 2010, 2016))


###
### Question 3
###

### Your answer here.
class Sith:
    def __init__(self, name, *powers):
        self.name = "Darth " + name
        self.master_apprentice = [None, None]
        self.powers = []
        if powers:
            for power in powers:
                self.powers.append((power, 0))
        self.alive = True
    def get_name(self):
        return self.name
    def get_powers(self):
        return self.powers
    def get_master(self):
        return self.master_apprentice[0].get_name()
    def get_apprentice(self):
        return self.master_apprentice[1].get_name()
    def take_apprentice(self, apprentice):
        if not self.alive:
            return f"{self.get_name()} is already dead"
        elif not apprentice.alive:
            return f"{apprentice.get_name()} is already dead"
        elif any(self.master_apprentice) or any(apprentice.master_apprentice):
            return f"{self.get_name()} cannot take {apprentice.get_name()} as an apprentice"
        self.master_apprentice[1] = apprentice
        apprentice.master_apprentice[0] = self
        return f"{self.get_name()} takes {apprentice.get_name()} as an apprentice"
    def impart(self):
        if not self.alive:
            return f"{self.get_name()} is already dead"
        apprentice = self.master_apprentice[1]
        if not apprentice:
            return f"{self.get_name()} does not have an apprentice"
        for power, val in self.powers:
            if power not in map(lambda x: x[0], apprentice.powers):
                apprentice.powers.append((power, 0))
                return f"{self.get_name()} imparts {power} to {apprentice.get_name()}"
        return f"{self.get_name()} has nothing to impart to {apprentice.get_name()}"
    def train(self, power):
        if not self.alive:
            return f"{self.get_name()} is already dead"
        elif power not in map(lambda x: x[0], self.powers):
            return f"{self.get_name()} has does not know {power}"
        index = list(map(lambda x: x[0], self.powers)).index(power)
        old = self.powers[index]
        new = old[0], old[1]+1
        self.powers[index] = new
        return f"{self.get_name()} trains {new[0]} to level {new[1]}"
    def fight(self, opponent):
        if not self.alive:
            return f"{self.get_name()} is already dead"
        elif not opponent.alive:
            return f"{opponent.get_name()} is already dead"
        
        self_point, opp_point = 0, 0
        self_power, opp_power = self.powers.copy(), opponent.powers.copy()

        for i in range(len(self_power)):
            power, lvl = self_power[i]
            opp_power_name = list(map(lambda x: x[0], opp_power))
            if power not in opp_power_name:
                self_point += 1
                self_power[i] = ("Counted", None)
                continue
            index = opp_power_name.index(power)
            opplvl = opp_power[index][1]
            if lvl > opplvl: self_point += 1
            elif lvl < opplvl: opp_point += 1
            self_power[i] = ("Counted", None)
            opp_power[index] = ("Counted", None)

        for i in range(len(opp_power)):
            power, lvl = opp_power[i]
            if (power, lvl) == ("Counted", None): continue
            self_power_name = list(map(lambda x: x[0], self_power))
            if power not in self_power_name:
                opp_point += 1
                opp_power[i] = ("Counted", None)
                continue
            index = self_power_name.index(power)
            selflvl = self_power[index][1]
            if lvl > selflvl: opp_point += 1
            elif lvl < selflvl: self_point += 1
            self_power[i] = ("Counted", None)
            opp_power[index] = ("Counted", None)

##        print("")
##        print(f"{self.name} powers = {self_power}, {opponent.name} powers = {opp_power}")
##        print(f'{self.name} points = {self_point}, {opponent.name} points = {opp_point}')
        if self_point == opp_point:
            return f"{self.get_name()} and {opponent.get_name()} are equally matched"
        elif self_point > opp_point:
            opponent.alive = False
            for sith in opponent.master_apprentice:
                if isinstance(sith, Sith):
                    sith.master_apprentice = [None, None]
            opponent.master_apprentice = [None, None]
            
            return f"{self.get_name()} kills {opponent.get_name()} in battle"
        else:
            self.alive = False
            for sith in self.master_apprentice:
                if isinstance(sith, Sith):
                    sith.master_apprentice = [None, None]
            self.master_apprentice = [None, None]
            return f"{opponent.get_name()} kills {self.get_name()} in battle"

plagueis = Sith("Plagueis", "lightning", "choke") 
sidious = Sith("Sidious", "shadow")
maul = Sith("Maul")
tyranus = Sith("Tyranus")
vader = Sith("Vader", "hate")

print(plagueis.get_name())
print(plagueis.get_powers())
print(plagueis.train("choke"))
print(plagueis.train("lightning"))
print(plagueis.take_apprentice(sidious))
print(plagueis.get_apprentice())
print(sidious.get_master())
print(plagueis.impart())
print(sidious.train("lightning"))
print(sidious.train("choke"))
print(sidious.get_powers())
print(sidious.take_apprentice(maul))
print(sidious.fight(plagueis))
print(plagueis.impart())
print(plagueis.impart())
print(plagueis.get_powers())
print(sidious.get_powers())
print(sidious.fight(plagueis))
print(sidious.train("lightning"))
print(sidious.fight(plagueis))
print(sidious.take_apprentice(maul))
print(plagueis.train("choke"))
print(sidious.impart())
print(maul.train(maul.get_powers()[0][0]))
print(maul.train(maul.get_powers()[0][0]))
print(maul.train(maul.get_powers()[0][0]))
print(maul.impart())
print(maul.take_apprentice(tyranus))
print(maul.fight(sidious))
print(sidious.take_apprentice(tyranus))
print(vader.train("hate"))
print(vader.fight(tyranus))
print(sidious.take_apprentice(vader))

            
### Test cases
def test3():
    plagueis = Sith("Plagueis", "lightning", "choke") 
    sidious = Sith("Sidious", "shadow")
    maul = Sith("Maul")
    tyranus = Sith("Tyranus")
    vader = Sith("Vader", "hate")

    print("plagueis.get_name():", plagueis.get_name() == 'Darth Plagueis' , sep="\t")
    print("plagueis.get_powers():", dict(plagueis.get_powers()) == {'choke':0, 'lightning':0} , sep="\t")
    print("plagueis.train('choke'):", plagueis.train("choke") == 'Darth Plagueis trains choke to level 1' , sep="\t")
    print("plagueis.train('lightning'):", plagueis.train("lightning") == 'Darth Plagueis trains lightning to level 1' , sep="\t")
    print("plagueis.take_apprentice(sidious):", plagueis.take_apprentice(sidious) == 'Darth Plagueis takes Darth Sidious as an apprentice' , sep="\t")
    print("plagueis.get_apprentice():", plagueis.get_apprentice() == 'Darth Sidious' , sep="\t")
    print("sidious.get_master():", sidious.get_master() == 'Darth Plagueis' , sep="\t")
    print("plagueis.impart():", plagueis.impart() in ['Darth Plagueis imparts choke to Darth Sidious', 'Darth Plagueis imparts lightning to Darth Sidious'] , sep="\t")
    print("sidious.train('lightning'):", sidious.train("lightning") in ['Darth Sidious has does not know lightning', 'Darth Sidious trains lightning to level 1'] , sep="\t")
    print("sidious.train('choke'):", sidious.train("choke") in ['Darth Sidious has does not know choke' ,'Darth Sidious trains choke to level 1'], sep="\t")
    print("sidious.get_powers():", dict(sidious.get_powers()) in [{'choke':1, 'shadow':0}, {'lightning':1, 'shadow':0}], sep="\t")
    print("sidious.take_apprentice(maul):", sidious.take_apprentice(maul) == 'Darth Sidious cannot take Darth Maul as an apprentice' , sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious and Darth Plagueis are equally matched' , sep="\t")
    print("plagueis.impart():", plagueis.impart() in ['Darth Plagueis imparts lightning to Darth Sidious', 'Darth Plagueis imparts choke to Darth Sidious'] , sep="\t")
    print("plagueis.impart():", plagueis.impart() == 'Darth Plagueis has nothing to impart to Darth Sidious' , sep="\t")
    print("sidious.get_powers():", dict(sidious.get_powers()) in [{'choke':1, 'shadow':0, 'lightning':0}, {'choke':0, 'shadow':0, 'lightning':1}], sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious and Darth Plagueis are equally matched' , sep="\t")
    print("sidious.train('shadow'):", sidious.train("shadow") == 'Darth Sidious trains shadow to level 1' , sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious and Darth Plagueis are equally matched' , sep="\t")
    print("sidious.train('lightning'):", sidious.train("lightning") in ['Darth Sidious trains lightning to level 1','Darth Sidious trains lightning to level 2'] , sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious kills Darth Plagueis in battle' , sep="\t")
    print("sidious.take_apprentice(maul):", sidious.take_apprentice(maul) == 'Darth Sidious takes Darth Maul as an apprentice' , sep="\t")
    print("plagueis.train('choke'):", plagueis.train("choke") == 'Darth Plagueis is already dead' , sep="\t")
    print("sidious.impart():", sidious.impart() in ['Darth Sidious imparts choke to Darth Maul', 'Darth Sidious imparts lightning to Darth Maul', 'Darth Sidious imparts shadow to Darth Maul'] , sep="\t")
    print("maul.train(maul.get_powers()[0][0]):", maul.train(maul.get_powers()[0][0]) in ['Darth Maul trains choke to level 1', 'Darth Maul trains lightning to level 1', 'Darth Maul trains shadow to level 1'] , sep="\t")
    print("maul.train(maul.get_powers()[0][0]):", maul.train(maul.get_powers()[0][0]) in ['Darth Maul trains choke to level 2', 'Darth Maul trains lightning to level 2', 'Darth Maul trains shadow to level 2'] , sep="\t")
    print("maul.train(maul.get_powers()[0][0]):", maul.train(maul.get_powers()[0][0]) in ['Darth Maul trains choke to level 3', 'Darth Maul trains lightning to level 3', 'Darth Maul trains shadow to level 3'] , sep="\t")
    print("maul.impart():", maul.impart() == 'Darth Maul does not have an apprentice' , sep="\t")
    print("maul.take_apprentice(tyranus):", maul.take_apprentice(tyranus) == 'Darth Maul cannot take Darth Tyranus as an apprentice' , sep="\t")    
    print("maul.fight(sidious):", maul.fight(sidious) == 'Darth Sidious kills Darth Maul in battle' , sep="\t")
    print("sidious.take_apprentice(tyranus):", sidious.take_apprentice(tyranus) == 'Darth Sidious takes Darth Tyranus as an apprentice' , sep="\t")
    print("vader.train('hate'):", vader.train("hate") == 'Darth Vader trains hate to level 1' , sep="\t")    
    print("vader.fight(tyranus):", vader.fight(tyranus) == 'Darth Vader kills Darth Tyranus in battle' , sep="\t")
    print("sidious.take_apprentice(vader):", sidious.take_apprentice(vader) == 'Darth Sidious takes Darth Vader as an apprentice' , sep="\t")

def print3():
    plagueis = Sith("Plagueis", "lightning", "choke") 
    sidious = Sith("Sidious", "shadow")
    maul = Sith("Maul")
    tyranus = Sith("Tyranus")
    vader = Sith("Vader", "hate")
    
    print('plagueis.get_name():', plagueis.get_name())
    print('plagueis.get_powers():', plagueis.get_powers())
    print('plagueis.train("choke"):', plagueis.train("choke"))
    print('plagueis.train("lightning"):', plagueis.train("lightning"))
    print('plagueis.take_apprentice(sidious):', plagueis.take_apprentice(sidious))
    print('plagueis.get_apprentice():', plagueis.get_apprentice())
    print('sidious.get_master():', sidious.get_master())
    print('plagueis.impart():', plagueis.impart())
    print('sidious.train("lightning"):', sidious.train("lightning"))
    print('sidious.train("choke"):', sidious.train("choke"))
    print('sidious.get_powers():', sidious.get_powers())
    print('sidious.take_apprentice(maul):', sidious.take_apprentice(maul))
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('plagueis.impart():', plagueis.impart())
    print('plagueis.impart():', plagueis.impart())
    print('sidious.get_powers():', sidious.get_powers())
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('sidious.train("shadow"):', sidious.train("shadow"))
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('sidious.train("lightning"):', sidious.train("lightning"))
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('sidious.take_apprentice(maul):', sidious.take_apprentice(maul))
    print('plagueis.train("choke"):', plagueis.train("choke"))
    print('sidious.impart():', sidious.impart())
    print('maul.train(maul.get_powers()[0][0]):', maul.train(maul.get_powers()[0][0]))
    print('maul.train(maul.get_powers()[0][0]):', maul.train(maul.get_powers()[0][0]))
    print('maul.train(maul.get_powers()[0][0]):', maul.train(maul.get_powers()[0][0]))
    print('maul.impart():', maul.impart())
    print('maul.take_apprentice(tyranus):', maul.take_apprentice(tyranus))
    print('maul.fight(sidious):', maul.fight(sidious))
    print('sidious.take_apprentice(tyranus):', sidious.take_apprentice(tyranus))
    print('vader.train("hate"):', vader.train("hate"))
    print('vader.fight(tyranus):', vader.fight(tyranus))
    print('sidious.take_apprentice(vader):', sidious.take_apprentice(vader))

# Uncomment to show sample execution
# print3()

# Uncomment to test sample execution
# test3()
