#  Day 03: 30 days of python programming

my_age = 34
my_height = 5.9
num_complex = 2 - 6j

# Calculating area of a triangle
# area_of_triangle = h * b / 2
base_num = int(input("base of the triangle: "))
height_num = int(input("height of the triangle: "))
area_of_triangle = base_num * height_num / 2
print(area_of_triangle)


# perimeter of a triangle = a + b + c
sideA = int(input("side a number: "))
sideB = int(input("side b number: "))
sideC = int(input("side c number: "))
perimeter = sideA + sideB + sideC
print(perimeter)

# calculating area of a rectangle and its perimeter
# area_of_rectangle = length * width
length_num = int(input("number of length: "))
width_num = int(input("number of width: "))
area_of_rectangle = length_num * width_num
print(area_of_rectangle)

# perimeter of a rectangle = 2 * (length + width)
perimeter_of_rectangle = 2 * (length_num + width_num)
print(perimeter_of_rectangle)

# calculating area and circumference of a circle
# area of a circle = πr2
radius = int(input("Give me radius of a circle: "))
square_of_radius = radius * radius
pi = 3.14
area_of_circle = pi * square_of_radius
print(area_of_circle)

# circumference of a circle = 2πr
circum_of_circle = 2 * pi * radius
print(circum_of_circle)

# Comparison Statement
pyth_len = "python"
jarg_len = "jargon"
print(len(pyth_len) != len(jarg_len))

print('on' is pyth_len and 'on' is jarg_len)

print('jargon' in 'I hope this course is not full of jargon')

# Find the length of the text python and convert the value to float and convert it to string
python_len = "python"
len_size = len(python_len)
print(len_size)

float_len_size = print(float(len_size))
str_len_size = print(str(len_size))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print(4 % 2)

print(7 // 3)

# Check if type of '10' is equal to 10
print('10' == 10)

# Check if int('9.8') is equal to 10
# int class cannot convert a string float into an integer.
# int_num = int("9.8")
# print(int_num)

# Writ a script that prompt a user to enters hours and rate per hour. Calculate pay of the person?
num_of_hours_per_day = int(input("Number of hours you work per day: "))
rate_per_hour = int(input("your pay per hour: "))
daily_wage = num_of_hours_per_day * rate_per_hour
print(daily_wage)

# Write a script that prompt the user to enter number of years. Calculate the number of seconds a person 
# can live. Assume some one lives just hundred years
year_per_seconds = 31536000
num_of_years_lived = int(input("How many years have you been on Earth? "))
total_num_of_seconds_lived = year_per_seconds * num_of_years_lived
print(total_num_of_seconds_lived)