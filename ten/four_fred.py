import random


def nearest_stars(stars, k):
    s = stars[:]
    random.shuffle(s)
    s.sort(key=lambda x: x[0]**2 + x[1]**2 + x[2]**2)
    return s[:k]
