import pandas as pd
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


#print(weapon_df)

def WeaponChoice():
    features = {
        'light':0, 'finesse':0, 'thrown':0, 'two_handed':0,
        'versatile':0, 'heavy':0, 'reach':0, 'special':0,
        'ammunition':0, 'loading':0, 'dice_count':0, 'dmg':0
    }
    while True:
        #take an integer value that corresponds with the name of a weapon for all weapons
        wpn = int(input("(HELP returns a list of the armory)\n Choose a weapon index integer: "))
        if wpn == 'help':
            c = 0
            for i in weapon_df.columns:
                print(f'{i} \t\t {c}')
                c = c+1
        else:
            stat_clip = []
            x = weapon_df.iloc[0:12, wpn]
            for i in x:
                stat_clip.append(i)
            #print(stat_clip)
            light, finesse, thrown, two_handed, versatile, heavy, reach, special, ammunition, loading, dice_count, dmg = stat_clip
            return stat_clip
            break


#WeaponChoice()
#stat_loader = []
stat_loader = WeaponChoice()
print(stat_loader)