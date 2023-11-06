##Recitation 9

class Food(object):
    def __init__(self, name, nutrition_val, good_until):
        self.name = name
        self.nutrition_value = nutrition_val
        self.good_until = good_until
        self.age = 0

    def sit_there(self, time):
        self.age += time

    def eat(self):
        if self.age < self.good_until: return self.nutrition_value
        return 0


class AgedFood(Food):
    def __init__(self, name, nutrition_val, good_until, good_after):
        super().__init__(name, nutrition_val, good_until)
        self.good_after = good_after

    def sniff(self):
        return self.age >= self.good_after

    def eat(self):
        if not self.sniff(): return 0
        return super().eat()

class VendingMachine(object):
    def __init__(self, name, nutrition_val, good_until):
        Food.__init__(self, name, nutrition_val, good_until)
        self.age = 0

    def sit_there(self, time):
        self.age += time/2

    def sell_food(self):
        food = Food(self.name, self.nutrition_value, self.good_until)
        food.age = 0
        return food


def mapn(fn, lsts):
    res = ()
    newlst = []
    for i in range(len(lsts[0])):
        sub = []
        for j in range(len(lsts)):
            sub.append(lsts[j][i])
        newlst.append(sub)

    for sub in newlst:
        print(sub)
        res += (tuple(fn(*sub)),)
     
    return res

    ##alt
    return tuple(map(fn, *lsts))
