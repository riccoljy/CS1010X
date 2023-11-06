from hungry_games import *

################
# Class: Troll #
################
    
class Troll(Person):
    """
    A troll is a kind of person (but not a kind person!)
    """
    def __init__(self, name, health, threshold):
        super().__init__(name, health, threshold)
        
    def act(self):
        others = [t for t in self.place.objects if t is not self and isinstance(t, Person)]
        should_eat = (randint(0, 1) == 0)
        if should_eat and others:
            self.eat_person(pick_random(others))
        else:
            super().act()

    def eat_person(self, person):
        #self.say("GROWL.... I'm going to eat you, {0}".format(person))
        person.reduce_health(person.get_health())
        #self.say("Chomp chomp. {0} tastes yummy! *burp*".format(person.name))

#################
# Class: SDCard #
#################

class SDCard(Thing):
    def __init__(self, name, id_num):
        self.id_num = id_num
        super().__init__(name)
    def is_sdcard(self):
        return True
    def copy(self):
        return SDCard(self.name, self.place, self.id_num)
    def __str__(self):
        return "{0} with id: {1}".format(self.name, self.id_num)

##################
# Clock routines #
##################

clock_list = [] # list of persons to move when clock ticks
dead_list = []
the_time = 0

def init_clock_list():
    global clock_list
    clock_list = []

def add_to_clock_list(person):
    clock_list.append(person)

def remove_from_clock_list(person):
    clock_list.remove(person)

def tick():
    print("---Tick---")
    global the_time
    the_time = the_time + 1
    dead_list = []
    for person in clock_list:
        if person.health <= 0:
            dead_list.append(person)
        else:
            person.act()
    for person in dead_list:
        clock_list.remove(person)

def current_time():
    return the_time

def run_clock(n):
    if n > 0:
        tick()
        run_clock(n - 1)

###########################
# Code for adventure game #
###########################

# define places
central_library = Place("central_library")
forum = Place("forum")
lt15 = Place("lt15")
arts_canteen = Place("arts_canteen")
com1_open_area = Place("com1_open_area")
sr1 = Place("sr1")
com1_classrooms = Place("com1_classrooms")
beng_office = Place("beng_office")
bing_office = Place("bing_office")
com1_lift_lobby_top  = Place("com1_life_lobby_top")
com1_lift_lobby_bottom = Place("com1_lift_lobby_bottom")
com1_ladies = Place("com1_ladies")
com1_gents = Place("com1_gents")
secret_portal = Place("secret_portal")
ben_office = Place("ben_office")
technical_services = Place("technical_services")
com1_research_labs = Place("com1_research_labs")
com1_staircase_top = Place("com1_staircase_top")
com1_student_area = Place("com1_student_area")
enchanted_garden = Place("enchanted_garden")
data_comm_lab2 = Place("data_comm_lab2")
com1_staircase_bottom = Place("com1_staircase_bottom")

# Adding neighbors
forum.add_neighbor(central_library, up)
bing_office.add_neighbor(central_library, north)
lt15.add_neighbor(forum, north)
arts_canteen.add_neighbor(lt15, east)
lt15.add_neighbor(bing_office, up)
com1_open_area.add_neighbor(lt15, north)
com1_open_area.add_neighbor(sr1, east)
com1_classrooms.add_neighbor(com1_open_area, north)
beng_office.add_neighbor(com1_classrooms, north)
com1_lift_lobby_top.add_neighbor(com1_open_area, east)
com1_lift_lobby_bottom.add_neighbor(com1_lift_lobby_top, up)
com1_ladies.add_neighbor(com1_lift_lobby_bottom, north)
com1_gents.add_neighbor(com1_ladies, north)
secret_portal.add_neighbor(com1_gents, up)
ben_office.add_neighbor(secret_portal, east)
com1_lift_lobby_bottom.add_neighbor(technical_services, east)
com1_research_labs.add_neighbor(technical_services, north)
com1_staircase_top.add_neighbor(com1_research_labs, north)
com1_student_area.add_neighbor(technical_services, up)
com1_student_area.add_neighbor(enchanted_garden, east)
data_comm_lab2.add_neighbor(com1_student_area, north)
com1_staircase_bottom.add_neighbor(data_comm_lab2, north)
com1_staircase_bottom.add_neighbor(com1_staircase_top, up)

init_clock_list()

# define important critters in our world
#you = Person("you", 100, 0)
beng = Person("beng", 100, 0)
bing = Person("bing", 100, 1)
proffy = Troll("proffy", 100, 2)

# Add critters to places
#beng_office.add_object(you)
beng_office.add_object(beng)
bing_office.add_object(bing)
lt15.add_object(proffy)

# Initialize clock_list
#add_to_clock_list(you)
add_to_clock_list(beng)
add_to_clock_list(bing)
add_to_clock_list(proffy)

bing_card = SDCard("bing_card", "888-12-3456")
beng_card = SDCard("beng_card", "888-98-7654")

bing_office.add_object(bing_card)
beng_office.add_object(beng_card)

def display_game_state():
    print("You are at: {0}".format(you.place))
    things_str = ', '.join(str(t) for t in you.place.objects)
    print("You see: {0}".format(things_str))
    print("Exits: {0}".format(you.place.get_exits()))


## EASTER EGG!!
## Sample commands: go NORTH
def play_game_interactive():
    clock_list.remove(you)
    while True:
        display_game_state()
        command = input("Command:")
        cmd_list = command.split()
        method = cmd_list[0]
        args = cmd_list[1:]
        try:
            getattr(you, method)(*args)
        except AttributeError as e:
            print("No such command:", command)
            continue
        tick()

def load_tut_codes():
    """
    runs the scripted game
    """
    python_docs = Thing("python_docs")
    lt15.add_object(python_docs)
    print(beng.objects_around())
    beng.go(north)
    beng.go(north)
    print(beng.get_place().get_exits())
    beng.go(north)
    bing.go(down)
    beng.take(python_docs)
    beng.go(north)
    bing.go(north)
    print(bing.objects_around())
    bing.take(python_docs)
    beng.go(up)
    bing.go(south)
    proffy.eat_person(bing)

def main():
    # Uncomment line below to play in interactive mode, easter egg!
    #play_game_interactive()
    # Uncomment line below to load all the actions listed in tutorial 9
    #load_tut_codes() 
    pass

if __name__ == "__main__":
    main()
