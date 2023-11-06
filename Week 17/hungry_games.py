from random import *

######################
# Class: NamedObject #
######################

class NamedObject(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<{0} : {1}>".format(self.name, self.__class__.__name__)

################
# Class: Place #
################

class Place(NamedObject):
    def __init__(self, name):
        super().__init__(name)
        self.objects = []
        self.neighbor_dict = {} # direction: place

    def add_object(self, new_object):
        ''' Add only Thing and LivingThing to current place '''
        if isinstance(new_object, Thing) or isinstance(new_object, LivingThing):
            self.objects.append(new_object)
            new_object.place = self
        else:
            print("Cannot add {0}!".format(new_object))

    def del_object(self, curr_object):
        ''' Delete object from current place'''
        if curr_object in self.objects:
            self.objects.remove(curr_object)
            curr_object.place = None
        else:
            print("{0} is not at {1}".format(curr_object, self.name))

    def get_objects(self):
        return self.objects
    
    def get_exits(self):
        ''' Returns the exits of current place'''
        return list(self.neighbor_dict.keys())

    def add_neighbor(self, new_neighbor,direction):
        opp_dir = opposite_direction(direction)
        if direction not in self.neighbor_dict.keys() and opp_dir not in new_neighbor.neighbor_dict.keys():
            self.neighbor_dict[direction] = new_neighbor
            new_neighbor.neighbor_dict[opp_dir] = self
        else:
            print("A neighbor is already assigned!")

    def get_neighbors(self):
        ''' Returns neighbors of current place'''
        return list(self.neighbor_dict.values())

    def get_neighbor_at(self, direction):
        ''' Get neighbor at sepcified exit'''
        return self.neighbor_dict.get(direction, None)

#######################
# Class: MobileObject #
#######################

class MobileObject(NamedObject):
    def __init__(self, name, place):
        super().__init__(name)
        self.place = place

    def get_place(self):
        return self.place

################
# Class: Thing #
################

class Thing(MobileObject):
    def __init__(self, name):
        super().__init__(name, None)
        self.owner = None 

    def get_owner(self):
        return self.owner

    def is_owned(self):
        return self.owner is not None

######################
# Class: LivingThing #
######################

class LivingThing(MobileObject):
    def __init__(self, name, health, threshold):
        super().__init__(name, None)
        self.health = health
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold

    def get_health(self):
        ''' Returns the current health of this living thing. '''
        return self.health

    def add_health(self, health):
        self.health = min(100, self.health+health)

    def reduce_health(self, health):
        self.health = max(0, self.health-health)
        if self.health == 0:
            self.go_to_heaven()

    def go_to_heaven(self):
        self.place.del_object(self)
        heaven.add_object(self)
        print(self, "went to heaven!")
        return True

    def move_to(self, new_place):
        ''' Move to an adjacent place '''
        old_place = self.place
        if new_place in old_place.neighbor_dict.values():
            old_place.del_object(self)
            new_place.add_object(self)
            print("{0} moves from {1} to {2}".format(self.name, old_place, new_place))
        else:
            print("{0} cannot move from {1} to {2}".format(self.name, old_place, new_place))

    def act(self):
        if self.threshold >= 0 and randint(0, self.threshold) == 0:
            new_place = random_neighbor(self.place)
            if new_place:
                self.move_to(new_place)

#################
# Class: Person #
#################

class Person(LivingThing):
    def __init__(self, name, health, threshold):
        self.inventory = []
        super().__init__(name, health, threshold)
        
    def take(self, thing):
        ''' Takes an item and put into inventory. '''
        if isinstance(thing, Thing) and thing in self.place.objects and not thing.is_owned():
            ''' Can only take thing in current location & not owned by others '''
            thing.owner = self
            self.inventory.append(thing)
            self.place.del_object(thing)
            print(self.name, 'took', thing.name, 'in', self.place.name)
        else:
            print("{1} cannot take {0}.".format(thing.name, self.name))
                    
    def go(self, direction):
        new_place = self.place.get_neighbor_at(direction.upper())
        if new_place is not None:
            self.move_to(new_place)
        else:
            print("{2} cannot go {0} from {1}".format(direction, self.place.name, self.name))

    def get_inventory(self):
        ''' Returns the list of items in the inventory. '''
        return list(self.inventory)

    def objects_around(self):
        ''' Returns the list of objects in the current location. '''
        return [t for t in self.place.objects if t is not self]

    def get_exits(self):
        return self.place.get_exits()

##################
# Misc Functions #
##################

# define places
Base = Place("Base")
heaven = Place("Heaven")

# define direction
up = "UP"
down = "DOWN"
north = "NORTH"
south = "SOUTH"
east = "EAST"
west = "WEST"

global_directions = ['NORTH', 'EAST', 'UP','SOUTH', 'WEST', 'DOWN']

def opposite_direction(direction):
    index = global_directions.index(direction)
    index = (index+3) % 6
    return global_directions[index]

def random_neighbor(place):
    return pick_random(place.get_neighbors())

def pick_random(lst):
    if lst:
        rand_index = randint(0, len(lst) - 1)
        return lst[rand_index]
    else:
        return None
