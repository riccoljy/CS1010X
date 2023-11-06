#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from contest_simulation import *
import random


class Player(Tribute):
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

#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
if __name__ == '__main__':
    def qualifer_map(size, wrap):
        game_config = GameConfig()
        game_config.set_item_count(Weapon, 10)
        game_config.set_item_count(RangedWeapon, 10)
        game_config.set_item_count(Food, 10)
        game_config.set_item_count(Medicine, 10)
        game_config.set_item_count(Animal, 10)
        game_config.steps = 1000

        def spawn_wild_animals(game):
            for i in range(3):
                animal = DefaultItemFactory.create(WildAnimal)
                game.add_object(animal[0])
                GAME_LOGGER.add_event("SPAWNED", animal[0])
        game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")

        return (GameMap(size, wrap=wrap), game_config)

    # Create 6 AI Clones
    tributes = []
    for i in range(6):
        # An AI is represented by a tuple, with the Class as the first element,
        # and the name of the AI as the second
        ai = (Player, "AI" + str(i))
        tributes.append(ai)

    # Qualifier Rounds
    # Uncomments to run more rounds, or modify the rounds list
    # to include more rounds into the simulation
    # (Note: More rounds = longer simulation!)
    rounds = [qualifer_map(4, False),
              #qualifer_map(4, False),
              #qualifer_map(4, False),
              qualifer_map(4, True),
              #qualifer_map(4, True),
              #qualifer_map(4, True),
             ]



    match = Match(tributes, rounds)
    print("Simulating matches... might take a while")

    # Simulate without the graphics
    match.text_simulate_all()

    # Simulate a specific round with the graphics
    # Due to limitation in the graphics framework,
    # can only simulate one round at a time
    # Round id starts from 0
##    match.gui_simulate_round(0)
