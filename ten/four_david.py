import math

from one_david import BinaryHeap

def find_closest_stars(star_coords, k):
    heap = BinaryHeap(min=False)
    for star_coord in star_coords:
        star_dist = math.sqrt(star_coord[0]**2 + star_coord[1]**2 + star_coord[2]**2)
        heap.push(star_dist, star_coord)
        if heap.size > k:
            heap.pop()
            
    closest_coords = []
    while heap.size > 0:
        closest_coords.append(heap.pop()[1])
    
    return closest_coords[::-1]