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