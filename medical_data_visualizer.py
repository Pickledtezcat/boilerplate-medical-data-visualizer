import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#continuing project

# Import data
df = pd.read_csv(
'medical_examination.csv')

print(df.iloc[0])

weight_series = df["weight"]
height_series = df["height"]
hm = height_series * 0.01

bmi = weight_series / (hm * hm)

# Add 'overweight' column
df['overweight'] = bmi > 25

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

cholesterol_series = df["cholesterol"]
gluc_series = df["gluc"]

cholesterol_series = cholesterol_series

df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars= ["cardio"], value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(kind="count", x="variable", hue="value", col="cardio", data=df_cat) 
        
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    blood_mask = df['ap_lo'] <= df['ap_hi']
    df.loc[blood_mask]
    h1 = df['height'] >= df['height'].quantile(0.025) 
    df.loc[h1]
    h2 = df['height'] <= df['height'].quantile(0.975)
    df.loc[h2]
    w1 = df['weight'] >= df['weight'].quantile(0.025)
    df.loc[w1]
    w2 = df['weight'] <= df['weight'].quantile(0.975)
    df.loc[w2]

    # Calculate the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    t_mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, mask=t_mask, vmax=0.3, center=0.09,square=True, cbar_kws = {'orientation' : 'horizontal'})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
