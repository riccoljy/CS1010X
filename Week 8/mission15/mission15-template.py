#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class Ricco_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!


        #priority 1: ensure don't die; health < 100 and hunger < 100
        if self.get_medicine(): 

            #finding worst & best medicine
            meds = self.get_medicine()
            worst_med, best_med = meds[0], meds[0]
            lowest_med_val, highest_med_val = worst_med.get_medicine_value(), best_med.get_medicine_value()
            
            for med in meds[1:]:
                if med.get_medicine_value() < lowest_med_val:
                    worst_med = med
                    lowest_med_val = worst_med.get_medicine_value()
                if med.get_medicine_value() > highest_med_val:
                    best_med = med
                    highest_med_val = best_med.get_medicine_value()

                    
            if self.health + lowest_med_val <= 100: 
##                self.eat(worst_med)
                return ("EAT", worst_med)
            
            
        #and if no medicine, try to run away if health below certain treshold, say 20
        treshold = 20
        if self.health < treshold and not self.get_medicine():
            exits = self.get_exits()
            if exits:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)
            
        if self.get_food():
            
            #finding worst & best food
            food = self.get_food()
            worst_food, best_food = food[0], food[0]
            lowest_food_val, highest_food_val = worst_food.get_food_value(), best_food.get_food_value()
            
            for f in food[1:]:
                if f.get_food_value() < lowest_food_val:
                    worst_food = f
                    lowest_food_val = worst_food.get_food_value()
                if f.get_food_value() > highest_food_val:
                    best_food = f
                    highest_food_val = best_food.get_food_value()

            if self.get_hunger() - lowest_food_val >= 100: 
##                self.eat(worst_food)
                return ("EAT", worst_food)
            #and if no food, try to run away if hunger above certain treshold, say 80
            treshold = 80
            if self.get_hunger() > treshold and not self.get_food():
                exits = self.get_exits()
                if exits:
                    index = random.randint(0, len(exits)-1)
                    direction = exits[index]
                    return ("GO", direction)

                    
        #priority 2: take weapon/food/medicine if there's any
        for item in self.objects_around(): 
            if isinstance(item, Weapon) or isinstance(item, Ammo) or isinstance(item, Food):
                return ("TAKE", item)

        #-------------------------FINDING ENEMIES (IF ANY)------------------#
        enemies = []
        for obj in self.objects_around():
            if isinstance(obj, LivingThing):
                enemies.append(obj)
        weapons = self.get_weapons()
        #-------------------------------------------------------------------#

        #priority 3: kill enemies if any
        if enemies:
            #if no weapon, run away first
            if not weapons:
                exits = self.get_exits()
                if exits:
                    index = random.randint(0, len(exits)-1)
                    direction = exits[index]
                    return ("GO", direction)
            else: #if got weapon, attack
                #finding best weapon
                best_weapon, best_melee_weapon = weapons[0], weapons[0]
                best_mean_damage = (best_weapon.min_damage() + best_weapon.max_damage())/2
                best_melee_mean_damage = (best_melee_weapon.min_damage() + best_melee_weapon.max_damage())/2
                for weapon in weapons:
                    mean_damage = (weapon.min_damage() + weapon.max_damage())/2
                    if mean_damage > best_mean_damage:
                        best_weapon = weapon
                        best_mean_damage = mean_damage
                    if best_melee_mean_damage > best_mean_damage and not isinstance(weapon, RangedWeapon):
                        best_melee_weapon = weapon
                        best_melee_mean_damage = mean_damage
                        

                #after finding which is best weapon,

                #if best_weapon is RangedWeapon, check whether got shots loaded/ammo
                if isinstance(best_weapon, RangedWeapon):
                    ammo = None
                    for item in self.get_inventory():
                        if isinstance(item, Ammo):
                            if item.weapon_type() == best_weapon.name:
                                ammo = item
                                break
                           
                    #if best_weapon (ranged) no shots loaded but got ammo, load the weapon     
                    if best_weapon.shots_left() == 0 and ammo:
                        return ("LOAD", best_weapon, ammo)

                    #if no shots and no ammo, then need use best melee weapon.
                    elif best_weapon.shots_left() == 0 and ammo == None and not isinstance(best_melee_weapon, RangedWeapon):
                        return ("ATTACK", enemies[0], best_melee_weapon)

                    #if got shots loaded, then attack
                    elif best_weapon.shots_left() != 0:
                        return ("ATTACK", enemies[0], best_melee_weapon)
                elif isinstance(best_weapon, Weapon):                    
                    return ("ATTACK", enemies[0], best_weapon)
            
        #if no enemy, no meat, and reach here, go to next grid
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)
        
        # Otherwise, do nothing
        return None

# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = Ricco_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
##simulation.task1(Ricco_AI("Ricco AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
##simulation.task2(Ricco_AI("Ricco AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.optional_task(Ricco_AI("Ricco AI", 100), config, gui=False)
