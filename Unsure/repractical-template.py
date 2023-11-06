#******************************************************
#*
#*  CS1010S Re-Practical Exam
#*  AY2016/2015, Semester 1
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

def compute(f, x):
    val = 0
    for tup in f:
        coeff, exp = tup
        val += coeff*x**exp
    return val

def deriv(f):
    new = []
    for tup in f:
        coeff, exp = tup
        if exp == 0: continue
        curr = (coeff*exp, exp-1)
        new.append(curr)
    return tuple(new)


def root(f, x0, d):
    f_prime = deriv(f)
    delta = d+1
    while delta > d:
        xn = x0 - compute(f, x0)/compute(f_prime, x0)
        delta = abs(xn - x0)
        x0 = xn
    return xn

# Test cases
def test_q1a():
    print(compute(((3,2), (-8,0)), 8))
    print(compute(((1,3), (-2,2), (-11,1), (12,0)), -3))
    print(compute(((5,1),), 5))

def test_q1b():
    print(deriv(((3,2), (-8,0))))
    print(deriv(((1,3), (-2,2), (-11,1), (12,0))))
    print(deriv(((5,1),)))

def test_q1c():
    print(root(((3,2), (-8,0)), -1, 0.0001))
    print(root(((3,2), (-8,0)), 1, 0.0001))
    print(root(((1,3), (-2,2), (-11,1), (12,0)), 2.35287527, 0.0001))
    
# Uncomment to test
##test_q1a()
##test_q1b()
##test_q1c()

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


def statistics(fname, module_code):
    file = filter(lambda x: x[1] == module_code, read_csv(fname))
    students_marks = {}
    for row in file:
        student, mod, ca, marks = row
        students_marks[student] = students_marks.get(student, 0) + int(marks)
    students_marks = tuple(students_marks.items())
    all_marks = sorted(list(map(lambda x: x[1], students_marks)))
    total_marks = sum(all_marks)
    total_students = len(students_marks)
    ave = round(total_marks / total_students, 2)
    med = all_marks[total_students//2]
    return (med, ave)
    
def top_students(fname, module_code):
    file = filter(lambda x: x[1] == module_code, read_csv(fname))
    students_marks = {}
    for row in file:
        student, mod, ca, marks = row
        if student not in students_marks:
            students_marks[student] = {}
        students_marks[student][ca] = int(marks)
    for student in students_marks:
        students_marks[student]["Total"] = sum(map(lambda x: x[1], students_marks[student].items()))
    students_marks = sorted(list(students_marks.items()), key = lambda x: x[1]['Total'], reverse = True)
    from math import floor
    if len(students_marks) < 10:
        studentID, marksdict = students_marks[0]
        return {studentID: (marksdict['Midterm'], marksdict['PE'], marksdict['Project'])}
    top10 = floor(len(students_marks)/10)
    tenth = students_marks[top10-1][1]['Total']
    filtered = filter(lambda x: x[1]['Total'] >= tenth, students_marks)
    res = {}
    for student in filtered:
        studentID, marksdict = student
        res[studentID] = (marksdict['Midterm'], marksdict['PE'], marksdict['Project'])
    return res

# Test cases
def test_q2a():
    print(statistics("evil.csv", "CS1010E"))
    print(statistics("evil.csv", "MA1105"))
    print(statistics("evil.csv", "CM1101"))

def test_q2b():
    print(top_students('evil.csv', 'CS2105') ==
          { 'A00584X': (20, 11, 12), 'A00862H': (19, 13, 14),
            'A00249V': (17, 15, 15), 'A00270U': (17, 11, 15),
            'A00691H': (17, 15, 10), 'A00547W': (19, 12, 15),
            'A00619O': (14, 13, 15) })
    print(top_students('evil.csv', 'CM1101') ==
          { 'A00732A': (16, 13, 15) })
    print(top_students('evil.csv', 'EG1109') ==
          { 'A00060A': (17, 12, 15), 'A00467J': (16, 14, 14),
            'A00897P': (18, 15, 10), 'A00051B': (19, 14, 12),
            'A00148Y': (19, 12, 14), 'A00911R': (19, 12, 12), 
            'A00642Y': (14, 14, 15), 'A00700Y': (18, 15, 15) })

# Uncomment to test
##test_q2a()
##test_q2b()

##############
# Question 3 #
##############

class Artifact:
    def __init__(self, name, charge, seq):
        self.name = name
        self.charge = charge
        self.seq = seq
        self.masters = []
    def get_name(self):
        return self.name
    def get_magics(self):
        return self.seq
    def get_charges(self):
        return self.charge
    def get_masters(self):
        return tuple(map(lambda x: x.get_name(), filter(lambda x: self in x.equipped, self.masters)))
    def choose(self, sorcerer):
        if sorcerer in self.masters:
            return f"{sorcerer.get_name()} is already chosen by {self.get_name()}"
        self.masters.append(sorcerer)
        sorcerer.artifacts.append(self)
        return f"{self.get_name()} chooses {sorcerer.get_name()}"
    def abandon(self, sorcerer):
        if sorcerer not in self.masters:
            return f"{sorcerer.get_name()} is not chosen by {self.get_name()}"
        self.masters.remove(sorcerer)
        sorcerer.artifacts.remove(self)
        return f"{self.get_name()} abandons {sorcerer.get_name()}"
    
class Sorcerer:
    def __init__(self, name):
        self.name = name
        self.artifacts = []
        self.equipped = []
        self.inactivemagics = {}
    def get_name(self):
        return self.name
    def get_artifacts(self):
        return tuple(map(lambda x: x.get_name(), self.artifacts))
    def get_magics(self):
        res = {}
        for artifact in self.equipped:
            if not artifact.masters or self in artifact.masters:
                for spell in artifact.seq:
                    res[spell] = self.inactivemagics.get(spell, 1)
        return res
        return self.activemagics
    def equip(self, artifact):
        if artifact in self.equipped:
            return f"{self.get_name()} is already equipping the {artifact.get_name()}"
##        if (artifact.masters and self in artifact.masters) or (not artifact.masters):
##            for magic in artifact.get_magics():
##                self.activemagics[magic] = self.inactivemagics.get(magic, 1)
        self.equipped.append(artifact)
        return f"{self.get_name()} equips {artifact.get_name()}"
    def unequip(self, artifact):
        if artifact not in self.equipped:
            return f"{self.get_name()} is not equipped with the {artifact.get_name()}"
        self.equipped.remove(artifact)
##        if (artifact.masters and self in artifact.masters) or (not artifact.masters):
##            for magic in artifact.get_magics():
##                self.inactivemagics[magic] = self.inactivemagics.get(magic, self.activemagics[magic])
##                del self.activemagics[magic]
        return f"{self.get_name()} unequips {artifact.get_name()}"
    def train(self):
        if not self.get_magics():
            return f"{self.get_name()} does not have any magic"
        lowest = min(list(self.get_magics().items()), key=lambda x: x[1])[0]
        self.inactivemagics[lowest] = self.inactivemagics.get(lowest, 2)
        return f"{self.get_name()} trains {lowest} to level {self.inactivemagics[lowest]}"
    def chant(self, spell):
        if spell not in self.get_magics():
            return f"{self.get_name()} cannot {spell}"

        
##        print(f"equipped = {self.equipped}")
##        print(f"master = {self.artifacts}")
        spellfilter = tuple(filter(lambda x: spell in x.seq, self.equipped))
##        print(f"spellfilter = {spellfilter}")

        
        highest = max(spellfilter, key = lambda x: x.charge)
        if highest.charge == 0: return f"{self.get_name()} cannot {spell}"
        highest.charge -= self.get_magics()[spell]        
        if highest.charge < 0: highest.charge = 0
        return f"{self.get_name()} does {spell} with {highest.get_name()}"

eye_of_agamotto = Artifact("Eye of Agamotto", 3, ("Time magic", "Levitation", "Hypnosis"))
cloak_of_levitation = Artifact("Cloak of Levitation", 2, ("Levitation",))
silver_dagger = Sorcerer("Silver Dagger")
stephen_strange = Sorcerer("Doctor Strange")
print(stephen_strange.get_name())
print(silver_dagger.get_magics())
print(eye_of_agamotto.get_name())
print(eye_of_agamotto.get_magics())
print(silver_dagger.equip(eye_of_agamotto))
print(silver_dagger.equip(eye_of_agamotto))
print(silver_dagger.get_magics())
print(silver_dagger.unequip(cloak_of_levitation))
print(silver_dagger.equip(cloak_of_levitation))
print(silver_dagger.get_magics())
print(eye_of_agamotto.get_charges())
print(silver_dagger.chant("Levitation"))
##stop 1901
##resume 1926
print(eye_of_agamotto.get_charges())
print(eye_of_agamotto.get_masters())
print(eye_of_agamotto.choose(stephen_strange))
print(silver_dagger.get_magics())
print(stephen_strange.get_magics())
print(eye_of_agamotto.get_masters())
print(silver_dagger.unequip(eye_of_agamotto))
print(stephen_strange.equip(eye_of_agamotto))
print(stephen_strange.get_magics())
print(eye_of_agamotto.get_masters())
print(stephen_strange.train())
print(stephen_strange.unequip(eye_of_agamotto))
print(eye_of_agamotto.get_masters())
print(stephen_strange.train())
print(stephen_strange.get_magics())
print(stephen_strange.equip(eye_of_agamotto))
print(stephen_strange.get_magics())
print(stephen_strange.train())
print(stephen_strange.train())
print(stephen_strange.get_magics())
print(eye_of_agamotto.choose(silver_dagger))
print(silver_dagger.equip(eye_of_agamotto))
print(stephen_strange.chant("Hypnosis"))
print(silver_dagger.chant("Time magic") )
print(silver_dagger.chant("Levitation"))
print(eye_of_agamotto.get_masters())
print(cloak_of_levitation.abandon(silver_dagger))
print(eye_of_agamotto.abandon(silver_dagger))




# Test cases
def test_q3():
    eye_of_agamotto = Artifact("Eye of Agamotto", 3, ("Time magic", "Levitation", "Hypnosis"))
    cloak_of_levitation = Artifact("Cloak of Levitation", 2, ("Levitation",))

    silver_dagger = Sorcerer("Silver Dagger")
    stephen_strange = Sorcerer("Doctor Strange")

    print('stephen_strange.get_name():\t', stephen_strange.get_name() == "Doctor Strange")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {})
    print('eye_of_agamotto.get_name():\t', eye_of_agamotto.get_name() == "Eye of Agamotto")
    print('eye_of_agamotto.get_magics():\t', sorted(eye_of_agamotto.get_magics()) == ['Hypnosis', 'Levitation', 'Time magic'])
    print('silver_dagger.equip(eye_of_agamotto):\t', silver_dagger.equip(eye_of_agamotto) == "Silver Dagger equips Eye of Agamotto")
    print('silver_dagger.equip(eye_of_agamotto):\t', silver_dagger.equip(eye_of_agamotto) == "Silver Dagger is already equipping the Eye of Agamotto")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 1})
    print('silver_dagger.unequip(cloak_of_levitation):\t', silver_dagger.unequip(cloak_of_levitation) == "Silver Dagger is not equipped with the Cloak of Levitation")
    print('silver_dagger.equip(cloak_of_levitation):\t', silver_dagger.equip(cloak_of_levitation) == "Silver Dagger equips Cloak of Levitation")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 1})
    print('eye_of_agamotto.get_charges():\t', eye_of_agamotto.get_charges() == 3)
    print('silver_dagger.chant("Levitation"):\t', silver_dagger.chant("Levitation") == "Silver Dagger does Levitation with Eye of Agamotto")
    print('eye_of_agamotto.get_charges():\t', eye_of_agamotto.get_charges() == 2)
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ())
    print('eye_of_agamotto.choose(stephen_strange):\t', eye_of_agamotto.choose(stephen_strange) == "Eye of Agamotto chooses Doctor Strange")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {'Levitation': 1})
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {})
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ())
    print('silver_dagger.unequip(eye_of_agamotto):\t', silver_dagger.unequip(eye_of_agamotto) == "Silver Dagger unequips Eye of Agamotto")
    print('stephen_strange.equip(eye_of_agamotto):\t', stephen_strange.equip(eye_of_agamotto) == "Doctor Strange equips Eye of Agamotto")
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 1})
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ('Doctor Strange',))
    print('stephen_strange.train():\t', stephen_strange.train() in ("Doctor Strange trains Levitation to level 2",
                                                                    "Doctor Strange trains Hypnosis to level 2",
                                                                    "Doctor Strange trains Time magic to level 2"))
    print('stephen_strange.unequip(eye_of_agamotto):\t', stephen_strange.unequip(eye_of_agamotto) == "Doctor Strange unequips Eye of Agamotto")
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ())
    print('stephen_strange.train():\t', stephen_strange.train() == "Doctor Strange does not have any magic")
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {})
    print('stephen_strange.equip(eye_of_agamotto):\t', stephen_strange.equip(eye_of_agamotto) == "Doctor Strange equips Eye of Agamotto")
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() in ({'Levitation': 2, 'Time magic': 1, 'Hypnosis': 1},
                                                                              {'Levitation': 1, 'Time magic': 2, 'Hypnosis': 1},
                                                                              {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 2}))
    print('stephen_strange.train():\t', stephen_strange.train() in ("Doctor Strange trains Levitation to level 2",
                                                                    "Doctor Strange trains Hypnosis to level 2",
                                                                    "Doctor Strange trains Time magic to level 2"))
    print('stephen_strange.train():\t', stephen_strange.train() in ("Doctor Strange trains Levitation to level 2",
                                                                    "Doctor Strange trains Hypnosis to level 2",
                                                                    "Doctor Strange trains Time magic to level 2"))
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {'Levitation': 2, 'Time magic': 2, 'Hypnosis': 2})
    print('eye_of_agamotto.choose(silver_dagger):\t', eye_of_agamotto.choose(silver_dagger) == "Eye of Agamotto chooses Silver Dagger")
    print('silver_dagger.equip(eye_of_agamotto):\t', silver_dagger.equip(eye_of_agamotto) == "Silver Dagger equips Eye of Agamotto")
    print('stephen_strange.chant("Hypnosis"):\t', stephen_strange.chant("Hypnosis") == "Doctor Strange does Hypnosis with Eye of Agamotto")
    print('silver_dagger.chant("Time magic"):\t', silver_dagger.chant("Time magic") == "Silver Dagger cannot Time magic")
    print('silver_dagger.chant("Levitation"):\t', silver_dagger.chant("Levitation") == "Silver Dagger does Levitation with Cloak of Levitation")
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ('Doctor Strange', 'Silver Dagger'))
    print('cloak_of_levitation.abandon(silver_dagger):\t', cloak_of_levitation.abandon(silver_dagger) == "Silver Dagger is not chosen by Cloak of Levitation")
    print('eye_of_agamotto.abandon(silver_dagger):\t', eye_of_agamotto.abandon(silver_dagger) == "Eye of Agamotto abandons Silver Dagger")


# uncomment to test
# test_q3()
