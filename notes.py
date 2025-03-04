# Dictionaries in Python are a powerful way to store and organize data in pairs. 
# They let you quickly retrieve information using a "key," similar to how you look up a word in a dictionary by its definition. 
# The key can be any immutable data type, like a string or number, and the associated value can be anything, including another dictionary.

# Dictionaries are mutable and allow us to easily add, modify, or remove data. Starting from Python 3.7, they also preserve the order in which items are added, making them even more useful.

# Here's an example of a basic dictionary:
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
# In the example above, we have three key-value pairs. The keys are 'name', 'age', and 'city', with their respective values 'Alice', 25, and 'New York'.

# Accessing Values in a Dictionary
# You can access the values in a dictionary by using the key. 
# If a key exists, the corresponding value is returned.

print(my_dict['name'])  # Output: Alice

# If you try to access a key that doesn’t exist, Python will throw an error. To avoid this, you can use the `.get()` method.
# This method returns None (or a default value you specify) instead of raising an error when the key is not found.

print(my_dict.get('age'))  # Output: 25
print(my_dict.get('address', 'Not Available'))  # Output: Not Available

# Adding, Modifying, and Removing Elements
# Dictionaries are dynamic, so you can easily add, modify, or delete key-value pairs.

# Adding Elements: To add a new key-value pair, simply assign a value to a new key.
my_dict['profession'] = 'Engineer'

# Modifying Elements: You can change an existing value by assigning a new value to an existing key.
my_dict['age'] = 26

# Removing Elements: You can remove items using `del` or the `.pop()` method.
# `del` removes the key-value pair, and `.pop()` removes the key-value pair and returns the value.

# Using del
del my_dict['city']

# Using .pop()
removed_value = my_dict.pop('profession')
print(removed_value)  # Output: Engineer

# Dictionary Methods
# Dictionaries come with built-in methods that help you interact with their data in useful ways.

# .keys(): This method returns all the keys in the dictionary.
print(list(my_dict.keys()))  # Output: ['name', 'age']

# .values(): This method returns all the values in the dictionary.
print(list(my_dict.values()))  # Output: ['Alice', 26]

# .items(): This method returns all the key-value pairs as tuples.
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 26)]

# Looping Through Dictionaries
# You can loop through dictionaries in various ways to access the data. 

# Looping through only the keys
for key in my_dict:
    print(key)

# Looping through only the values
for value in my_dict.values():
    print(value)

# Looping through both keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Nested Dictionaries
# Dictionaries can hold other dictionaries as values, creating a nested structure.

users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

# To access data in a nested dictionary, you use multiple keys.
city_user1 = users['user1']['address']['city']
print(city_user1)  # Output: New York

# You can also modify nested data just like in a flat dictionary.
users['user2']['address']['zipcode'] = '94109'
print(users['user2']['address']['zipcode'])  # Output: 94109

# Adding new elements to a nested dictionary is also simple.
users['user1']['phone'] = '555-1234'
print(users['user1']['phone'])  # Output: 555-1234

# Looping Through Nested Dictionaries
# You can loop through both outer and inner dictionaries using nested loops.

for user, info in users.items():
    print(f"User ID: {user}")
    for key, value in info.items():
        print(f"  {key}: {value}")

# A List of Dictionaries
# Sometimes, you might have multiple dictionaries stored in a list. This is common when managing collections of similar data.

students = [
    {
        'name': 'Alice',
        'age': 25,
        'major': 'Physics'
    },
    {
        'name': 'Bob',
        'age': 22,
        'major': 'Computer Science'
    },
    {
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]

# Accessing data from a list of dictionaries is as simple as indexing into the list and using the keys.
first_student_major = students[0]['major']
print(first_student_major)  # Output: Physics

# Looping Through a List of Dictionaries
# You can loop through a list of dictionaries just like any other list.

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# A List within a Dictionary
# You can also store a list as a value for a key in a dictionary. For example, storing multiple phone numbers or books.

favorite_books = {
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}

# To access a list inside a dictionary, retrieve the list by the key and then work with it like any other list.
alice_books = favorite_books['Alice']
print(alice_books)  # Output: ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice']

second_favorite_bob = favorite_books['Bob'][1]
print(second_favorite_bob)  # Output: Catch-22

# Looping Through Lists Inside a Dictionary
# You can also loop through the dictionary and each list within it.

for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")

# 👾 Final Challenge: Student Grade Program
# This challenge reinforces iterating through a dictionary and applying conditional logic based on the values.

students_grades = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

# Check if each student passed (grade ≥ 50) and print their status.
for student, grade in students_grades.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")
