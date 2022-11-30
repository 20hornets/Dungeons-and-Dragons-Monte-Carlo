import pandas as pd
import random
pd.set_option('display.max_columns', 85)
import numpy as np
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
wpn = -13
stat_clip = []
x = weapon_df.iloc[0:12, wpn]
for i in x:
    stat_clip.append(i)

def Damage(stat_clip):
    num_dice = stat_clip[-2]
    dmg_dice = stat_clip[-1]
    wpn_dmg1 = random.randint(1, dmg_dice)
    if num_dice > 1:
        wpn_dmg2 = random.randint(1, dmg_dice)
        wpn_dmg1 = wpn_dmg1 + wpn_dmg2
    return wpn_dmg1

Damage(stat_clip)