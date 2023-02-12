def number_of_passengers(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)
