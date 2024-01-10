# (p3.py) Flight numbers along with the number of passengers are stored in a dictionary d.
# Define a function f(d) that returns the number of flights in which the number of passengers is greater than the average number of passengers on all flights.
# Example:
# f({"LO231":150,"BA787":120,"NZ15":30})  2
# f({"LO231":150,"BA787":20,"NZ15":30})  1


def f(d):
    if not d:
        return 0

    average_passengers = sum(d.values()) / len(d)

    num_flights_above_average = sum(1 for passengers in d.values() if passengers > average_passengers)

    return num_flights_above_average

if __name__ == "__main__":
    print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))
    print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))