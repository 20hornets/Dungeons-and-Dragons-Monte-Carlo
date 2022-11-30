import math
import statistics as stat
import random

class Combat():
    total_damage = []
    def __init__(self, attack_count, spell_level, divine_smite):
        self.attack_count = attack_count
        self.spell_level = spell_level
        self.divine_smite = divine_smite

    def Greatsword(self):
        damage = []
        for i in range(self.attack_count):
            dice = random.randint(1,6) + random.randint(1,6)
            damage.append(dice)
        return sum(damage)

    def Smite(self):
        damage = []
        for i in range(self.spell_level):
            dice = random.randint(1,8)
            damage.append(dice)
        return sum(damage)

    def DivineSmite(self, divine_smite):
        if divine_smite:
            damage = random.randint(1,8)
        return damage

#A work in progress here, trying to create a child class to calculate all the parent class objects
class Calculate(Combat):
    def __init__(self)
        Combat.__init__(self,attack_count,spell_level,divine_smite)
    pass

Vikter = Combat(2,4,1)
print(Vikter)

#Vikter = [Combat.Greatsword(2), Combat.Smite(4), Combat.DivineSmite(True)]



# damage_sim = []
# for i in range(10000):
#     Vikter = [Combat.Greatsword(2), Combat.Smite(4), Combat.DivineSmite(True)]
#     damage_sim.append(sum(Vikter))
# print(sum(damage_sim)/len(damage_sim))