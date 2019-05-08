#Exercise0
my_list = ["skyblue", "lightblue", "white", 37, 33, 40, 24, "heads", "heads", "tails", "Blackpink", "Tupac", "Twice"]

my_dictionary = {"judo": "to smash people", "mma": "to knockout people", "developer": "create stuffs", "Heat": 1995, "Toronto": 300, "Seoul": 5000, "New York": 2900, "Grace": 24, "Helen": 33}

#Exercise1
# Print out the list of coin flips.
print(my_list[2:4])
# Print out the first element of the list of your favourite colours.
print(my_list[0])
# Output the sorted version of the list of your friends and family members' ages.
ages = my_list[3:7]
ages.sort()
print(ages)
# Add a new baby (0 years old) to the list of your family's ages.
my_list.append(0)
print(my_list)
# Using the dictionary of movie information, access and print the year of one of the movies.
print(my_dictionary["Heat"])

#Exercise2

# Print out the last element of the list of your favourite colours.
# Note: do this in a way that would still work for a list of any size!
print(my_list[:3])
# Add a new city to the dictionary of cities and population.
my_dictionary['Miami']= 5000
# Reverse the list of coin flips and save it.
coins = my_list[7:10]
coins.reverse()
print(coins)
# Print out the population of one of the cities.
print(my_dictionary["Toronto"])
# Print out a sentence about each item in the list of performing artists. For example:
# I think Pearl Jam is great.
# I think Lady Gaga is great.
# I think Pink Floyd is great.
print("I think {} is hot.".format(my_list[10]))
print("I think {} is great.".format(my_list[11]))
print("I think {} is cute.".format(my_list[12]))

#Exercise3

# Print out the first two performing artists in that list.
print(my_list[10])
print(my_list[11])
# For each of your favourite movies, print out a sentence about when the movie was released. For example:
# Avatar came out in 2009.
# Mean Girls came out in 2004.
# The Matrix came out in 1999.
print("Heat came out in {}.".format(my_dictionary["Heat"]))
# Sort and reverse the list of ages of your family. Save it and print it to the screen.
# See if you can sort and reverse the list on one line!
family_age = {"Grace": 24, "Helen": 33}
family_age_sorted_keys = sorted(family_age, key = family_age.get, reverse=True)
print(family_age_sorted_keys)
# Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out.
my_dictionary["Beauty and the Beast"] = 1991, 2017
print(my_dictionary)

#Exercise4

# Print out all of the ages of your friends/family that are less than 30 (or any number where some ages will not be printed!).
for each_age in ages:
    if each_age < 30:
        print(each_age)
# Find and output the age of the oldest person in your friends/family list.
print(max(ages))
# Count how many times you flipped 'heads' using the coin flips list.
print(coins.count('heads'))
# You realize one of the performing artists in your list is no longer a favourite. Remove one of them from the list.
print(my_list.pop(-3))
# Pick a city in your city population dictionary and change its population.
my_dictionary['Toronto'] = 3150
print(my_dictionary)

#Exercise5

# Find the sum total of the population in the dictionary of cities.
population = 0
for key, value in my_dictionary.items():
    if key == "Toronto": 
        population = population + value
    elif key == "New York":
                population += value
    elif key == "Seoul":
                        population += value


print(population)

# Using your dictionary containing the names of your family and friends with their ages, print out one of two messages for each depending on their age. For example:
# Martha is old.
# Stewart is young.
# Holly is young.

for key, value in family_age.items():
        if value < 30:
                print(f"{key} is young")
        else:
                print(f"{key} is old ")

# Print out the last two colours in your list of favourite colours.
print(my_list[1:3])

# Increase by 1 the age of everyone in your list of ages. Print it out.
for index, age in enumerate(ages):
        ages[index] = age + 1
print(ages)

# Add two new colours to your list of favourite colours.
my_list.append("red")
my_list.append("cyan")
print(my_list)

#Exercise 6

# Make a new dictionary that contains a list of movies for each year. Each list of movies should be a list. Below is some data you can use.

# 1999: The Matrix, Star Wars: Episode 1, The Mummy
# 2009: Avatar, Star Trek, District 9
# 2019: How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9

movies = {1999: ["The Matrix", "Star Wars", "The Mummy"], 2009: ["Avatar", "Star Trek", "District 9"], 2019: ["Your Dragon", "Toy Story", "Avengers"]}

# Make a new list that contains each row of the buttons on a phone. Each row should be a list.

# The rows on a phone are: 1 2 3, 4 5 6, 7 8 9, * 0 #
# phone = [[1,2,3], [4,5,6], [7,8,9], [*,0,'#']]

# Make a new list that contains information about three countries. Each country should be a dictionary that has a name, a continent, and whether or not it is an island.

three_countries = [{"Canada": ["North America","not island"]}, {"USA": ["North America", "not island"]}, {"Korea": ["Asia", "not island"]}]

#Exercise7

# Output the message "I will not skateboard in the halls" 20 times.

# for i in range(20):
#         print("I will not skateboard in the halls")

# Create a list consisting of the above message. It should appear in the list 20 times.
# skateboard = ["I will not skateboard in the halls"]
# for i in range(20):
#         print(skateboard)

# Create a list consisting of the numbers between 1 and 50.

numbers = range(1, 51)
print(list(numbers))

# Use a for loop to find the sum of the numbers in the above list.
sum = 0
for i in numbers:
        sum = sum + i
print(sum)

# Create a new list which has three of each number up to 50.
# Ie. [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50] and so on, up to 50.

repeats = []
for i in numbers:
        repeats.append(i)
        repeats.append(i)
        repeats.append(i)

print(repeats)

# Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands. Print out both lists.
three_countries = [{"Canada": ["North America","not island"]}, {"USA": ["North America", "not island"]}, {"Korea": ["Asia", "not island"]}]

# You want to add up your expenses for the year. Create a list of numbers (integers or floats) that represents your expenses, eg:
# [250, 7.95, 30.95, 16.50]
# Add up the numbers and output the result.

my_expense = [300, 50.1, 30, 50, 10]
# total = sum(my_expense) 
# print(total)

# Put this code into a method. The method should take a list as an argument and return the sum of the expenses in the list. Call the method twice with different lists.
def total(my_expense):
        the_sum = 0
        for i in my_expense:
                the_sum+=i
        return the_sum

print(total(my_expense))       