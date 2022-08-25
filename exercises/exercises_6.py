import math
import calendar

# exercise 1

# a.
math.floor(-2.8)
# b.
abs(round(-4.3))
# c.
math.ceil(math.sin(34.5))

# exercise 2
# c.
print(help(calendar.isleap()))
# d.
print(calendar.isleap(2023))
# e.
print(dir(calendar))
# f.
print(calendar.leapdays(2000, 2050))
# g.
print(calendar.weekday(2016, 7, 29))

# exercise 3


def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10, 20)
    20.0
    >>> average(2.5, 3.0)
    4.0
    """
    return num1 + num2 / 2



