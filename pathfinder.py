"""
HackDelft Team BacPac
Solving a TSP problem to find optimal itinerary in region
"""

from main import dataset
import numpy as np

# Load graph

"""
Landmark Definition:
1. Bali Kuta/Denpasar
2. Bali Ubud
3. Nusa Penida
4. Gili Islands
5. Borobudur
6. Ujung Kulon
7. Mount Bromo
8. Yogyakarta
9. Jakarta
10. Lombok
11. Flores
12. Komodo
13. Rinca
14. Labuan Bajo
"""


def cost_array(a, b):
    pass


path_distance = lambda r, c: np.sum([np.linalg.norm(c[r[p]]-c[r[p-1]]) for p in range(len(r))])

# Reverse the order of all elements from element i to element k in array r.
two_opt_swap = lambda r, i, k: np.concatenate((r[0:i], r[k:-len(r)+i-1:-1], r[k+1:len(r)]))


def two_opt(cities, improvement_threshold): # 2-opt Algorithm adapted from https://en.wikipedia.org/wiki/2-opt
    route = np.arange(cities.shape[0])  # Make an array of row numbers corresponding to cities.
    improvement_factor = 1  # Initialize the improvement factor.
    best_distance = path_distance(route,cities) # Calculate the distance of the initial path.
    while improvement_factor > improvement_threshold: # If the route is still improving, keep going!
        distance_to_beat = best_distance # Record the distance at the beginning of the loop.
        for swap_first in range(1,len(route)-2): # From each city except the first and last,
            for swap_last in range(swap_first+1,len(route)): # to each of the cities following,
                new_route = two_opt_swap(route,swap_first,swap_last) # try reversing the order of these cities
                new_distance = path_distance(new_route,cities) # and check the total distance with this modification.
                if new_distance < best_distance: # If the path distance is an improvement,
                    route = new_route # make this the accepted best route
                    best_distance = new_distance # and update the distance corresponding to this route.
        improvement_factor = 1 - best_distance/distance_to_beat # Calculate how much the route has improved.
    return route # When the route is no longer improving substantially, stop searching and return the route.