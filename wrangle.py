##### acquire animal crossing new horizon csv#######

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from env import get_db_url
import os
from sklearn.model_selection import train_test_split

# default pandas decimal number display format
pd.options.display.float_format = '{:20,.2f}'.format
from sklearn.preprocessing import MinMaxScaler


def get_acnh_data():
    filename = 'villagers.csv'

    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col = 0)
        return df



def successful(tier):
    if tier == 1 or tier == 2 or tier == 3:
        return 1
    else:
        return 0



    
def prep_acnh_data(df):
    columns = ['birthday', 'catchphrase', 'wallpaper', 'flooring', 'filename', 'furniture_list', 'unique_entry_id']
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace( ' ' , '_')
    df.drop(columns,inplace = True, axis = 1)
    df["is_successful"] = df["tier"].apply(lambda tier: successful(tier))
    df = df.rename(columns={'rank':'position'})
    return df



