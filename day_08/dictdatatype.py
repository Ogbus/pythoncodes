# Create a an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog, dictionary
dog['name'] = 'Bingo'
dog['color'] = 'Brown'
dog['breed'] = 'German Dog'
dog['legs'] = 4
dog['age'] = 26
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as key for the dictionary
student = {
    'first_name': 'Felix',
    'last_name': 'Iroms',
    'gender': 'male',
    'age': 56,
    'is_married': True,
    'skills': ['HTML', 'CSS', 'JavaScript', 'Python', '.NET'],
    'country': 'Nigeria',
    'city': 'PH',
    'address': {
        'street': 'Mpape street',
        'zipcode': '902104'
    }
}
# Get the length of student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be list
print(student['skills'])
print(type(student['skills']))
# Modify the skills value by adding one or two skills
student['skills'].append('React')
print(student['skills'])
# Get the dictionary keys as list
print(student.keys())
# Get the dictionary values as list
print(student.values())
# Change the dictionary to a list of tuples using *items() method
dict_to_list = student.items()
print(dict_to_list)
# Delete one of the item in the dictionary
print(student.pop('last_name'))
# Delete the dictionary completely
del student