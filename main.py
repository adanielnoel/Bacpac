"""
Created by Alejandro Daniel Noel
"""

import pandas

from utils import transport_cost

dataset = pandas.read_csv("IndonesiaDataset.csv")
dataset.set_index("Landmark", inplace=True)

# # Factor for those that include ferry (usually more expensive)
# dataset.loc[dataset["Cost to Ujung Kulon"] > 1090, "Cost to Ujung Kulon"] *= 1.4
# # Convert to fuel cost
# dataset.loc[:, "Cost to Ujung Kulon"] *= 0.09 * 9250  # liter/km * rupiah/liter
# # Factor service cost
# dataset.loc[:, "Cost to Ujung Kulon"] *= 1.1

print(transport_cost(dataset, "Bali Ubud", "Nusa Penida"))

# plot_map(points=[tuple(coords) for coords in dataset[["Latitude", "Longitude"]].values],
#          names=dataset["Landmark"].values)
