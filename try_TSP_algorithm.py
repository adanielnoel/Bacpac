import numpy as np
from greedy_TSP_albi import solve_tsp
from main import dataset
from utils import transport_cost, plot_map
'''#test
#a = np.array([[0,2,3],[7,0,5], [9,10,0]])
a = np.random.rand(14,14)
np.fill_diagonal(a, 0)
print(a)'''

def cost_array():
    'generates cost array'
    array = np.zeros((len(dataset.index.values),len(dataset.index.values)))
    for i, city1 in enumerate(dataset.index.values):
        for j, city2 in enumerate(dataset.index.values):
            array[i, j] = transport_cost(dataset, city1, city2)
    return array
a = cost_array()

def array2list(array):
    'list conversions'
    b = list(array)
    c = [list(i) for i in b]
    triangular_list = [i[: i.index(0)] for i in c]
    return triangular_list

D= array2list(a)
print(D)
path = solve_tsp(D, optim_steps=100, endpoints=(8,4))
print(path)

plot_map(itinerary=[(dataset.at[dataset.index.values[i], "Latitude"], dataset.at[dataset.index.values[i], "Longitude"]) for i in path])

