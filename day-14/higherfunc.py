from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.
# map, filter and reduce are higher order functions: map takes a function and iteratible data type that iterates over each item and 
# returns a new array. Filter takes a function and an iteratible data type and returns elements that meets the conditions of the function.
# reduce takes a function and an iteratible data type and returns a single value.
# Explain the difference between higher order function, closure and decorator
# Define a call function before map, filter or reduce, see examples.
# Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# Use for to print each name in the names list.
for name in names:
    print(name)

# Use for to print each number in the numbers list.
for number in numbers:
    print(number)

# Use map to create a new list by changing each country to uppercase in the countries list
def uppercase(county):
    return county.upper()
countries_uppercase = map(uppercase, countries)
print(list(countries_uppercase))

# Using the lamda function
countries_uppercases = map(lambda name: name.upper(), countries)
print(list(countries_uppercases))

# Use map to create a new list by changing each number to square in the numbers list
def square(num):
    return num ** 2
squared_numbers = map(square, numbers)
print(list(squared_numbers))

# Use map to change to each name to uppercase in the names list
def name_uppercase(name):
    return name.upper()
capitalize_names = map(name_uppercase, names)
print(list(capitalize_names))

# Use filter to filter out countries containing land.
def filter_countries(filtered):
    if filtered.endswith('land'):
        return filtered
    else:
        pass
filtered_countries = filter(filter_countries, countries)
print(list(filtered_countries))

# Use filter to filter out countries having six character.
def filter_six_countries(character):
    if len(character) == 6:
        return character
    else:
        pass
filtered_six_characters = filter(filter_six_countries, countries)
print(list(filtered_six_characters))

# Use filter to filter out countries containing six letters and more in the country list.
def filter_six_more_countries(character):
    if len(character) >= 6:
        return character
    else:
        pass
filtered_six_more_characters = filter(filter_six_more_countries, countries)
print(list(filtered_six_more_characters))

# Use filter to filter out country start with 'E'
def start_with(first):
    if first.startswith('E'):
        return first
    else:
        pass
starting_with = filter(start_with, countries)
print(list(starting_with))

# Chain two or more list iterators(eg. arr.map(callback).filter(callback).reduce(callback))
def addition(a, b):
    return int(a) + int(b)
change_two_orderfunc = map(square, numbers)
reduce_func = reduce(addition, change_two_orderfunc)
print(reduce_func)
# Declare a function called get_string_lists which takes an list as a parameter and then returns an list only with string items.

# Use reduce to sum all the numbers in the numbers list.
summation = reduce(addition, numbers)
print(summation)
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and IceLand are north European countries
def concatenate(*args):
    return ', '.join(args)
concatenating = reduce(concatenate, countries)
print(concatenating, 'are Nothern European countries.')
# Declare a function called categorize_countries which returns an list of countries which have some common pattern(you find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Create a function which return a list of dictionary, which is the letter and the number of times the letter used to start a name of a country.
# Declare a get_first_ten_countries function and return an list of ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function which which returns the last ten countries in the countries list.
# Find out which letter is used many times as initial for a country name from the countries list(eg. Finland, Fiji, France etc)
