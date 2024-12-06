# -*- coding: utf-8 -*-

from hockey_rink import NHLRink
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

data = pd.read_csv('nhl_shot_data.csv')

data = data.rename(columns={"details.zoneCode": "ZoneCode", "details.shotType": "ShotType", 
                     "details.reason": "Reason"})

categorical_columns = ["homeTeamDefendingSide", "typeDescKey", 
                       "ZoneCode", "ShotType", 
                       "Reason"]

for i, column in enumerate(categorical_columns):
    plt.figure(figsize=(15, 10))
    sns.countplot(data=data, x=column, hue=column, palette="deep", legend=False)
    plt.title(f"Distribution of {column}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"Distribution of {column}.png")
    
    rink = NHLRink()
    fig, ax = plt.subplots(figsize=(12, 8))
    rink.draw(ax=ax)
    sns.scatterplot(
        data=data,
        x="details.xCoord",
        y="details.yCoord",
        hue=column,
        palette="dark",
        ax=ax,
        legend="full"
    )
    plt.title("Shot Locations on NHL Rink")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend(title=f"{column}", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f"Shot Location with {column}.png")
    
    

