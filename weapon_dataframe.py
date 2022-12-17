import statistics
import pandas as pd
import random
import time
import statistics as stat
# import seaborn as sns
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
                    print(f"{i: <20} {c}")
                    c = c+1
            elif 0 >= wpn or wpn >= 37:
                print(f'Entered {wpn}, please enter a number between 1 and 36.')
            else:
                wpn = int(wpn)
                stat_clip = []
                x = weapon_df.iloc[0:12, wpn-1]
                for i in x:
                    stat_clip.append(i)
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

'''Define a function that will calculate smite damage and or divine fury, smite_chk will be a value of 0 if false or
greater to indicate spell level which reflects the damage calc.
'''
def Smite(smite_chk):
    smite_dmg = []
    for k in range(smite_chk + 1):
        smite = random.randint(1, 8)
        smite_dmg.append(smite)
    return sum(smite_dmg)

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

def ReportStats(raw_dmg, hit_dmg, hit_chc):
    # print(len(raw_dmg), len(hit_dmg), len(hit_chc))
    raw_dmg_mean = stat.mean(raw_dmg)
    hit_dmg_mean = stat.mean(hit_dmg)
    hit_chc_mean = stat.mean(hit_chc)

    raw_dmg_std = stat.stdev(raw_dmg)
    hit_dmg_std = stat.stdev(hit_dmg)
    hit_chc_std = stat.stdev(hit_chc)
    N_root = len(raw_dmg)**.5       #Use for raw and hit, they are always the same length as each other
    N_root_chc = len(hit_chc)

    # print(raw_dmg_std, hit_dmg_std, hit_chc_std)  #troubleshooting
    #CI calculate with square root of 10,000 as a fixed value, entered 100 to save resources
    raw_dmg_CI_upper = raw_dmg_mean + 1.96 * (raw_dmg_std / N_root)
    raw_dmg_CI_lower = raw_dmg_mean - 1.96 * (raw_dmg_std / N_root)

    hit_dmg_CI_upper = hit_dmg_mean + 1.96 * (hit_dmg_std / N_root)
    hit_dmg_CI_lower = hit_dmg_mean - 1.96 * (hit_dmg_std / N_root)

    #Hit chance pulls from a list of varied length and must adjust accordingly, need to assign
    #fixed values, may be worth just calculating the square root of N for code simplicity at the
    #expense of resources, will probably be very little if we preload the calc and assign the value
    hit_chc_CI_upper = hit_chc_mean + 1.96 * (hit_chc_std / N_root_chc)
    hit_chc_CI_lower = hit_chc_mean - 1.96 * (hit_chc_std / N_root_chc)

    return raw_dmg_mean, hit_dmg_mean, hit_chc_mean, \
           raw_dmg_CI_lower, raw_dmg_CI_upper, \
           hit_dmg_CI_lower,hit_dmg_CI_upper, \
           hit_chc_CI_lower, hit_chc_CI_upper


def ReportGraphs(x, y, z):
    pass

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
    stat_clip = WeaponChoice()
    armor_class, adventuring_bonus, str_bonus, dex_bonus, attks_per_rnd, smite_chk = BonusCalc()  # retrieve pertinent accuracy mods for tohit calculation
    raw_dmg = []            #accumulated, per round damage, regardless of weapon contact
    hit_dmg = []            #accumulated, per round damage, with regard to weapon contact
    hit_chc = []            #binomial hit chance list
    start = time.time()
    for i in range(100000):
        temp_raw_dmg = []   #accumulated dmg regardless of weapon contact, round by round the list is refreshed
        temp_hit_dmg = []   #accumulated dmg with regard to weapon contact, round by round the list is refreshed
        #temp_hit_chc = []   #accumulated boolean of whether or not weapon makes contact, round by round the list is refreshed
        for j in range(attks_per_rnd):
            # print(f'\nRaw attack number: {j+1}')          #troubleshooting
            x = Damage(stat_clip)
            if smite_chk:
                y = Smite(smite_chk)
                x = x + y
            temp_raw_dmg.append(x)
            # print(f' Temp Raw Damage: {temp_raw_dmg}')    #troubleshooting
            # print(f' Temp Hit Damage: {temp_hit_dmg}')    #troubleshooting
        for j in range(attks_per_rnd):
            # print(f'\nHit attack number: {j + 1}')        #troubleshooting
            action = ToHit(AC=armor_class, Adv_Bonus=adventuring_bonus, STR=str_bonus, DEX=dex_bonus)  # retrieve inputs for a hit or miss -> bool
            if action:
                hit_chc.append(1)
                x = Damage(stat_clip)
                if smite_chk:
                    y = Smite(smite_chk)
                    x = x + y
                temp_hit_dmg.append(x)
            else:
                hit_chc.append(0)
        temp_raw_dmgMean = sum(temp_raw_dmg)
        temp_hit_dmgMean = sum(temp_hit_dmg)
        raw_dmg.append(temp_raw_dmgMean), hit_dmg.append(temp_hit_dmgMean)

    raw_dmg_mean, hit_dmg_mean, hit_chc_mean, raw_dmg_CI_lower, raw_dmg_CI_upper, hit_dmg_CI_lower, hit_dmg_CI_upper, \
    hit_chc_CI_lower, hit_chc_CI_upper = ReportStats(raw_dmg, hit_dmg, hit_chc)
    # print(hit_dmg_CI_lower, hit_dmg_CI_upper)
    print(f'Raw Mean: {round(raw_dmg_mean,2)}'
          f'\nHit Mean: {round(hit_dmg_mean,2)}'
          f'\nHit Probability: {round(hit_chc_mean*100,2)}%'
          f'\nRaw CI:\n {round(raw_dmg_CI_lower,2)},{round(raw_dmg_CI_upper,2)}'
          f'\nHit CI:\n {round(hit_dmg_CI_lower,2)},{round(hit_dmg_CI_upper,2)}'
          f'\nHit Probability CI:\n {round(hit_chc_CI_lower*100,4)}%,{round(hit_chc_CI_upper*100,4)}%')
    finish = time.time()
    print(f'\nRuntime:\n {round(finish - start,6)} seconds.')
    #return raw_dmg, hit_dmg, hit_prob

damage_simulation = Combat()

