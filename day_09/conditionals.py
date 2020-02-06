# Get user input using input(“Enter your age:”). If user is 18 or older , give feedback:You are old enough to drive 
# but if not 18 give feedback to wait for the years he supposed to wait for. Output:
# driving_age = int(input('How old are you? '))
# real_age = 18
# difference_of_age = str(real_age - driving_age)

# if driving_age == 18 or driving_age > 18:
#     print('You are old enough to drive')
# else:
#     print('You are left with ' + difference_of_age + ' more years to drive')

# Compare the values of my_age and your_age using if … else. Based on the comparison print who is older (me or you). 
# Use input(“Enter your age:”) to get the age as input. Output:
# my_age = int(input('My age is: '))
# your_age = int(input('Enter your age: '))

# greater_my_age = str(my_age - your_age)
# greater_your_age = str(your_age - my_age)

# if my_age > your_age:
#     print('I am', greater_my_age, 'years older than you.')
# else:
#     print('You are', greater_your_age, 'years older than me.')

# Get two numbers from user using, input prompt. If a is greater than b return a is greater than b,
# if a is less b return a lesson b, else a is equal to b. Output:
# input_a = int(input('Enter a number: '))
# input_b = int(input('Enter a number: '))
# if input_a > input_b:
#     print(input_a, 'is greater than', input_b)
# else:
#     print(input_b, 'is greater than', input_a)

# Write a code which give grade to students according to theirs scores:
test_score = int(input('Enter your test score: '))
# 80-100, A
if test_score >= 80 and test_score <= 100:
    print('Your test grade is A')
# 70-89, B
elif test_score >= 70 and test_score <= 89:
    print('Your test grade is B')
# 60-69, C
elif test_score >= 60 and test_score <= 69:
    print('Your test grade is C')
# 50-59, D
elif test_score >= 50 and test_score <= 59:
    print('Your test grade is D')
# 0 -49, F
elif test_score == 0 or test_score <= 49:
    print('Your test grade is F')
else:
    print('Your test score is null and void')

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or 
# November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
# year_seasons = input('Enter any month of the year: ').capitalize()
# if year_seasons == 'September' or year_seasons == 'October' or year_seasons == 'November':
#     print('The season is Autumn')
# elif year_seasons == 'December' or year_seasons == 'January' or year_seasons == 'February':
#     print('The season is Winter')
# elif year_seasons == 'March' or year_seasons == 'April' or year_seasons == 'May':
#     print('The season is Sping')
# elif year_seasons == 'June' or year_seasons == 'July' or year_seasons == 'August':
#     print('The season is Summer')
# else:
#     print('Enter the correct month')

# The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit in the list and print the modified 
# list but if the fruit exists print('A fruit already exist in the list')
# fruits = ['banana', 'orange', 'mango', 'lemon']
# name_of_fruit = input('Enter a name of a fruit: ')
# does_exist = name_of_fruit in fruits
# print(does_exist)
# if does_exist == False:
#     fruits.append(name_of_fruit)
#     print(fruits)
# else:
#     print('That fruit already exist in the list')

person = {
    'first_name':'Felix',
    'last_name':'Iroms',
    'age':50,
    'country':'Nigeria',
    'is_marred': False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Mpape street',
        'zipcode':'901203'
    }
}

# Check if the person dictionary has skills, if it has skills key check print out the middle skill in the skills list.
skills_exist = 'skills' in person
print(skills_exist)
if 'skills' in person:
    middle_index = person['skills'][2]
    print(middle_index)
else:
    print('Skills is not available')

# Check if the person dictionary has skills, if it has skills key check if the person has 'Python' skill and print the skill.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('python')
    else:
        print('javascript')
else:
    print('Skills is not in person dictionary')
