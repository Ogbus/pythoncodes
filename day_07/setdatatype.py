it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set, it_companies
print(len(it_companies))
# Add 'Twitter' to it companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple it companies at once to the set, it_companies
multiple_it_companies = {'ujiigroceries', 'ujiilearn'}
it_companies.update(multiple_it_companies)
print(it_companies)
# Remove one of the companies from the set, it_companies
it_companies.remove('Facebook')
print(it_companies)
# What is the difference between remove and discard
# The difference between remove and discard is that remove method raises an error the item you want to remove is not found in the set,
# while discard method does not raise any error even when the item is not found in the set.
# Join A and B
set_union = A.union(B)
print(set_union)
# Find A intersection B
inter_section = A.intersection(B)
print(inter_section)
# Is A subset of B
A.issubset(B)
# Are A and B disjoint sets
A.isdisjoint(B)
# Join A with B and B with A
join_C = A.update(B)
print(join_C)

join_D = B.union(A)
print(join_D)
# What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
# Delete the sets completely
del A
del B
# Convert the ages to set and compare the length of the list and the set, which is larger ?
ages = set(age)
print(ages)
# Explain the difference among the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence.