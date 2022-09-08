
# exercise 1
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

print(kingdoms[0])
print(kingdoms[5])
print(kingdoms[:3])
print(kingdoms[2:5])
print(kingdoms[4:])
print(kingdoms[2:2])

# exercise 2

print(kingdoms[-6])
print(kingdoms[-1])
print(kingdoms[-6:-3])
print(kingdoms[-4:-1])
print(kingdoms[-2:])
print(kingdoms[-1:-1])

# exercise 3

appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']

# a.
appointments.append('16:30')

# b.
print(appointments + ['16:30'])

# c.
# The second approach created a new list

# exercise 4

ids = [4354, 2314, 2956, 3382, 9362, 3900]

# a.
del ids[3]
# b.
print(ids.index(9362))
# c.
ids.insert(4, 4499)
# d.
ids.extend([5566, 1830])
# e.
ids.reverse()
# f.
ids.sort()

# exercise 5
# a.
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
# b.
alkaline_earth_metals[5]
alkaline_earth_metals[-1]
# c.
print(len(alkaline_earth_metals))
# 6
# d.
print(max(alkaline_earth_metals))

# exercise 6
# a.
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
# b.
temps.sort()
# c.
cool_temps = temps[:2]
warm_temps = temps[2:]
# d.
temps_in_celsius = cool_temps + warm_temps

# exercise 7


def same_first_last(l: list) -> bool:
    if l[0] == l[-1]:
        return True

print(same_first_last([2,5,7,4,2,7,3,1,2]))

# exercise 8


def is_longer(l1: list, l2: list) -> bool:
    if len(l1) > len(l2):
        return True

# exercise 9


# exercise 10
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
# a.
units[0]
# b.
units[1]
# c.
units[0][0]
# d.
units[1][0]
# e.
units[0][1:]
# f.
units[1][:2]

# exercise 11

# a.
units[-2]
# b.
units[-1]
# c.
units[-2][-3]
# d.
units[-1][-3]
# e.
units[-2][-2:]
# f.
units[-1][:-1]
