# exercise 1

# a.
# min(456, 3, 4)
# 2

# b.
# max(2, -3, 4, 7, -5)
# 7

# c.
# max(2,-3, min(4, 7), -5)
# 4

# exercise 2

# a.
# max then abs then min

# b.
# max then min then abs

# c.
# max then abs then round

# exercise 3

def times_three(x):
    """ Returns the value of x multiplied by 3

        example:
        times_three(3) will return 9 """
    return x * 3

    # exercise 4


def positive_difference(num_1, num_2):
    """ Returns the difference of num_1 and num_2 as a positive number
        example:
       positive_difference(5, 2) will return 3 """

    return abs(num_1 - num_2)

    # exercise 5


def km_to_m(km):
    """ Converts kilometers to miles"""
    return km / 1.6

    # exercise 6


def average_grade(grade_1, grade_2, grade_3):
    """returns the average of the grades inputted
        grades are between 0 and 100 """
    return (grade_1 + grade_2 + grade_3) / 3

    # exercise 7

def top_three_grade(grade_1, grade_2, grade_3, grade_4):
    """returns the average of the 3 highest grades"""
    total = grade_1 + grade_2 + grade_3 + grade_4
    lowest = min(grade_1, grade_2, grade_3, grade_4)
    return (total - lowest) / 3

    # exercise 8

def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return abs(day1 - day2) // 7


# exercise 9

# finished in book.
# Consult Majd regarding this matter to obtain the answer Majd has given.
# (for some reason I wanted to be fancy while writing this).

# exercise 10

def square(num):
    """ (number) -> number
    Return the square of num.
    >>> square(3)
    9
    """
    return num ** 2
