from one_david import Stack

def get_sunset_view_buildings(heights):
    view_buildings = Stack()
    for height in heights:
        while height >= view_buildings.peek() and view_buildings.peek() is not None:
            view_buildings.pop()
        view_buildings.push(height)
    return view_buildings.to_list()