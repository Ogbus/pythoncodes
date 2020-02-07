# Iterate 0 to 10 using for loop, do the same using while and do while loop.
# for loop
counts = [0,1,2,3,4,5,6,7,8,9,10]
for count in counts:
    print('for loop', count)

# while loop
num = 0
while num < 10:
    print('while loop',num)
    num = num + 1

# do-while loop
numbers = 0
while True:
    print(numbers)
    numbers = numbers + 1
    if numbers > 10:
        break

# Iterate 10 to 0 using for loop, do the same using while and do while loop.
# while loop decrement
numbs = 10
while numbs > 0:
    print('reverse while', numbs)
    numbs = numbs - 1

# for loop decrement
for digits in range(10, 0, -1):
    print(digits)

# Write a loop that makes seven calls to print() output the following triangle:
for i in range(0, 7):
    for n in range(0, i+1):
        print('# ', end='')
    print('\r')

multiple = 0
while multiple < 12:
    print('${multiple} * ${multiple} = ', multiple * multiple)
    multiple = multiple + 1

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
frameworks = ['Python', 'Numpy','Pandas','Django', 'Flask']
for framework in frameworks:
    print(framework)

# Use for loop to iterate from 0 to 100 and print only even numbers
for even in range(0, 100):
    if even % 2 == 0:
        print(even)
    else:
        pass

# Use for loop to iterate from 0 to 100 and print only odd numbers
for odd in range(0, 100):
    if odd % 2 != 0:
        print(odd)
    else:
        pass

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
num_sum = 0
print(num_sum)
for numbers in range(1, 101):
    num_sum += numbers
print('The sum of all numbers is', num_sum)
print(num_sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0

for integers in range(0, 101):
    if integers % 2 == 0:
        even_sum += integers
    if integers % 2 != 0:
        odd_sum += integers
print('The sum of all even numbers is', even_sum, '.', 'And the sum of all odd numbers is', odd_sum)