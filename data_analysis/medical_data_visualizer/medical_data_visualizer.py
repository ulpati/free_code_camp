import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# import data
df = pd.read_csv('medical_examination.csv')

# add 'overweight' column
df['overweight'] = (df['weight']/((df['height']/100)**2)>25).astype(int)

# normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1
df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)

# draw Categorical Plot
def draw_cat_plot():
    # create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()).rename(columns={'value': 'total'}).reset_index()
    
    # draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')

    # get the figure for the output
    fig = g.figure

    # do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# draw Heat Map
def draw_heat_map():
    # clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # calculate the correlation matrix
    corr = df_heat.corr()

    # generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.5, cmap='coolwarm', center=0, square=True, cbar_kws={'shrink': .5})

    # do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig