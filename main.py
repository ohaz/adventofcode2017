from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4
from day5 import day5
from day6 import day6
from day7 import day7
from day8 import day8
from day9 import day9

if __name__ == '__main__':
    days = [day1, day2, day3, day4, day5, day6, day7, day8, day9]

    for index, day in enumerate(days):
        print("Result for day {} is: {}".format(index+1, day.calculate_solution()))
