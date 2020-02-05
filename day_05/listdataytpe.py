# Declare an empty list
emptyList = []
# Declare a list with more than 5 number of items
household_items = ['coffee', 'cereals', 'pots', 'air-conditions', 'chairs']
# Find the length of your list
length = len(household_items)
print(length)
# Get the first item, the middle item and the last item of the list
first_item = household_items[0]
second_item = household_items[1]
third_item = household_items[2]
print(first_item)
print(second_item)
print(third_item)
# Declare a list called mixed_data_types,put your(name, age, height, marital status, address)
mixed_data_types = ['Iroms', 34, 1.6, False, {'address': '9ja'}]
print(mixed_data_types)
# Declare a list variable name it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['facebook', 'google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
first_it_companies = it_companies[0]
second_it_companies = it_companies[3]
third_it_companies = it_companies[-1]
print(first_it_companies)
print(second_it_companies)
print(third_it_companies)
# Print modify any of the companies
it_companies[1] = 'ujiigroceries'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('ujiigroceries')
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'ujiilearn')
print(it_companies)
# Change one of the it_companies item to uppercase
uppercase = it_companies[2].upper()
print(uppercase)
# Join the it_companies with a string '#;  '
joining = '#,'.join(it_companies)
print(joining)
# Check if a certain company exists in the it_companies list.
does_it_exist = 'apple' in it_companies
print(does_it_exist)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
# Slice out the first 3 companies from the list
firts_three_items = it_companies[0:3]
print(firts_three_items)
# Slice out the last 3 companies from the list
last_three_items = it_companies[6:]
print(last_three_items)
# Slice out the middle IT company or companies from the list
middle_item = it_companies[4:3]
print(middle_item)
# Remove the first IT company from the list
it_companies.remove('ujiigroceries')
print(it_companies)
# Remove the middle IT company or companies from the list
it_companies.remove('microsoft')
print(it_companies)
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# Remove all IT companies item
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies
# print(it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
# After joining the lists in question 26. Copy the joined list and assigned it to a variable full_stack. Then insert, Python and SQL after Redux.
full_stack.append('python')
full_stack.append('SQL')
print(full_stack)

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = 19
max_age = 26
# Add the min age and the max age
total_minmax_age = min_age + max_age
print(total_minmax_age)
# Find the median age(one middle item or two middle items divided by two)
# Find the average age(all items divided by number of items)
average_age = ages/2
print(average_age)
# Find the range of the ages(max minus min)
range_of_ages = max_age - min_age
print(range_of_ages)
# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.