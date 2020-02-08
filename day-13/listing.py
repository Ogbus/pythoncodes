# Filter only negative or zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_negative = [i for i in numbers if i < 0 or i == 0]
print(filter_negative)

positive_integer = [i for i in range(21) if i % 2 == 0]
print(positive_integer)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [number for row in list_of_lists for number in row]
flat_list_again = [nums for row in flat_list for nums in row]
print(flat_list_again)

# Change the following list to a flatten list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flaten_list = [flat for row in countries for flat in row]
flaten_list_again = [flat for row in flaten_list for flat in row]
print(flaten_list_again)