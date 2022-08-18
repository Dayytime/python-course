
# exercise 1
# a. True
# b. error
# c. True
# d. True
# e. True
# f. True
# g. False
# h. False

# exercise 2

# a. x and y
# b. not x
# c. x or y

# exercise 3

# (full and not empty) or (empty and not full)

# exercise 4

# yes my friend is right. Their code is much easier to read and works.

# exercise 5

# result = abs(x) == x

# exercise 6

def different(a, b) -> bool:
    "Returns true if a and b are not equal to each other"
    return a != b


print(different(1, 2))

# exercise 7

population = 0
land_area = 1

# a.
if population < 10000000:
    print(population)

# b.
if 10000000 <= population <= 35000000:
    print(population)

# c.
if (population/land_area) > 100:
    print("Densely populated")

# d.
if (population/land_area) > 100:
    print("Densely populated")
else:
    print("Sparsely populated")

# exercise 8
# a.


def pain(t, source, target):
    if source == 'Kelvin':
        celsius = t - 273.15
    elif source == 'Celsius':
        celsius = t
    elif source == 'Fahrenheit':
        celsius = (t - 32) * 5 / 9
    elif source == 'Rankine':
        celsius = (t - 491.67) * 5 / 9
    elif source == 'Delisle':
        celsius = 100 - t * 2 / 3
    elif source == 'Newton':
        celsius = t * 100 / 33
    elif source == 'Reamur':
        celsius = t * 5 / 4
    elif source == 'Romer':
        celsius = (t - 7.5) * 40 / 21

    if target == 'Kelvin':
        return celsius + 273.15
    elif target == 'Celsius':
        return celsius
    elif target == 'Fahrenheit':
        return celsius * 9 / 5 + 32
    elif target == 'Rankine':
        return (celsius + 273.15) * 9 / 5
    elif target == 'Delisle':
        return (100 - celsius) * 3 / 2
    elif target == 'Newton':
        return celsius * 33 / 100
    elif target == 'Reamur':
        return celsius * 4 / 5
    elif target == 'Romer':
        return celsius * 21 / 40 + 7.5


# b. 2

# exercise 9

# the problem is when it runs the first if statment it checks for ANY number below 7. if our number is 3 it will say it
# is acidic and not run the elif statment. We can fix this by doing:

ph= 0

if ph < 3:
    print("very acidic")
else:
    print("acidic")

# exercise 10

# a. it's acidic
# b. it's acidic

# c. change the elif to if


# exercise 11

# I am not sure why you would put light instead of heavy but you can change it to this:

young = age < 45
heavy = bmi >= 22.0

if young and not heavy:
    risk = 'low'
elif young and heavy:
    risk = 'medium'
elif not young and not heavy:
    risk = 'medium'
elif not young and heavy:
    risk = 'high'




