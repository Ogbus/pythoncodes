# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
concatunate = ['Thirty', 'Days', 'Of', 'Python']
full_sentence = ' '.join(concatunate)
print(full_sentence)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
string = ['Coding', 'For', 'All']
string_sentence = ' '.join(string)
print(string)

# Declare a variable name company and assign it to an initial value "Coding For All.
company = 'Coding For All'
# Print company using print()
print(company)
# Print the length of the company string using len() method and print()
print(len(company))
# Change all the characters to capital letters using upper() method
print(company.upper())
# Change all the characters to lowercase letters using lower() method
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value the string Coding For All.
print(company.capitalize())
print(company.swapcase())
print(company.title())
# Cut(slice) out the first word of Coding For All string
remove_coding = company[7:15]
print(remove_coding)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
# Change Python for Everyone to Python for All using the replace method or other methods
sentense = 'Python for Everyone'
print(company.replace('Everyone', 'All'))
# Split the string 'Coding For All' at the space using split() method
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
# What is character at index 0 in the string Coding For All.
first_letter = company[0]
print(first_letter)
# What is the last index of the string Coding For All
lastLetter = company[-1]
print(lastLetter)

# What character is at index 10 in "Coding For All" string.
tenth_index = company[10]
print(tenth_index)
# Create an acronym or an abbreviation for the name 'Python For Everyone'
print(''.join(w[0] for w in sentense.split()))
# Create an acronym or an abbreviation for the name 'Coding For All'
print(''.join(x[0] for x in company.split()))
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All
print(company.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_l = 'l'
print(company.find(last_l, 13))
# Use index or find to find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
text = 'You cannot end a sentence with because because because is a conjunction'
first_because = 'because'
print(text.find(first_because))
# Use rindex to find the position of the last occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
last_because = 'because'
print(text.find(last_because, 56))
# Slice outr the phrase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print(text[31:54])
# Find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
ferst_because = 'because'
print(text.find(ferst_because))
# Slice out the phase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
because = text[31:54]
print(because)
# Does Coding For All starts with a substring Coding?
print(company.startswith('Coding'))
# Does Coding For All ends with a substring coding?
print(company.endswith('Coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
trailing = '   Coding For All      '
print(trailing.strip())

# Which one of the following variable return True when we use the method isidentifier()30DaysOfPython, thirty_days_of_python
correct_id = 'thirty_days_of_python'
incorrect_id = '30daysofpython'
print(correct_id.isidentifier())
print(incorrect_id.isidentifier())
# The following are some of python libraries list: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#, '.join(python_libraries))
# Use new line escape sequence to writ the following sentence.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
# Use a tab escape sequence to writ the following sentence.
# Name      Age     Country
# Asabeneh  250     Finland
print('Name\tAge\tCountry\nFelix\t45\tNigeria')
# Use string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of radius 10 is 314 meters squares. 
radius = 10
area = 3.14 * radius ** 2
result = 'he area of the radius {} is {:.3f}.'.format(radius, area)
# Make the following using string formatting methods:
num1 = 8
num2 = 6
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')
