"""
Created by Alejandro Daniel Noel
"""

import pandas

from maps import plot_map


dataset = pandas.read_csv("IndonesiaDataset.csv")

# Factor for those that include ferry (usually more expensive)
dataset.loc[dataset["Distance to Ujung Kulon"] > 1090, "Distance to Ujung Kulon"] *= 1.4
# Convert to fuel cost
dataset.loc[:,"Distance to Ujung Kulon"] *= 0.09 * 9250  # liter/km * rupiah/liter
# Factor service cost
dataset.loc[:,"Distance to Ujung Kulon"] *= 1.1


plot_map(points=[tuple(coords) for coords in dataset[["Latitude", "Longitude"]].values],
         names=dataset["Landmark"].values)

