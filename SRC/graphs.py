import numpy as pd
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import functions as fn 

#BE SURE TO EDIT FIG SAVE - APPARENTLY NOT A FUNCTION

def plot_sort_census_estimate_highest(df, est_name):

    fig, ax = plt.subplots(figsize=(8,4))
    county_name = fn.sort_census_estimate_highest(df)['County_Name']
    print(county_name)
    name = fn.sort_census_estimate_highest(df).columns[2]
    print(name)
    census_tract_est = fn.sort_census_estimate_highest(df)[name]
    print(census_tract_est)
    ax.bar(county_name, census_tract_est, color='salmon')
    ax.set_title(f'Highest {est_name} Estimates')
    ax.set_xlabel("Counties", size=11)
    ax.set_ylabel("Estimated Frequency Rate in %")
    plt.tight_layout()
    plt.show();



def plot_sort_census_estimate_lowest(df, est_name_1):
    
    fig, ax = plt.subplots(figsize=(8,4))
    county_name = fn.sort_census_estimate_lowest(df)['County_Name']
    name = fn.sort_census_estimate_lowest(df).columns[2]
    census_tract_est = fn.sort_census_estimate_lowest(df)[name]
    ax.bar(county_name, census_tract_est, color='lightblue')
    ax.set_title(f'Lowest {est_name_1} Estimates')
    ax.set_xlabel("Counties", size=11)
    ax.set_ylabel("Estimated Frequency Rate in %")
    plt.tight_layout()
    plt.show();



def plot_census_estimate(df, name):
    census_est = df.columns[6]
    state_est_col = df.columns[11]
    df['state_estimate'] = df[state_est_col].str.extract('(\d*\.\d+|\d+)', expand=False).astype(float)
    regional_est_col = df.columns[12]
    fig, axs = plt.subplots(figsize=(8,5))
    x = df[census_est]
    t = df[regional_est_col]
    axs.hist(x, bins=50, color='lightblue', edgecolor='navy')
    axs.axvline(df['state_estimate'][0], color='salmon', label='State Census Level', linewidth=3)
    axs.set_xlabel(f'Estimated {name} Rate', size=13)
    axs.set_ylabel('Frequency', size=12)
    axs.set_title(f'{name} Survey Estimate Distribution', size=16)
    plt.legend()
    plt.tight_layout()
    plt.show();


def plot_violin_adults(df1, df1_name, df2, df2_name, df3, df3_name):

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
    # Plot violin plot on axes 1
    violin_plot1 = ax1.violinplot(df1['Adult_Population_Age18_and_over'], showmedians=True)
    ax1.set_title(f'{df1_name}')
    ax1.set_ylabel('Adults per Census')
    # Plot violin plot on axes 2
    violin_plot2= ax2.violinplot(df2['Adult_Population_Age18_and_over'], showmedians=True)
    ax2.set_title(f'{df2_name}')
    # Plot violin plot on axes 3
    violin_plot3= ax3.violinplot(df3['Adult_Population_Age18_and_over'], showmedians=True)
    ax3.set_title(f'{df3_name}')
    plt.suptitle('Distribution of County Sample Sizes')
    
    for pc in violin_plot1['bodies']:
        pc.set_facecolor('teal')
        pc.set_edgecolor('black')
        plt.tight_layout()
    for pc in violin_plot2['bodies']:
        pc.set_facecolor('teal')
        pc.set_edgecolor('black')
        plt.tight_layout()
    for pc in violin_plot3['bodies']:
        pc.set_facecolor('teal')
        pc.set_edgecolor('black')
        plt.tight_layout()
    plt.show()

####need to add a save figure 



if __name__ == '__main__':
    
    obesity = pd.read_csv('Obesity_in_Adults_-_CDPHE_Community_Level_Estimates_(Census_Tracts) .csv')
    overweight = pd.read_csv('Overweight_and_Obese_Adults_-_CDPHE_Community_Level_Estimates_(Census_Tracts).csv')
    diabetes = pd.read_csv('Diabetes_in_Adults_-_CDPHE_Community_Level_Estimates__Census_Tracts_.csv')

    print(fn.sort_census_estimate_highest(obesity))

    #print(plot_sort_census_estimate_highest(obesity, 'Obesity'))
    #print(plot_sort_census_estimate_highest(overweight, 'Overweight'))
    #print(plot_sort_census_estimate_highest(diabetes, 'Diabetes'))
    print(plot_census_estimate(obesity, 'Obesity'))
    print(plot_census_estimate(obesity, 'Overweight'))
    print(plot_census_estimate(obesity, 'Diabetes'))
    print(plot_violin_adults(obesity, "Obesity", overweight, "Overweight", diabetes, "Diabetes"))