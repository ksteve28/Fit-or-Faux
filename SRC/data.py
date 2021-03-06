import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy.stats as stats 

#clean up this - this doesn't work 
#def import_data(df_name, df_file):
    
   # return df_name = pd.read_csv('df_file')

def null_data(df):
    return df.isnull().sum().sum()

def clean_nulls(df):
    return df.dropna(how='any', inplace=True)

def sort_census_estimate_highest(df):
    name = df.columns[6]
    return df.iloc[:, [3,4,6,9,11]].sort_values([name], ascending=[False]).head(6)

def sort_census_estimate_lowest(df):
    name = df.columns[6]
    return df.iloc[:, [3,4,6,9,11]].sort_values([name], ascending=[True]).head(6)

"""
Due to the structure of column additions the following lines of code add columns and are in congruence
to the way they were written. If you do not import the functions moving from regional to state it is
possible they will not run appropriately.
"""

def regional_estimate(df):
    '''
    The regional estimate data is designed to take the difference between the
    census tract estimate minus the regional estimate data and sort in descneding
    order. 

    The regional estimate data is formatted into as string therefore we must
    isolate the value in order to compare it to the census data.
     '''
    estimate_col = df.columns[6]
    reg_est_col = df.columns[9]
    df['reg_estimate'] = df[reg_est_col].str.extract('(\d*\.\d+|\d+)', expand=False).astype(float)
    df['reg_est_difference'] = df[estimate_col] - df['reg_estimate']
    return df.iloc[:, [3,6,9,11,13]].sort_values(['reg_est_difference'], ascending=[False]).head(10)


def state_estimate(df):
    '''
    The state estimate data is designed to take the difference between the
    census tract estimate minus the state estimate data and sort in descneding
    order. 
    The state estimate data is formatted into as string therefore we must
    isolate the value in order to compare it to the census data.
     '''
    estimate_col = df.columns[6]
    state_est_col = df.columns[11]
    df['state_estimate'] = df[state_est_col].str.extract('(\d*\.\d+|\d+)', expand=False).astype(float)
    df['state_est_difference'] = df[estimate_col] - df['state_estimate']
    return df.iloc[:, [3,6,9,11,15]].sort_values([estimate_col], ascending=[False]).head(10)


def find_age_mm(df):
    return df.iloc[:, 4].agg(['median', 'mean'])

def grouping_counties_desc(df):
    return df.groupby('County_Name').agg('count').sort_values('OBJECTID', ascending=False)

def grouping_counties_desc(df):
    return df.groupby('County_Name').agg('count').sort_values('OBJECTID', ascending=True)

if __name__ == '__main__':

    obesity = pd.read_csv('Obesity_in_Adults_-_CDPHE_Community_Level_Estimates_(Census_Tracts) .csv')
    overweight = pd.read_csv('Overweight_and_Obese_Adults_-_CDPHE_Community_Level_Estimates_(Census_Tracts).csv')
    diabetes = pd.read_csv('Diabetes_in_Adults_-_CDPHE_Community_Level_Estimates__Census_Tracts_.csv')

    print(overweight)