import numpy as np
from greedy_TSP_albi import solve_tsp
from main import dataset
from utils import transport_cost, plot_map
from other_utils import sort, update_dict
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


def generate_update(dataset, start_point_string, end_point_string ): #include update
    cost_array = generate_cost_array(dataset)
    triangular_list = array2list(cost_array)
    scores = dataset['score']
    sorter = range(len(scores))
    scores_sort = sort(scores, sorter)
    day_city = dataset['Est. min duration (nights)']
    day_city_max = dataset['Est. max duration (nights)']
    start_point = list(dataset.index.values).index(start_point_string)
    end_point = list(dataset.index.values).index(end_point_string)
    path = solve_tsp(triangular_list, optim_steps=100, endpoints=(start_point, end_point))
    return path, scores_sort, day_city, day_city_max, start_point,end_point



#path = solve_tsp(triangular_list, optim_steps=100, endpoints=(8,0))

def calculate_time_spent(day_city, indeces):
    counter = 0
    for i in indeces:
        counter += day_city[i]
    return counter

start_point_string = 'Jakarta'
end_point_string = 'Bali Kuta/Denpasar'
time_available= 15
def optimize_time(start_point_string, end_point_string, time_available):
    optimaized = False
    dataset_live = dataset
    path, scores_sort, day_city, day_city_max, start_point,end_point = generate_update(dataset_live, start_point_string, end_point_string)
    time_spent = calculate_time_spent(day_city, path)
    while not optimaized:


        if time_spent > time_available:
            try_remove = scores_sort[0]
            if try_remove==start_point or try_remove==end_point: #checkforremoval
                try_remove = scores_sort[1]
            if try_remove==start_point or try_remove==end_point: #checkforremoval needs to be done twice
                try_remove = scores_sort[2]
            dataset_live = update_dict(dataset_live, try_remove)
            path, scores_sort, day_city, day_city_max, start_point, end_point=generate_update(dataset_live, start_point_string, end_point_string)


        if time_spent < time_available:
            counter = -1
            do = True
            while do:
                if day_city[scores_sort[counter]] < day_city_max[day_city[scores_sort[counter]]]: #todo remove day_city
                    day_city[scores_sort[counter]] = day_city[scores_sort[counter]]+1
                    do = False
                else:
                    counter-=1

        time_spent = calculate_time_spent(day_city, path)
        if time_spent==time_available:
            optimaized = True

        print(day_city)

    return dataset_live

dataset_live = optimize_time(start_point_string, end_point_string, time_available)
path, scores_sort, day_city, day_city_max, start_point, end_point=generate_update(dataset_live, start_point_string, end_point_string)
money_available = 2000
start_date = '2018-07-01'
cost_day = 15
get_price(day, place) #todo pull dani
def calculate_money_spent(dataset_live, indeces, cost_day, time_available):
    counter = 0
    # add travel expense
    city1 = dataset_live.index[indeces[0]]
    for i in range(1,len(indeces)):
        city2 = dataset_live.index[indeces[i]]
        counter+=transport_cost(dataset_live, city1, city2)
        city1 = city2
    # add living expenses
    counter += float(cost_day)*float(time_available)
    # add hotel expenses
    for i in indeces:
        counter += day_city[i]
    return counter

def optimize_money(start_point_string, end_point_string, money_available, dataset_live, origin_dataset):
    optimaized = False
    path, scores_sort, day_city, day_city_max, start_point, end_point = generate_update(dataset_live, start_point_string, end_point_string)
    money_spent = calculate_money_spent(day_city, path) #todo change
    while not optimaized:

        if money_spent > money_available:
            try_remove = scores_sort[0]
            if try_remove==start_point or try_remove==end_point: #checkforremoval
                try_remove = scores_sort[1]
            if try_remove==start_point or try_remove==end_point: #checkforremoval needs to be done twice
                try_remove = scores_sort[2]
            dataset_live = update_dict(dataset_live, try_remove)
            path, scores_sort, day_city, day_city_max, start_point, end_point = generate_update(dataset_live, start_point_string, end_point_string)
        if money_spent > money_available:
            counter = 0
            do = True
            while do:
                if day_city[scores_sort[counter]] > origin_dataset['Est. min duration (nights)'][day_city[scores_sort[counter]]]: #todo remove day_city
                    day_city[scores_sort[counter]] = day_city[scores_sort[counter]]-1
                    do = False
                elif counter > len(dataset_live.index.values): # need to remove one element
                    try_remove = scores_sort[0]
                    if try_remove == start_point or try_remove == end_point:  # checkforremoval
                        try_remove = scores_sort[1]
                    if try_remove == start_point or try_remove == end_point:  # checkforremoval needs to be done twice
                        try_remove = scores_sort[2]
                    dataset_live = update_dict(dataset_live, try_remove)
                    path, scores_sort, day_city, day_city_max, start_point, end_point = generate_update(dataset_live,
                                                                                                        start_point_string,
                                                                                                        end_point_string)
                    do = False
                else:
                    counter+=1

        money_spent = calculate_money_spent(day_city, path) #todo change
        if money_spent<=money_available:
            optimaized = True

        print(day_city)

    return dataset_live
#plot_map(itinerary=[(dataset.at[dataset.index.values[i], "Latitude"], dataset.at[dataset.index.values[i], "Longitude"]) for i in path])

