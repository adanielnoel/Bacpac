"""
Created by Alejandro Daniel Noel
"""

import pandas
from hotel_finder import Hotels
from utils import transport_cost
import datetime

'Inputs'
checkin_date = '2018-10-29'
nr_days = 1

#######################
dataset = pandas.read_csv("IndonesiaDataset.csv")
dataset.set_index("Landmark", inplace=True)
accomodation_cost = 0

for landmark in dataset.index.values:
    my_hotels = Hotels((dataset.at[landmark, 'Latitude'], dataset.at[landmark, 'Longitude']), checkin_date,
                       nr_days)
    my_hotel_price = my_hotels.get_average_price()
    if isinstance(my_hotel_price, (int, float)):
        accomodation_cost += my_hotel_price
    else:
        dataset.drop([landmark], inplace=True)
    print(landmark, my_hotel_price)

# dataset.set_index("Landmark", inplace=True)

# # Factor for those that include ferry (usually more expensive)
# dataset.loc[dataset["Cost to Ujung Kulon"] > 1090, "Cost to Ujung Kulon"] *= 1.4
# # Convert to fuel cost
# dataset.loc[:, "Cost to Ujung Kulon"] *= 0.09 * 9250  # liter/km * rupiah/liter
# # Factor service cost
# dataset.loc[:, "Cost to Ujung Kulon"] *= 1.1
print(accomodation_cost)
print(transport_cost(dataset, "Bali Ubud", "Nusa Penida"))

# plot_map(points=[tuple(coords) for coords in dataset[["Latitude", "Longitude"]].values],
#          names=dataset["Landmark"].values)
# print(dataset)