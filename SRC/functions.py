import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy.stats as stats 

#clean up this - this doesn't work 
#def import_data(df_name, df_file):
    
   # return df_name = pd.read_csv('df_file')

def null_data(df):
    """" To determine if there is nulls in the data """"
    return df.isnull().sum().sum()

def clean_nulls(df):
    return df.dropna(how='any', inplace=True)

def sort_census_estimate_highest(df):
    """This function creates a new column in order to plot later on and primary function is
    to return the highest census estimates in each individual census tract. """
    df['census_tract'] = df['Census_Tract_Name'].str.extract('(\d*\.\d+|\d+)', expand=False)
    df['county_name_tract'] = df['County_Name'] + ' ' + df['census_tract']
    name = df.columns[6]
    return df.iloc[:, [3,4,6,9,11,13]].sort_values([name], ascending=[False]).head(6)

def sort_census_estimate_lowest(df): 
    """This function creates a new column in order to plot later on and primary function is
    to return the lowest census estimates in each individual census tract. """
    df['census_tract'] = df['Census_Tract_Name'].str.extract('(\d*\.\d+|\d+)', expand=False)
    df['county_name_tract'] = df['County_Name'] + ' ' + df['census_tract']
    name = df.columns[6]
    return df.iloc[:, [3,4,6,9,11,13]].sort_values([name], ascending=[True]).head(6)

"""
Due to the structure of column additions the following lines of code add columns and are in congruence
to the way they were written. If you do not import the functions moving from regional to state it is
possible they will not run appropriately.
"""

def ave_estimate(df, is_diabetes=False):
    """This function allows for grouping counties and taking average census estimate
    through a weighted division of the counties. The diabetes dataset was not consistent
    with the other two data sets tested therefore needed to create a boolean function
    to direct to a different row to produce the desired results. """
    summed_estimate = df.groupby('County_Name').sum()
    grouped_counties = df.groupby('County_Name').count()
    average = summed_estimate / grouped_counties
    if is_diabetes:
        return average.iloc[:, [3]]
    return average.iloc[:, [5]]

def ave_estimate_asc(df, is_diabetes=False):
    summed_estimate = df.groupby('County_Name').sum()
    grouped_counties = df.groupby('County_Name').count()
    average = summed_estimate / grouped_counties
    if is_diabetes:
        return average.iloc[:, [3]].sort_values(['Diabetes_Census_Tract_Estimate'], ascending=True).head(6)
    return average.iloc[:, [5]].sort_values(['fill_in_data'], ascending=True).head(6)


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

    obesity = pd.read_csv('/Users/Kelly/Desktop/Fit-or-Faux/Datasets/Obesity_in_Adults_-_CDPHE_Community_Level_Estimates_(Census_Tracts) .csv')
    overweight = pd.read_csv('/Users/Kelly/Desktop/Fit-or-Faux/Datasets/Overweight_and_Obese_Adults_-_CDPHE_Community_Level_Estimates_(Census_Tracts).csv')
    diabetes = pd.read_csv('/Users/Kelly/Desktop/Fit-or-Faux/Datasets/Diabetes_in_Adults_-_CDPHE_Community_Level_Estimates__Census_Tracts_.csv')

    print(ave_estimate(diabetes))
    
    print(ave_estimate(overweight))
    
    print(sort_census_estimate_highest(overweight))
    print(sort_census_estimate_lowest(obesity))
    #print(state_estimate(obesity))

    #print(overweight)