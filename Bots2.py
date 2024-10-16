import random

class Spellmaster:
    name = "Spellmaster"
    def turn(self, my_life, other_life):
        threshold = 6
        if other_life >= threshold:
            return dict(accuracy = 4, power = 4, defense = 2)
        if other_life < threshold:
            return dict(accuracy = 7, power = 2, defense = 1)


class Jay:
    name = "jay"
    def turn(self, my_life, other_life):
        return dict(accuracy = 3, power = 4, defense = 3)


class Rand:
    name = "Random Man"
    def turn(self, my_life, other_life):
        accuracy = random.randint(1,9)
        offense = random.randint(0,10-accuracy)
        defense = 10 - accuracy - offense
        return dict( accuracy = accuracy, power = offense, defense = defense)

class Power:
    name = "power"
    def turn(self, my_life, other_life):
        return dict(accuracy = 1,power = 9, defense = 0)

class DragonKiller:
    name = "DragonKiller"
    def turn(self, my_life, other_life):
        if my_life >= 15:
            return dict(accuracy = 4, power = 3, defense = 3)
        if my_life < 15:
            return dict(accuracy = 4, power = 5, defense = 1)

class Dragon:
    name = "Dragon"
    def turn(self, my_life, other_life):
        if my_life >= 15:
            return dict(accuracy = 6, power = 3, defense = 1)
        if my_life < 15:
            return dict(accuracy = 5, power = 1, defense = 4)

class Accuracy:
    name = "Accuracy"
    def turn(self, my_life, other_life):
        return dict(accuracy = 9, power = 1, defense = 0)

class Rice:
    name = "Rnice"
    def turn(self, my_life, other_life):
            return dict(accuracy = 5, power = 5, defense = 0)

class Knight:
    name = "Knight"
    def turn(self, my_life, other_life):
        return dict(accuracy = 4, power = 3, defense = 3)

class Megaman:
    name = "megaman"
    def turn(self, my_life, other_life):
        return dict(accuracy = 3, power = 4, defense = 3)

class Defense:
    name = "defense"
    def turn(self, my_life, other_life):
            return dict(accuracy = 1, power = 1, defense = 8)


class Smart:
     name = "Mega computer"
     mine = []
     other = []
     change = []
     def turn(self, my_life, other_life):
         self.mine.append(my_life)
         self.other.append(other_life)
         p = dict(accuracy = 9, power = 1, defense = 0)
         if len(self.mine) > 1:
             self.change.append(self.mine[-2] - self.mine[-1])
             avg = sum(self.change)/len(self.change)
             print(avg)

             if max(self.change) >= 5:
                 print("other = power")
                 p = dict(accuracy = 7, power = 3, defense = 0)


             if self.change.count(3) > 0 or self.change.count(4) > 0:
                print("other = avrege")
                p = dict(accuracy = 5, power = 4, defense = 1)

             if self.change.count(1) > self.change.count(0) or self.change.count(2) > self.change.count(0):
                 print("other = accuracy")
                 p = dict(accuracy = 6, power = 3, defense = 1)

             if self.change.count(0) > self.change.count(1) + self.change.count(2):
                print("other = defense")
                p = dict(accuracy = 5, power = 3, defense = 2)


             if avg >= 1.8:
                 p["accuracy"] -= 2
                 p["power"] -= 1
                 p["defense"] += 3

             if my_life < 15:
                 p["accuracy"] += 1
                 p["power"] -= 1



         return p