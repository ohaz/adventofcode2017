from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4

if __name__ == '__main__':
    days = [day1.calculate_solution, day2.calculate_solution, day3.calculate_solution, day4.calculate_solution]
    for index, day in enumerate(days):
        print("Result for day {} is: {}".format(index, day()))
