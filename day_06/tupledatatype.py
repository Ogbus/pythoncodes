# Create an empty tuple
empty_tuple = ()
# Create a tuple containing name of your sisters and your brothers
brothers = ('felix', 'Iroms', 'Junior', 'mike')
sisters = ('joy', 'florence', 'nkeshi')
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# How many siblings do you have ?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('webber')
family_members.append('angella')
# Unpack siblings and parents from family_members
del family_members
# Create a fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff.
fruits = ('mango', 'guava', 'apple', 'strawberry')
vegetables = ('cucumber', 'broccoli', 'cauliflower')
animal_product = ('corned-beef', 'hot dog')
food_stuff = fruits + vegetables + animal_product
print(food_stuff)
# Slice out the middle item or items from the food_staff list
# Slice out the first three items and the last three items from food_staff list
food_stuff[0:3]
# Check if an item exist in a tuple:
does_exist = 'cucumber' in food_stuff
print(does_exist)
# Delete the food_staff list completely
del food_stuff
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
is_estonia = 'Estonia' in nordic_countries
print(is_estonia)
# Check if 'Iceland' is a nordic country
is_iceland = 'Iceland' in nordic_countries
print(is_iceland)