import pandas as pd
import random
import time
import statistics as stat
import pdb
'''create a dataframe that contains a boolean value for each weapon attribute
then also include the number of die and which die the weapons do for damage
use this table to feed information into functions and classes to consolidate 
data'''

'''
Updates still needed
1) make sure strength affects tohit and damage
2) add magic weapon functionality
3) make seperate lists for raw damage and tohit adjust damage, if there is a really skewed hit% the variance will skew in 
an odd way
4) make the stat report function more robust, needs to run graphs in a clean way also
'''

weapon_df = pd.DataFrame({'club':           [1,0,0,0,0,0,0,0,0,0,1,4],
                          'dagger':         [1,1,1,0,0,0,0,0,0,0,1,4],
                          'greatclub':      [0,0,0,1,0,0,0,0,0,0,1,8],
                          'handaxe':        [1,0,1,0,0,0,0,0,0,0,1,6],
                          'javelin':        [0,0,1,0,0,0,0,0,0,0,1,6],
                          'light_hammer':   [1,0,1,0,0,0,0,0,0,0,1,4],
                          'mace':           [0,0,0,0,0,0,0,0,0,0,1,6],
                          'quarterstaff':   [0,0,0,0,0,0,0,0,0,0,1,6],
                          'sickle':         [1,0,0,0,0,0,0,0,0,0,1,4],
                          'spear':          [0,0,1,0,0,0,0,0,0,0,1,6],
                          'light_crossbow': [0,0,0,1,0,0,0,0,1,1,1,8],
                          'dart':           [0,1,1,0,0,0,0,0,0,0,1,4],
                          'shortbow':       [0,0,0,1,0,0,0,0,1,0,1,6],
                          'sling':          [0,0,0,0,0,0,0,0,0,1,1,4],
                          'battleaxe':      [0,0,0,0,1,0,0,0,0,0,1,8],
                          'flail':          [0,0,0,0,0,0,0,0,0,0,1,8],
                          'glaive':         [0,0,0,1,0,1,1,0,0,0,1,10],
                          'greataxe':       [0,0,0,1,0,1,0,0,0,0,1,12],
                          'greatsword':     [0,0,0,1,0,1,0,0,0,0,2,6],
                          'halberd':        [0,0,0,1,0,1,1,0,0,0,1,10],
                          'lance':          [0,0,0,0,0,0,1,1,0,0,1,12],
                          'longsword':      [0,0,0,0,1,0,0,0,0,0,1,8],
                          'maul':           [0,0,0,1,0,1,0,0,0,0,2,6],
                          'morningstar':    [0,0,0,1,0,1,1,0,0,0,1,8],
                          'pike':           [0,0,0,1,0,1,1,0,0,0,1,10],
                          'rapier':         [0,1,0,0,0,0,0,0,0,0,1,8],
                          'scimitar':       [1,1,0,0,0,0,0,0,0,0,1,6],
                          'shortsword':     [1,1,0,0,0,0,0,0,0,0,1,6],
                          'trident':        [0,0,1,0,0,0,0,0,0,0,1,6],
                          'war_pick':       [0,0,0,0,0,0,0,0,0,0,1,8],
                          'warhammer':      [0,0,0,0,1,0,0,0,0,0,1,8],
                          'whip':           [0,1,0,0,0,0,1,0,0,0,1,4],
                          'blow_gun':       [0,0,0,0,0,0,0,0,1,1,1,1],
                          'hand_crossbow':  [1,0,0,0,0,0,0,0,1,1,1,6],
                          'heavy_crossbow': [0,0,0,0,0,1,0,0,1,1,1,10],
                          'longbow':        [0,0,0,0,1,0,1,0,1,1,1,8]},
                         index = ['light','finesse', 'thrown', 'two_handed',
                                  'versatile', 'heavy', 'reach', 'special',
                                  'ammunition', 'loading', 'dice_count','dmg'])
# print(weapon_df)
'''Create a function that chooses a weapon to simulate damage with from the dataframe'''
def WeaponChoice():
    while True:
        #take an integer value that corresponds with the name of a weapon for all weapons
        try:
            wpn = int(input("(0 returns a list of the armory)\nChoose a weapon index integer: "))
            if wpn == 0:
                c = 1
                for i in weapon_df.columns:
                    print(f"|{i: <20} {c}|")
                    c = c+1
            elif 0 >= wpn or wpn >= 37:
                print(f'Entered {wpn}, please enter a number between 1 and 36.')
            else:
                wpn = int(wpn)
                stat_clip = []
                x = weapon_df.iloc[0:12, wpn-1]
                for i in x:
                    stat_clip.append(i)
                light, finesse, thrown, two_handed, versatile, heavy, reach, special, ammunition, loading, dice_count, dmg = stat_clip
                # print(stat_clip)
                return stat_clip
        except ValueError:
            print("Please enter a valid integer between 0 and 36")

'''Create a function that accepts the single fixed input bonuses for simple simulation, i.e. a
same level analysis to get an idea of what combat looks like currently for example'''
def BonusCalc():
    armor_class = int(input("Enter fixed AC: "))
    adventuring_bonus = int(input("Enter fixed Adventuring Bonus: "))
    str_bonus = int(input("Enter fixed STR bonus: "))
    dex_bonus = int(input("Enter fixed DEX bonus: "))
    attks_per_rnd = int(input("Enter the number of attacks per round: "))
    smite_chk = int(input("Calculate smite damage also? "))
    if smite_chk == 1:
        spell_lvl = int(input("What level smite? "))
        divine_fury = int(input("Is divine fury active? "))
        if divine_fury == 1:
            spell_lvl = divine_fury + 1
        smite_chk = spell_lvl
    print('\nCalculating... ')
    return armor_class, adventuring_bonus, str_bonus, dex_bonus, attks_per_rnd, smite_chk

'''Calculate whether or not a swing connects and return True or False'''
def ToHit(AC=10, Adv_Bonus=0, STR=0, DEX=0):
    swing = random.randint(1, 20)
    eval = swing + Adv_Bonus + STR + DEX
    if eval >= AC:
        return True
    else:
        return False

'''Write a function that takes the weapon stat data and rolls the appropriate damage dice, this is a simple function
meant to be called anytime weapon damage is rolled call the last 2 elements of the stat_clip and load the numbers in 
here very simply, return a single damage output.'''
def Damage(stat_clip):
    num_dice = stat_clip[-2]
    dmg_dice = stat_clip[-1]
    wpn_dmg1 = random.randint(1, dmg_dice)
    if num_dice > 1:
        wpn_dmg2 = random.randint(1, dmg_dice)
        wpn_dmg1 = wpn_dmg1 + wpn_dmg2
    return wpn_dmg1

def RunStats(dmg_sim, raw_dmg):
    raw_title = "Damage data not adjusted for hit chance"
    raw_dmg_mean = stat.mean(raw_dmg)
    raw_dmg_var = stat.variance(raw_dmg)
    raw_dmg_dev = stat.stdev(raw_dmg)
    raw_dmg_upperCI = raw_dmg_mean + 2 * raw_dmg_dev
    raw_dmg_lowerCI = raw_dmg_mean - 2 * raw_dmg_dev
    sim_title = "Damage data adjusted for hit chance"
    dmg_sim_mean = stat.mean(dmg_sim)
    dmg_sim_var = stat.variance(dmg_sim)
    dmg_sim_dev = stat.stdev(dmg_sim)
    dmg_sim_upperCI = dmg_sim_mean + 2 * dmg_sim_dev
    dmg_sim_lowerCI = dmg_sim_mean - 2 * dmg_sim_dev
    print(f'\n{raw_title:^20}\n\nMean: {round(raw_dmg_mean,2): <20}\nVariance: {round(raw_dmg_var,2) : <20}\n'
          f'95% Confidence Interval:\n {round(raw_dmg_lowerCI,2): <15} {round(raw_dmg_mean,2): ^15}{round(raw_dmg_upperCI,2): < 20}')
    print(f'{sim_title:^20}\n\nMean: {round(dmg_sim_mean,2): <20}\nVariance: {round(dmg_sim_var,2): <20}\n'
          f'95% Confidence Interval:\n{round(dmg_sim_lowerCI,2): <15} {round(dmg_sim_mean,2): ^15}{round(dmg_sim_upperCI,2): < 20}')

'''create a function that accepts all functions that contribute to combat, make it verbose enough
 to hand having fixed value inputs, range inputs and default fixed inputs'''
def Combat():
    # FXorRNG = int(input("Would you like to do a single sim or range of sims? "))
    stat_clip = WeaponChoice()
    # print(stat_clip)
    armor_class, adventuring_bonus, str_bonus, dex_bonus, attks_per_rnd, smite_chk = BonusCalc()  # retrieve pertinent accuracy mods for tohit calculation
    dmg_sim = []        #damage being calculated with and without and misses factored in
    hit_sim = []        #accounting of all hits and misses as a boolean for probability and stat calcs
    start = time.time()
    for i in range(1000000):
        temp_dmg_list = []
        for j in range(attks_per_rnd):
            action = ToHit(AC=armor_class, Adv_Bonus=adventuring_bonus, STR=str_bonus, DEX=dex_bonus)  # retrieve inputs for a hit or miss -> bool
            if action:
                hit_sim.append(1)
                temp_dmg_list.append(Damage(stat_clip))
                if smite_chk:
                    smite_dmg = []
                    for k in range(smite_chk + 1):
                        smite = random.randint(1, 8)
                        smite_dmg.append(smite)
                    temp_dmg_list.append(sum(smite_dmg))
            else:
                temp_dmg_list.append(0)
                hit_sim.append(0)
        dmg_sim.append(sum(temp_dmg_list))
    # print(dmg_sim)
    finish = time.time()
    long_run_average = stat.mean(dmg_sim)
    raw_dmg = []
    for l in dmg_sim:
        if l != 0:
            raw_dmg.append(l)
    RunStats(dmg_sim, raw_dmg)
    print(f'Average hit chance: {sum(hit_sim) / len(hit_sim)}')
    print(f'\n{round(finish - start, 2)} seconds to compute.')
    # return stat.mean(dmg_sim)

    #elif we want a range with specific allocations at each step
    #else we want a range with linear range specifications


damage_simulation = Combat()

# print(damage_simulation)