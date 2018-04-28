import numpy as np
from greedy_TSP_albi import solve_tsp
from main import dataset
from utils import transport_cost, plot_map
'''#test
#a = np.array([[0,2,3],[7,0,5], [9,10,0]])
a = np.random.rand(14,14)
np.fill_diagonal(a, 0)
print(a)'''

def generate_cost_array(dataset):
    'generates cost array'
    array = np.zeros((len(dataset.index.values),len(dataset.index.values)))
    for i, city1 in enumerate(dataset.index.values):
        for j, city2 in enumerate(dataset.index.values):
            array[i, j] = transport_cost(dataset, city1, city2)
    return array


def array2list(array):
    'list conversions'
    b = list(array)
    c = [list(i) for i in b]
    triangular_list = [i[: i.index(0)] for i in c]
    return triangular_list


def generate_triangular_list(dataset): #include update
    cost_array = generate_cost_array(dataset)
    triangular_list = array2list(cost_array)
    return triangular_list

#need function get max array
#need function get min array
#need function get popularity array



#path = solve_tsp(triangular_list, optim_steps=100, endpoints=(8,0))

popular_list= [10,9,7,3,6,4,2,1,5,14,13,11,12,0] #this will update with dictionary automatically
day_city = [3,4,5,6,5,3,4,1,2,3,4,5,1,2] #this will update with dictionary automatically minimum

def calculate_time_spent(day_city, indeces):
    counter = 0
    for i in indeces:
        counter += day_city[i]
    return counter
optimaized = False
time_available= 14 #input user
start_point = 8 #index of start city, good to put time and get number
end_point = 0 #index of end city
triangular_list = generate_triangular_list(dataset)
path = solve_tsp(triangular_list, optim_steps=100, endpoints=(start_point, end_point))
time_spent = calculate_time_spent(day_city, path)
while not optimaized:


    if time_spent > time_available:
        try_remove = popular_list[0]
        if try_remove==start_point or try_remove==end_point: #checkforremoval
            try_remove = popular_list[1]
        if try_remove==start_point or try_remove==end_point: #checkforremoval needs to be done twice
            try_remove = popular_list[2]
        #funtoremovefromdictionary
        triangular_list=generate_triangular_list(dataset)
        path = solve_tsp(triangular_list, optim_steps=100, endpoints=(start_point, end_point))

    if time_spent < time_available:
        counter = -1
        do = True
        while do:
            if day_city[popular_list[counter]] != max_day_city[day_city[popular_list[counter]]]:
                day_city[popular_list[-1]] = day_city[popular_list[-1]]+1
                do = False
            else:
                counter-=1

    time_spent = calculate_time_spent(day_city, path)
    if time_spent==time_available:
        optimaized = True



#plot_map(itinerary=[(dataset.at[dataset.index.values[i], "Latitude"], dataset.at[dataset.index.values[i], "Longitude"]) for i in path])

