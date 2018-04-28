"""
Created by Alejandro Daniel Noel
"""


def transport_cost(dataframe, landmark1, landmark2):
    p1 = dataframe.loc[landmark1, "Cost to Ujung Kulon"]
    p2 = dataframe.loc[landmark2, "Cost to Ujung Kulon"]
    return abs(p1 - p2)
