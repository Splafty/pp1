
# (p7.py) A computer system registers all entries into the car park ("in") and exits from the car park ("out").
# Define a function f(d) that for the registered data d returns an array containing the registration numbers of vehicles that remain in the car park, in alphabetical order.
# Example:
# cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
# f(cars)  ["BA111","GX444","KR234"]
# cars1 = [["KR234","in"],["KR234","out"]]
# f(cars1)  []

def f(d):
    in_out_count = {}
    in_park = set()

    for car, action in d:
        if action == "in":
            in_out_count[car] = in_out_count.get(car, 0) + 1
            in_park.add(car)
        elif action == "out":
            if car in in_out_count:
                in_out_count[car] -= 1
                if in_out_count[car] == 0:
                    in_park.remove(car)
    return sorted(list(in_park))


if __name__ == "__main__":
    cars = [["KR234", "in"], ["BA123", "in"], ["GX444", "in"], ["KR234", "out"], ["BA111", "in"], ["BA123", "out"], ["KR234", "in"]]
    print(f(cars))

    cars1 = [["KR234", "in"], ["KR234", "out"]]
    print(f(cars1))
