from collections import deque
from ten_nieoh import MaxQueue

def sunset_view(buildings):
    deck = deque('')
    for building in buildings:
        while len(deck) > 0 and building >= deck[-1]:
            deck.pop()
        deck.append(building)
    return list(deck)

def sunset_view_maxq(buildings):
    mq = MaxQueue()
    for building in buildings:
        mq.enqueue(building)

    return sorted(list(set(mq.max_candidates)), reverse=True)
