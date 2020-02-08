# Declare a function add_two_numbers and it takes two two parameters and it returns sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(39,4))

# Area of a circle is calculated as follows: area = π x r x r. Write a function which calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area
print(area_of_circle(13))

# Write a function called add_all_nums which take arbitrary number of arguments and sum all the arguments. Check if 
# all the list items are number types. If not give return reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, int):
            total += num
        else:
            print('Use integer instead')
    return total
print(add_all_nums(2,3,4,5,4,2))

# Temperature in oC can be converted to oF using this formula: oF = (oC x 9/5) + 32. Write a function which 
# converts oC to oF, convert_celcius_to-fahrenheit.
def convert_celcius_to_fahrenheit(oC):
    convert_oC_to_oF = (oC * 9/5) + 32
    return convert_oC_to_oF
print(convert_celcius_to_fahrenheit(1))

# Write a function called check-season, it takes a month parameter and returns the season:Autumn, Winter, Spring or Summer.
def check_season(month):
    # month = input('Enter a month: ').capitalize()
    if month == 'September' or month == 'October' or month == 'November':
        return ('The season is Autumn')
    elif month == 'December' or month == 'January' or month == 'February':
        return('The season is Winter')
    elif month == 'March' or month == 'April' or month == 'May':
        return('The season is Sping')
    elif month == 'June' or month == 'July' or month == 'August':
        return('The season is Summer')
    else:
        return('Enter the correct month')
print(check_season('August'))

# Declare a function name print_list. It takes list as a parameter and it prints out each element of the list.
def print_list(*lists):
    for items in lists:
        print(items)
print(print_list(1,3,3,4,5,6))

# Declare a function name reverse_list. It takes array as a parameter and it returns the reverse of the array (dont’ use method).
def reverse_list(array):
    new_array = array[::-1]
    return new_array
arrayy = [2,4,5,6,7]
string = ['a', 'b', 'c', 'd']
print(reverse_list(arrayy))
print(reverse_list(string))

# Declare a function name capitalize_list_items. It takes list as a parameter and it returns the capitalized list of the items
# def capitalize_list_items(array):
#     new_arr = array.capitalize()
#     print(new_arr)
# cap_letters = ['felix', 'iroms', 'john']
# print(capitalize_list_items(cap_letters))

# Declare a function name add_item. It takes a list and an item parameter and it returns a list after adding the item
def add_item(*arrs):
    food_items = ['fish', 'rice', 'yam']
    for arr in arrs:
        food_items.append(arr)
    return food_items
print(add_item('beans', 'garri'))

# Declare a function name remove_item. It takes a list and an item parameter and it returns a list after removing an item.
food_items = ['fish', 'rice', 'yam', 'beans', 'garri']
def remove_item(*array):
    for arr in array:
        food_items.pop(arr)
    return food_items
print(remove_item(2))

# Declare a function name sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    sum_total = 0
    for numbers in range(number):
        sum_total += numbers
    return sum_total
print(sum_of_numbers(101))

# Declare a function name sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(numbers):
    total_odd = 0
    for number in range(numbers):
        if number % 2 != 0:
            total_odd = total_odd + 1
        else:
            pass
    print('Total number of odd numbers are', total_odd)
    return total_odd
print(sum_of_odds(100))

# Declare a function name sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(numbers):
    total_even = 0
    for number in range(numbers):
        if number % 2 == 0:
            total_even = total_even + 1
        else:
            pass
    print('Total number of even numbers are', total_even)
    return total_even
print(sum_of_even(100))

# Declare a function name evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(numbers):
    total_even = 0
    total_odd = 0

    for number in range(numbers):
        if number % 2 == 0:
            total_even = total_even + 1
        if number % 2 != 0:
            total_odd = total_odd + 1
    print('The total numbers of evens are', total_even, '.', 'And the total numbers of odds are', total_odd) 
print(evens_and_odds(100))