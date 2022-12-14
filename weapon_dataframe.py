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
5) improve comments on what everything does
'''

''' The data frame weapon_df contains 12 elements for each weapon. The first 10 are booleans indicating whether or not
a certain characteristic is true. These characteristics can potentially alter if certain calculations are carried out. 
This will tend to impact combat only when the game mechanic called 'feats' or 'features' are implemented. The last two 
elements of the lists indicate first, the number of die, and second the die size for damage rolls. For example: [...,1,4]
indicates one 4 sided die will be rolled per weapon swing, [...,2,6] indicates a two 6 sided die will be rolled per weapon 
swing. The following ordered list corresponds with the aforementioned booleans as being true or false: 'light','finesse', 
'thrown', 'two_handed', 'versatile', 'heavy', 'reach', 'special', 'ammunition', 'loading', 'dice_count', 'dmg'
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

'''Create a function that accepts the single fixed input bonuses for simple simulation, check for certain conditions
from the user, ask if the following mechanics should be apart of the calculation or not, specifically from the paladin
class: Divine smite, (if so, what level divine smite), and divine fury. Later iterations of the program may do a class 
level check to provide these as true by default if a paladin of a certain level is true else do nothing'''
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

'''Calculate whether or not a swing connects and return True or False, Mathematically the False to hit will scale the 
damage rolled to zero but programmatically this should simply not roll to save on resources. This function takes into 
account all the factors entered by the user and includes them in the hit chance. Hit chance is calculated by rolling a
20 sided die and adding the characters strength or dexterity bonus, entered by the user, and the adventuring bonus,
another value entered by the user which is related to character level. If the sum of these components is equal to or 
greater than the armor class then there is a hit, and the calculation for damage may initiate otherwise, ToHit is false
and damage is not rolled.'''
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


'''
Once the simulation is run, we will pull in the lists of data and calculate all relevant statistics in this function.
The data should be cleanly formatted and give a comparative analysis of raw damage, that is unadjusted for hit probability,
and simulated damage, which is round by round damage with a hit probability factored in. This provides 2 important 
perspectives on damage calculations, knowing what a character's potential for damage is, and what the realistic outcome 
is. This is intended to provide the user for slightly more informative analysis when speccing a character out to determine
if a build is viable, or not, and whether the target armor class is the main contributing factor in the realistic damage 
calculation, or not. This is intended to provide some guidance implicitly for the user to tweak their build and optimize
damage output.
'''
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

'''create a master function that accepts all sub-functions which contribute to combat damage calculations, make it 
verbose enough to handle having fixed value inputs, range inputs and default fixed inputs.
This function should provide the following functionality to the user:
1) Query the weapon data frame for relevant damage metrics
2) Accept all relevant inputs for damage calculation
3) roll to hit
4) roll damage
5) retain hits misses and total damage on a per round basis in a list
6) report simulation time
7) report simulation statistics
'''
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