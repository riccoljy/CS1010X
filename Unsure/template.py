##############
# Question 1 #
##############

def next_pos(seq, i):
    while True:
        i += 1
        i %= len(seq)
        if seq[i]: return i


def next_k(seq, i, k):
    counter = 0
    while counter < k:
        i += 1
        i %= len(seq)
        if seq[i]: counter += 1
    return i


def josephus(n, k):
    lst = list(range(n))
    k = k-1
    while len(lst) > 1:
        k %= len(lst)
        lst = lst[k+1:] + lst[:k]
    return lst[0]

# Test cases
def test_q1a():
    print(next_pos((True, True, False, True, False), 1))
    print(next_pos((True, True, False, True, False), 3))
    print(next_pos((False, False, True, False, False, False), 3))

def test_q1b():
    print(next_k((True, True, False, True, False), 0, 2))
    print(next_k((True, True, False, True, False), 2, 3))

def test_q1c():
    print(josephus(10, 2))
    print(josephus(10, 3))
    print(josephus(41, 2))

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


def highest_year(fname, course):
    file = filter(lambda x: x[2] == course and x[-1].isdigit(), read_csv(fname))
    res = {}
    for row in file:
        year, num = row[0], int(row[-1])
        res[year] = res.get(year, 0) + num
    res = list(res.items())
    return max(res, key = lambda x: x[1])


def gender_ratio(fname, course):
    file = filter(lambda x: x[2] == course and x[-1].isdigit(), read_csv(fname))
    res = {}
    for row in file:
        year, sex, course, num = row
        num = int(num)
        if year not in res:
            res[year] = {}
        res[year][sex] = res[year].get(sex, 0) + num
    for year in res.copy():
        subdict = res[year]
        if subdict["Females"] == 0:
            res[year] = float("inf")
            continue
        perc = round(subdict["Males"] / subdict["Females"], 2)
        res[year]= perc
    return res


# Test cases
def test_q2a():
    print(highest_year("graduates.csv", "Law"))
    print(highest_year("graduates.csv", "Medicine"))
    print(highest_year("graduates.csv", "Dentistry"))

def test_q2b():
    print(gender_ratio("graduates.csv", "Law") == 
            {'1993': 0.99, '1994': 0.88, '1995': 0.94, '1996': 0.71,
             '1997': 0.93, '1998': 0.68, '1999': 1.19, '2000': 0.94, 
             '2001': 0.6,  '2002': 0.95, '2003': 0.73, '2004': 0.62,
             '2005': 0.5,  '2006': 0.52, '2007': 0.68, '2008': 0.82,
             '2009': 0.78, '2010': 1.54, '2011': 0.58, '2012': 0.68,
             '2013': 1.06, '2014': 1.02})
    print(gender_ratio("graduates.csv", "Accountancy") == 
            {'1993': 0.74, '1994': 0.72, '1995': 0.73, '1996': 0.61, 
             '1997': 0.5,  '1998': 0.54, '1999': 0.62, '2000': 0.51, 
             '2001': 0.53, '2002': 0.42, '2003': 0.42, '2004': 0.6, 
             '2005': 0.43, '2006': 0.38, '2007': 0.45, '2008': 0.55, 
             '2009': 0.58, '2010': 0.69, '2011': 0.65, '2012': 0.76, 
             '2013': 0.58, '2014': 0.73})
    print(gender_ratio("graduates.csv", "Services") == 
            {'2007': float("inf"),  '2008': 0.33, '2009': 0.36, '2010': 0.83, 
             '2011': 0.48, '2012': 0.82, '2013': 0.34, '2014': 0.62})

# Uncomment to test
##test_q2a()
##test_q2b()

##############
# Question 3 #
##############

class Trainer:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.pokemons = []
    def curr_level(self):
        return f"{self.name} is currently at level {self.level}"
    def list_pokemons(self):
        return tuple(map(lambda x: x.name, self.pokemons))
    def catch(self, pokemon):
        if pokemon.owner:
            return f"{pokemon.name} is already owned by {pokemon.owner.name}"
        elif pokemon.level > self.level:
            return f"{pokemon.name} got away!"
        else:
            self.pokemons.append(pokemon)
            pokemon.owner = self
            return f"{self.name} has caught {pokemon.name}"
    def give(self, pokemon, new_trainer):
        if pokemon not in self.pokemons:
            return f"{self.name} does not own {pokemon.name}"
        elif new_trainer == self:
            return "Cannot give to self"
        elif pokemon.level > new_trainer.level:
            return f"{new_trainer.name}'s level is not high enough"
        else:
            self.pokemons.remove(pokemon)
            new_trainer.pokemons.append(pokemon)
            pokemon.owner = new_trainer
            return f"{pokemon.name} transfers from {self.name} to {new_trainer.name}"        

class Pokemon:
    def __init__(self, name, level, *evolution_names):
        self.name = name
        self.level = level
        self.owner = None
        self.evolutions = evolution_names

    def curr_level(self):
        return f"{self.name} is currently at level {self.level}"
    def owned_by(self):
        if not self.owner:
            return f"{self.name} has no trainer"
        return f"{self.name}'s owner is {self.owner.name}"
    def power_up(self):
        if not self.owner:
            return f"{self.name} needs a trainer to power up"
        elif self.level < self.owner.level:
            self.level += 1
            return f"{self.name} powers up to level {self.level}"
        elif all(map(lambda x: x.level == self.owner.level, self.owner.pokemons)):
            self.owner.level += 1
            return f"{self.owner.name} levels up to level {self.owner.level}"
        else:
            return f"{self.name} cannot exceed trainer's level"
    def evolve(self):
        if not self.evolutions:
            raise EvolveError(self)
        new = Pokemon(self.evolutions[0], self.level, *self.evolutions[1:])
        if self.owner:
            self.owner.pokemons.remove(self)
            self.owner.pokemons.append(new)
            new.owner = self.owner
            self.owner = None
        return new

class EvolveError(Exception):
    def __init__(self, pokemon):
        self.pokemon = pokemon
        super().__init__(f"{pokemon.name} cannot evolve further" )

# Test cases
def test_q3():
    ash = Trainer("Ash")
    misty = Trainer("Misty")
    pikachu = Pokemon("Pikachu", 1)
    staryu = Pokemon("Staryu", 1)
    p1 = Pokemon("Pidgey", 1)
    p2 = Pokemon("Pidgey", 1)

    print('ash.curr_level():', ash.curr_level() == "Ash is currently at level 1")
    print('ash.list_pokemons():', ash.list_pokemons() == ())
    print('pikachu.curr_level():', pikachu.curr_level() == "Pikachu is currently at level 1")
    print('pikachu.owned_by():', pikachu.owned_by() == "Pikachu has no trainer")
    print('pikachu.power_up():', pikachu.power_up() == "Pikachu needs a trainer to power up")
    print('ash.catch(pikachu):', ash.catch(pikachu) == "Ash has caught Pikachu")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pikachu',])
    print('pikachu.owned_by():', pikachu.owned_by() == "Pikachu's owner is Ash")
    print('pikachu.power_up():', pikachu.power_up() == "Ash levels up to level 2")
    print('ash.curr_level():', ash.curr_level() == "Ash is currently at level 2")
    print('misty.catch(staryu):', misty.catch(staryu) == "Misty has caught Staryu")
    print('ash.catch(staryu):', ash.catch(staryu) == "Staryu is already owned by Misty")
    print('ash.catch(p1):', ash.catch(p1) == "Ash has caught Pidgey")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pidgey', 'Pikachu'])
    print('pikachu.power_up():', pikachu.power_up() == "Pikachu powers up to level 2")
    print('pikachu.power_up():', pikachu.power_up() == "Pikachu cannot exceed trainer's level")
    print('p1.power_up():', p1.power_up() == "Pidgey powers up to level 2")
    print('ash.catch(p2):', ash.catch(p2) == "Ash has caught Pidgey")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pidgey', 'Pidgey', 'Pikachu'])
    print('ash.give(p1, ash):', ash.give(p1, ash) == "Cannot give to self")
    print('ash.give(staryu, misty):', ash.give(staryu, misty) == "Ash does not own Staryu")
    print('ash.give(p1, misty):', ash.give(p1, misty) == "Misty's level is not high enough")
    print('ash.give(p2, misty):', ash.give(p2, misty) == "Pidgey transfers from Ash to Misty")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pidgey', 'Pikachu'])
    print('misty.list_pokemons():', sorted(misty.list_pokemons()) == ['Pidgey', 'Staryu'])
    print('p2.owned_by():', p2.owned_by() == "Pidgey's owner is Misty")
    charmander = Pokemon("Charmander", 3, "Charmelon", "Charizard")
    print('ash.catch(charmander):', ash.catch(charmander) == "Charmander got away!")
    print('p1.power_up():', p1.power_up() == "Ash levels up to level 3")    
    charmelon = charmander.evolve()
    print('charmelon == charmander:', not (charmelon == charmander))
    print('ash.catch(charmelon):', ash.catch(charmelon) == "Ash has caught Charmelon")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Charmelon', 'Pidgey', 'Pikachu'])
    charizard = charmelon.evolve()
    print(ash.list_pokemons())
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Charizard', 'Pidgey', 'Pikachu'])
    print('charizard.owned_by():', charizard.owned_by() == "Charizard's owner is Ash")
    print('charmelon.owned_by():', charmelon.owned_by() == "Charmelon has no trainer")

    try:
        charizard.evolve()
    except EvolveError as e:
        p = e.pokemon
        print(p.curr_level() == "Charizard is currently at level 3")
        print(str(e) == "Charizard cannot evolve further")


# Uncomment to test
test_q3()
