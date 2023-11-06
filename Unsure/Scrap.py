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

# Your answer here
def available_venues(file):
	res = {}
	timetable = read_csv(file)
	for module in timetable[1:]:
		venue = module[7]
		res[venue] = res.get(venue, 0) + 1
	return len(res)
# dpc is shorthand for decimal_point_compare - Do not modify!
def dpc(calculated, expected):
        # Your answer may be slightly different 
        # because of the accuracy of decimal point calculation
        # This function attempts to allow comparing inaccurate decimal point results
        # defaults to 3 decimal point precision
        return calculated // 0.001 == expected // 0.001

# Your answer here:
def venue_occupancy(filename):
    file = read_csv(filename)
    occupied = {}
    for i in range(1, 6):
        occupied[str(i)] = {}    
    for row in file[1:]:
        day = row[3]
        venue = row[7]
        starttime = int(row[5])
        endtime = int(row[6])
        
        if day == '6' or day == '7': continue

        if starttime > 1700: continue        
        elif starttime < 800:
            if endtime < 800: continue
            starttime = 800

    return


class Jedi(object):
    def __init__(self, name, level, *seq_of_power):
        self.name = name
        self.level = level
        self.master = None
        self.powers = []
        if seq_of_power:
            for power in seq_of_power[0]:
                self.powers.append((power, 0))
        self.disciples = []
    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_powers(self):
        return self.powers
    def get_master(self):
        return self.master.get_name()
    def set_master(self, master):
        if master.level < self.level:
            return f"{master.get_name()} has a lower level than {self.get_name()}"
        elif master == self.master:
            return f"{master.get_name()} is already the master of {self.get_name()}"
        self.master = master
        master.disciples.append(self)
        return f"{master.get_name()} takes {self.get_name()} as a disciple"
    def get_disciples(self):
        return list(map(lambda x: x.get_name(), self.disciples))
    def train(self):
        if not self.powers:
            return f"{self.get_name()} has not learnt any powers"
        lowest = min(self.powers, key=lambda x: x[1])[1]
        if lowest == self.level:
            self.level += 1
            if self.get_level() > self.master.get_level():
                
                self.master.disciples = self.disciples
                for disciple in self.disciples:
                    disciple.master = self.master
                self.disciples = [self.master]

                self.master.master.disciples.remove(self.master)
                self.master.master.disciples.append(self)
                
                self.master, self.master.master  = self.master.master, self
                

                
            return f"{self.get_name()} levels up to level {self.get_level()}"
        for i in range(len(self.powers)):
            power = self.powers[i]
            if power[1] == lowest:
                new = power[0], power[1]+1
                self.powers[i] = new
                return f"{self.get_name()} trains {new[0]} to level {new[1]}"
                
    def learn(self):
        if not self.master:
            return f"{self.get_name()} does not have a master"
        for power in self.master.get_powers():
            powername = power[0]
            if powername not in tuple(map(lambda x: x[0], self.powers)):
                new = (powername, 0)
                self.powers.append(new)
                return f"{self.get_name()} learns {new[0]} from {self.master.get_name()}"
        return f"{self.get_name()} has nothing to learn from {self.master.get_name()}"

dooku = Jedi("Dooku", 3, ("push", "jump"))
quigon = Jedi("Quigon", 2, ("mind trick",))
obiwan = Jedi("Obiwan", 1) # starts out with no powers
anakin = Jedi("Anakin", 1) #

luke = Jedi("Luke", 1) #

print(dooku.get_name())
print(dooku.get_level())
print(dooku.get_powers())
print(dooku.train())
print(dooku.get_powers())
print(dooku.train())
print(dooku.get_powers())
print(dooku.set_master(quigon))
print(quigon.set_master(dooku))
print(quigon.get_master())
print(quigon.train())
print(obiwan.train())
print(obiwan.learn())
print(obiwan.set_master(quigon))
print(obiwan.learn())
print(obiwan.get_powers())
print(obiwan.train())
print(obiwan.get_level())
print(obiwan.train())
print(obiwan.get_level())
print(obiwan.get_master())
print(quigon.get_disciples())
print(obiwan.learn())
print(obiwan.train())
print(anakin.set_master(obiwan))
print(luke.set_master(obiwan))

print(obiwan.train())
print(obiwan.get_master())
print(quigon.get_disciples())

print(obiwan.get_disciples())
print(dooku.get_disciples())
print(obiwan.learn())
print(obiwan.get_powers())
print(obiwan.train())
