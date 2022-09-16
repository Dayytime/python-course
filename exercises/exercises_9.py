# exercise 1

celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

for thing in celegans_phenotypes:
    print(thing)

# exercise 2

half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]

for number in half_lives:
    print(number, end=" ")

print()

# exercise 3

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
for item in whales:
    more_whales.append(item + 1)

print(more_whales)
print()
# exercise 4

alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.028], [38, 87.62], [56, 137.327], [88, 226]]
number_and_weight = []
for i in alkaline_earth_metals:
    for j in i:
        number_and_weight.append(j)


print(number_and_weight)


# exercise 5 ?????

# exercise 6

text = ''

# while text != "quit":
#    text = input("hey there! ").lower()

# exercise 7

populations = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0

for people in populations:
    total += people

print(total)

# exercise 8

rat1 = [5, 6, 3, 8, 4, 8, 4, 3, 9]
rat2 = [1, 7, 0, 10, 100, 635, 1000]

if rat1[1] > rat2[1]:
    print("Rat 1 weighed more than rat 2 on day 1")
else:
    print("Rat 1 weighed less than rat 2 on day 1")


if rat1[1] > rat2[1] and rat1[-1] > rat2[-1]:
    print("Rat 1 remained heavier")
else:
    print("Rat 1 remained lighter")

if rat1[1] > rat2[1]:
    if rat1[-1] > rat2[-1]:
        print("Rat 1 remained heavier")
    else:
        print("rat 2 remained heavier")
else:
    print("rat 2 is heavier")

# exercise 9

for i in range(33, 50):
    print(i)

# exercise 10

for i in range(10, 0, -1):
    print(i, end=" ")
print()

# exercise 11

rangee = range(2, 23)
summ = 0
count = 0
for digit in rangee:
    summ += digit
    count += 1
print(summ/count)

# exercise 12
# this one was hard

num_list = [1, 2, 3, -3, 6, -1, -3, 1]
index = 0
while index < len(num_list):
    if num_list[index] < 0:
        del num_list[index]
    else:
        index += 1


print(num_list)

# exercise 13

for t in range(1, 8):
    print("T" * t)

# exercise 14

space_counter = 6
for t in range(1, 8):
    print(" " * space_counter, "T" * t, sep="")
    space_counter -= 1

# exercise 15

counter = 1
t = 1
space_counter = 6

while counter < 8:
    print("T" * t)
    t += 1
    counter += 1

counter = 1
t = 1
space_counter = 6

while counter < 8:
    print(" " * space_counter, "T" * t, sep="")
    t += 1
    counter += 1
    space_counter -= 1

# exercise 16

rat_1_weight = 100
rat_2_weight = 100
rat_1_rate = 10 / 100
rat_2_rate = 5 / 100
weeks = 0
initial_rat_1_weight = rat_1_weight

while (initial_rat_1_weight / 100) >= (rat_1_weight / 125):
    increment = rat_1_weight * rat_1_rate
    rat_1_weight += increment
    print(weeks)
    weeks += 1


print(rat_1_weight)
print()

rat_1_weight = 100
weeks = 0

while rat_1_weight <= rat_2_weight * (110 / 100):
    rat_1_weight *= (110 / 100)
    rat_2_weight *= (105 / 100)
    weeks += 1

print("The number of weeks is " + str(weeks))
print()


