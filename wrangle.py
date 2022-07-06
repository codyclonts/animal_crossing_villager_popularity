##### acquire animal crossing new horizon csv#######

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from sklearn.model_selection import train_test_split

# default pandas decimal number display format
pd.options.display.float_format = '{:20,.2f}'.format
from sklearn.preprocessing import MinMaxScaler


def get_acnh_data():
    ''' 
    This function acquires a local csv entitled villagers.csv and returns it as a dataframe. For this function to run, it must exist as a csv in the working directory
    '''
    filename = 'villagers.csv'

    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col = 0)
        return df



def successful(tier):
    ''' 
    This function takes information from the villagers.csv tier column and returns a 1 if the tier is a 1,2, or 3 or a 0 if it is anything else
    '''
    if tier == 1 or tier == 2 or tier == 3:
        return 1
    else:
        return 0



    
def prep_acnh_data(df):
    '''
    prepares the data from the villager.csv file by lower-casing column
    names and getting rid of spaces,  getting rid of the columns listed,
    creating an is successful tier based on the successful functio, 
    renaming the rank column to position, 
    and stripping any blank spaces.
    '''
    columns = ['birthday', 'catchphrase', 'wallpaper', 'flooring', 'filename', 'furniture_list', 'unique_entry_id']
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace( ' ' , '_')
    df.drop(columns,inplace = True, axis = 1)
    df["is_successful"] = df["tier"].apply(lambda tier: successful(tier))
    df = df.rename(columns={'rank':'position'})
    df['style_1'] = df.style_1.str.strip()
    df['color_1'] = df.color_1.str.strip()
    return df



def split_acnh_data(df):
    '''
    Takes in a cleaned acnh dataframe, splits it into train, validate and test subgroups and then returns those subgroups.
    Arguments: df - a cleaned pandas dataframe with the expected feature names and columns in the acnh dataset
    Return: train, validate, test - dataframes ready for the exploration and model phases.
    '''

    train_validate, test = train_test_split(df, test_size=.2, 
        random_state=17)

    train, validate = train_test_split(train_validate, test_size=.3, 
        random_state=17)
    return train, validate, test







####### encoding section #########

### encoding for each species ###



'''
These functions are used to create dummy variables for each of the species in the species column. 
These functions are to be used in conjunction with the encode species vars function listed below
'''



def is_cat(df):
    if df.species.lower() == 'cat':
        return 1
    else:
        return 0


def is_rhino(df):
    if df.species.lower() == 'rhino':
        return 1
    else:
        return 0


def is_squirrel(df):
    if df.species.lower() == 'squirrel':
        return 1
    else:
        return 0


def is_deer(df):
    if df.species.lower() == 'deer':
        return 1
    else:
        return 0


def is_rabbit(df):
    if df.species.lower() == 'rabbit':
        return 1
    else:
        return 0


def is_octopus(df):
    if df.species.lower() == 'octopus':
        return 1
    else:
        return 0


def is_cub(df):
    if df.species.lower() == 'cub':
        return 1
    else:
        return 0


def is_goat(df):
    if df.species.lower() == 'goat':
        return 1
    else:
        return 0


def is_duck(df):
    if df.species.lower() == 'duck':
        return 1
    else:
        return 0


def is_wolf(df):
    if df.species.lower() == 'wolf':
        return 1
    else:
        return 0


def is_hamster(df):
    if df.species.lower() == 'hamster':
        return 1
    else:
        return 0


def is_dog(df):
    if df.species.lower() == 'dog':
        return 1
    else:
        return 0


def is_sheep(df):
    if df.species.lower() == 'sheep':
        return 1
    else:
        return 0


def is_frog(df):
    if df.species.lower() == 'frog':
        return 1
    else:
        return 0



def is_ostrich(df):
    if df.species.lower() == 'ostrich':
        return 1
    else:
        return 0


def is_penguin(df):
    if df.species.lower() == 'penguin':
        return 1
    else:
        return 0


def is_horse(df):
    if df.species.lower() == 'horse':
        return 1
    else:
        return 0

def is_eagle(df):
    if df.species.lower() == 'eagle':
        return 1
    else:
        return 0


def is_elephant(df):
    if df.species.lower() == 'elephant':
        return 1
    else:
        return 0


def is_koala(df):
    if df.species.lower() == 'koala':
        return 1
    else:
        return 0


def is_mouse(df):
    if df.species.lower() == 'mouse':
        return 1
    else:
        return 0


def is_pig(df):
    if df.species.lower() == 'pig':
        return 1
    else:
        return 0


def is_alligator(df):
    if df.species.lower() == 'alligator':
        return 1
    else:
        return 0


def is_bear(df):
    if df.species.lower() == 'bear':
        return 1
    else:
        return 0


def is_tiger(df):
    if df.species.lower() == 'tiger':
        return 1
    else:
        return 0


def is_anteater(df):
    if df.species.lower() == 'anteater':
        return 1
    else:
        return 0


def is_monkey(df):
    if df.species.lower() == 'monkey':
        return 1
    else:
        return 0


def is_lion(df):
    if df.species.lower() == 'lion':
        return 1
    else:
        return 0


def is_cow(df):
    if df.species.lower() == 'cow':
        return 1
    else:
        return 0


def is_hippo(df):
    if df.species.lower() == 'hippo':
        return 1
    else:
        return 0


def is_gorilla(df):
    if df.species.lower() == 'gorilla':
        return 1
    else:
        return 0


def is_kangaroo(df):
    if df.species.lower() == 'kangaroo':
        return 1
    else:
        return 0


def is_bird(df):
    if df.species.lower() == 'bird':
        return 1
    else:
        return 0


def is_chicken(df):
    if df.species.lower() == 'chicken':
        return 1
    else:
        return 0


def is_bull(df):
    if df.species.lower() == 'bull':
        return 1
    else:
        return 0





def encode_species_vars(df): 
    '''
    Takes in the information from the species dummy variables functions listed above to create new columns. 
    These columns are encoded variables used for modeling. 
    '''
    df['is_squirrel'] = df.apply(is_squirrel, axis = 1)

    df['is_cat'] = df.apply(is_cat, axis = 1)

    df['is_deer'] = df.apply(is_deer, axis = 1)

    df['is_rabbit'] = df.apply(is_rabbit, axis = 1)

    df['is_octopus'] = df.apply(is_octopus, axis = 1)

    df['is_cub'] = df.apply(is_cub, axis = 1)

    df['is_goat'] = df.apply(is_goat, axis = 1)

    df['is_duck'] = df.apply(is_duck, axis = 1)

    df['is_wolf'] = df.apply(is_wolf, axis = 1)

    df['is_rhino'] = df.apply(is_rhino, axis = 1)

    df['is_hamster'] = df.apply(is_hamster, axis = 1)

    df['is_dog'] = df.apply(is_dog, axis = 1)

    df['is_sheep'] = df.apply(is_sheep, axis = 1)

    df['is_frog'] = df.apply(is_frog, axis = 1)

    df['is_ostrich'] = df.apply(is_ostrich, axis = 1)

    df['is_penguin'] = df.apply(is_penguin, axis = 1)

    df['is_horse'] = df.apply(is_horse, axis = 1)

    df['is_eagle'] = df.apply(is_eagle, axis = 1)

    df['is_elephant'] = df.apply(is_elephant, axis = 1)

    df['is_koala'] = df.apply(is_koala, axis = 1)

    df['is_mouse'] = df.apply(is_mouse, axis = 1)

    df['is_pig'] = df.apply(is_pig, axis = 1)

    df['is_alligator'] = df.apply(is_alligator, axis = 1)

    df['is_bear'] = df.apply(is_bear, axis = 1)

    df['is_tiger'] = df.apply(is_tiger, axis = 1)

    df['is_anteater'] = df.apply(is_anteater, axis = 1)

    df['is_monkey'] = df.apply(is_monkey, axis = 1)

    df['is_lion'] = df.apply(is_lion, axis = 1)

    df['is_cow'] = df.apply(is_cow, axis = 1)

    df['is_hippo'] = df.apply(is_hippo, axis = 1)

    df['is_gorilla'] = df.apply(is_gorilla, axis = 1)

    df['is_kangaroo'] = df.apply(is_kangaroo, axis = 1)

    df['is_bird'] = df.apply(is_bird, axis = 1)

    df['is_chicken'] = df.apply(is_chicken, axis = 1)

    df['is_bull'] = df.apply(is_bull, axis = 1)

    return df



##### encode the personalities ######

'''
These functions are used to create dummy variables for each of the personalities in the personality column. 
These functions are to be used in conjunction with the encode personality vars function listed below
'''

def is_smug(df):
    if df.personality.lower() == 'smug':
        return 1
    else:
        return 0


def is_peppy(df):
    if df.personality.lower() == 'peppy':
        return 1
    else:
        return 0


def is_lazy(df):
    if df.personality.lower() == 'lazy':
        return 1
    else:
        return 0


def is_snooty(df):
    if df.personality.lower() == 'snooty':
        return 1
    else:
        return 0


def is_normal(df):
    if df.personality.lower() == 'normal':
        return 1
    else:
        return 0



def is_jock(df):
    if df.personality.lower() == 'jock':
        return 1
    else:
        return 0


def is_big_sister(df):
    if df.personality.lower() == 'big sister':
        return 1
    else:
        return 0


def is_cranky(df):
    if df.personality.lower() == 'cranky':
        return 1
    else:
        return 0





def encode_personality_vars(df):
    '''
    Takes in the information from the personality dummy variables functions listed above to create new columns. 
    These columns are encoded variables used for modeling. 
    '''
    df['is_smug'] = df.apply(is_smug, axis = 1)

    df['is_peppy'] = df.apply(is_peppy, axis = 1)

    df['is_lazy'] = df.apply(is_lazy, axis = 1)

    df['is_snooty'] = df.apply(is_snooty, axis = 1)

    df['is_normal'] = df.apply(is_normal, axis = 1)

    df['is_jock'] = df.apply(is_jock, axis = 1)

    df['is_big_sister'] = df.apply(is_big_sister, axis = 1)

    df['is_cranky'] = df.apply(is_cranky, axis = 1)

    return df



###### encode style_1 ######
'''
These functions are used to create dummy variables for each of the styles in the style_1 column. 
These functions are to be used in conjunction with the encode style vars function listed below
'''
def is_elegant(df):
    if df.style_1.lower() == 'elegant':
        return 1
    else:
        return 0

def is_simple(df):
    if df.style_1.lower() == 'simple':
        return 1
    else:
        return 0

def is_gorgeous(df):
    if df.style_1.lower() == 'gorgeous':
        return 1
    else:
        return 0


def is_cute(df):
    if df.style_1.lower() == 'cute':
        return 1
    else:
        return 0


def is_cool(df):
    if df.style_1.lower() == 'cool':
        return 1
    else:
        return 0


def is_active(df):
    if df.style_1.lower() == 'active':
        return 1
    else:
        return 0



def encode_style_vars(df):
    '''
    Takes in the information from the style dummy variables functions listed above to create new columns. 
    These columns are encoded variables used for modeling. 
    '''
    df['is_elegant'] = df.apply(is_elegant, axis = 1)

    df['is_simple'] = df.apply(is_simple, axis = 1)

    df['is_gorgeous'] = df.apply(is_gorgeous, axis = 1)

    df['is_cute'] = df.apply(is_cute, axis = 1)

    df['is_cool'] = df.apply(is_cool, axis = 1)

    df['is_active'] = df.apply(is_active, axis = 1)

    return df 





#### encode hobby column #####
    '''
    These functions are used to create dummy variables for each of the hobbies in the hobby column. 
    These functions are to be used in conjunction with the encode hobby vars function listed below
    '''
def is_music(df):
    if df.hobby.lower() == 'music':
        return 1
    else:
        return 0


def is_nature(df):
    if df.hobby.lower() == 'nature':
        return 1
    else:
        return 0


def is_education(df):
    if df.hobby.lower() == 'education':
        return 1
    else:
        return 0


def is_fashion(df):
    if df.hobby.lower() == 'fashion':
        return 1
    else:
        return 0

def is_play(df):
    if df.hobby.lower() == 'play':
        return 1
    else:
        return 0

def is_fitness(df):
    if df.hobby.lower() == 'fitness':
        return 1
    else:
        return 0




def encode_hobby_vars(df):
    '''
    Takes in the information from the style dummy variables functions listed above to create new columns. 
    These columns are encoded variables used for modeling.    
    '''
    df['is_music'] = df.apply(is_music, axis = 1)

    df['is_nature'] = df.apply(is_nature, axis = 1)

    df['is_education'] = df.apply(is_education, axis = 1)

    df['is_fashion'] = df.apply(is_fashion, axis = 1)

    df['is_play'] = df.apply(is_play, axis = 1)

    df['is_fitness'] = df.apply(is_fitness, axis = 1)

    return df 


####### encode gender ######

    '''
    This function are used to create dummy variables for each of the genders in the gender column. 
    These functions are to be used in conjunction with the encode gender vars function listed below
    '''

def is_female(df):
    if df.gender.lower() == 'female':
        return 1
    else:
        return 0



def encode_gender_vars(df): 
    '''
    Takes in the information from the gender dummy variables function listed above to create new columns. 
    These columns are encoded variables used for modeling.    
    '''
    df['is_female'] = df.apply(is_female, axis = 1)

    return df 




###### encode colors ########

    '''
    This function are used to create dummy variables for each of the colors in the color_1 column. 
    These functions are to be used in conjunction with the encode color_1 vars function listed below
    '''

def is_beige(df):
    if df.color_1.lower() == 'beige':
        return 1
    else:
        return 0


def is_white(df):
    if df.color_1.lower() == 'white':
        return 1
    else:
        return 0


def is_black(df):
    if df.color_1.lower() == 'black':
        return 1
    else:
        return 0


def is_light_blue(df):
    if df.color_1.lower() == 'light blue':
        return 1
    else:
        return 0


def is_colorful(df):
    if df.color_1.lower() == 'colorful':
        return 1
    else:
        return 0


def is_gray(df):
    if df.color_1.lower() == 'gray':
        return 1
    else:
        return 0


def is_pink(df):
    if df.color_1.lower() == 'pink':
        return 1
    else:
        return 0



def is_yellow(df):
    if df.color_1.lower() == 'yellow':
        return 1
    else:
        return 0


def is_red(df):
    if df.color_1.lower() == 'red':
        return 1
    else:
        return 0




def is_orange(df):
    if df.color_1.lower() == 'orange':
        return 1
    else:
        return 0





def is_purple(df):
    if df.color_1.lower() == 'purple':
        return 1
    else:
        return 0




def is_green(df):
    if df.color_1.lower() == 'green':
        return 1
    else:
        return 0



def is_brown(df):
    if df.color_1.lower() == 'brown':
        return 1
    else:
        return 0



def is_blue(df):
    if df.color_1.lower() == 'blue':
        return 1
    else:
        return 0



def is_aqua(df):
    if df.color_1.lower() == 'aqua':
        return 1
    else:
        return 0





def encode_color_1_vars(df):
    '''
    Takes in the information from the color dummy variables function listed above to create new columns. 
    These columns are encoded variables used for modeling.    
    '''
    df['is_beige'] = df.apply(is_beige, axis = 1)

    df['is_white'] = df.apply(is_white, axis = 1)

    df['is_black'] = df.apply(is_black, axis = 1)

    df['is_light_blue'] = df.apply(is_light_blue, axis = 1)

    df['is_colorful'] = df.apply(is_colorful, axis = 1)

    df['is_gray'] = df.apply(is_gray, axis = 1)

    df['is_pink'] = df.apply(is_pink, axis = 1)

    df['is_yellow'] = df.apply(is_yellow, axis = 1)

    df['is_red'] = df.apply(is_red, axis = 1)

    df['is_orange'] = df.apply(is_orange, axis = 1)

    df['is_purple'] = df.apply(is_purple, axis = 1)

    df['is_green'] = df.apply(is_green, axis = 1)

    df['is_brown'] = df.apply(is_brown, axis = 1)

    df['is_blue'] = df.apply(is_blue, axis = 1)

    df['is_aqua'] = df.apply(is_aqua, axis = 1)

    return df 






def encode_all_vars(df):
    '''
    Takes in functions used to encode the gender, hobby, style_1, species, and personality columns and creates new columns
    based on the encoded values. Drops unencoded columns. Returns dataframe to be used for modeling.
    '''
    unencoded_columns = ['position', 'tier', 'species', 'gender', 'personality', 'hobby', 'favorite_song', 'style_1', 'style_2', 'color_1', 'color_2']

    df = encode_gender_vars(df)

    df = encode_hobby_vars(df)

    df = encode_style_vars(df)

    df = encode_species_vars(df)

    df = encode_personality_vars(df) 

    df.drop(unencoded_columns,inplace = True, axis = 1)

    return df 
