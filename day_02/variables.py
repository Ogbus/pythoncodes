# Day 02: 30 days of python programming

first_Name = "Felix"
last_Name = "Iroms"
full_Name = "Felix Iroms"
country = "Nigeria"
city = "Lagos"
age = 34
year = 2020
is_Married = False
is_true = True
is_light_on = True
is_single, height, is_fit = True, 5.8, True

# Checking varible types
print(type(first_Name))
print(type(last_Name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_Married))
print(type(is_single))
print(type(is_light_on))
print(type(is_single))
print(type(height))
print(type(is_fit))

# Checking the length of a variable
print(len(first_Name))

# Doing some basic maths in python
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
divide = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(divide)
print(remainder)
print(exp)
print(floor_division)

# Calculating the area and circumference of a circle
radius = int(input("Give me radius of a circle: "))
square_of_radius = radius * radius
pi = 3.14
area_of_circle = pi * square_of_radius
print(area_of_circle)

circum_of_circle = 2 * pi * radius
print(circum_of_circle)

# Getting inputs from users
firstName = input("what is your first name? ")
lastName = input("what is your last name? ")
your_country = input("what country are you from? ")
isAge = input("how old are you? ")

print("Hello Sir, my name is", firstName, lastName, "I am from", your_country, "and I am", isAge, "years old.")