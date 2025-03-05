# Lesson 3: Introduction to Python Dictionaries

# Overview:
# In this lesson, we learn how to work with Python dictionaries, a data structure that stores data in key-value pairs. 
# Dictionaries are highly versatile and are used in various scenarios like managing user profiles, storing configurations, and handling inventory.

# Key Concepts:

# 1. **Creating a Dictionary**:
# A dictionary in Python is defined using curly braces {}. It contains key-value pairs, where each key is unique and immutable, 
# and values can be of any data type.
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 2. **Accessing Values in a Dictionary**:
# You can access dictionary values using their corresponding keys.
print(my_dict['name'])  # Output: Alice

# 3. **The .get() method**:
# The .get() method is safer than directly accessing keys because it returns None (or a specified default value) if the key is missing.
print(my_dict.get('age'))  # Output: 25
print(my_dict.get('address', 'Not Available'))  # Output: Not Available

# 4. **Adding Elements to a Dictionary**:
# You can add a new key-value pair by simply assigning a value to a new key.
my_dict['profession'] = 'Engineer'
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}

# 5. **Modifying Elements**:
# To modify an existing value, you assign a new value to an existing key.
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# 6. **Removing Elements**:
# You can use `del` or the `.pop()` method to remove elements from a dictionary.
# Using `del`:
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

# Using `.pop()`:
removed_value = my_dict.pop('profession')
print(removed_value)  # Output: Engineer

# 7. **Dictionary Methods**:
# - `.keys()` returns all the keys in a dictionary.
print(list(my_dict.keys()))  # Output: ['name', 'age']
# - `.values()` returns all the values in a dictionary.
print(list(my_dict.values()))  # Output: ['Alice', 26]
# - `.items()` returns both keys and values as a tuple.
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 26)]

# 8. **Looping Through Dictionaries**:
# You can loop through dictionaries using:
# - Keys: 
for key in my_dict:
    print(key)  # Output: name, age
# - Values:
for value in my_dict.values():
    print(value)  # Output: Alice, 26
# - Key-Value Pairs:
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 26

# 9. **Nested Dictionaries**:
# A nested dictionary is a dictionary where a value is another dictionary.
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {'street': '123 Main St', 'city': 'New York'}
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {'street': '456 Elm St', 'city': 'San Francisco'}
    }
}

# Accessing Nested Dictionary Data:
print(users['user1']['address']['city'])  # Output: New York

# 10. **Looping Through Nested Dictionaries**:
# You can loop through nested dictionaries similarly to how you would loop through a flat dictionary.
for user, info in users.items():
    print(f"User ID: {user}")
    for key, value in info.items():
        print(f"  {key}: {value}")

# Engage & Apply Exercise: Create a Dictionary
# Create a dictionary representing a book with keys like title, author, year, and genre. 
# Add a publisher key and modify the year key as shown in the example.

book = {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'genre': 'Dystopian'
}

# Add publisher
book['publisher'] = 'Secker & Warburg'
# Modify year
book['year'] = 1950

# Final Challenge: Student Grade Program
# Create a program that checks whether students passed or failed based on their grade.

students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")
