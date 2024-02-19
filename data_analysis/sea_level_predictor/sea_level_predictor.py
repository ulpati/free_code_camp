import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # create first line of best fit
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = list(range(1880, 2051))
    y_pred = [slope * x + intercept for x in x_pred]
    plt.plot(x_pred, y_pred, color='red', label='Best Fit Line (1880-2050)')

    # create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, *_= linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = list(range(2000, 2051))
    y_pred_recent = [slope_recent * x + intercept_recent for x in x_pred_recent]
    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (2000-2050)')

    # add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()