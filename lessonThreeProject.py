# Lesson 3: Python Dictionaries - Engage & Apply + Final Challenge

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Pre-provided Exercise: Create a Dictionary representing a book with keys like title, author, year, and genre. 
# Add a publisher key and modify the year.

book = {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'genre': 'Dystopian'
}

# Add a new key for publisher
book['publisher'] = 'Secker & Warburg'

# Modify the value for year
book['year'] = 1950

# Print the updated dictionary
print("Pre-provided Exercise Output:", book)

# ===========================
# engage and apply ---------> Exercise 1 My Version Created
# ===========================

# My Version: Create a dictionary representing a movie. 
# Include keys for title, director, release year, and genre. 
# Add a new key for rating, then modify the release year.

movie = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'release_year': 2010,
    'genre': 'Science Fiction'
}

# Add a new key for rating
movie['rating'] = 8.8

# Modify the value for release year
movie['release_year'] = 2012

# Print the updated dictionary
print("My Version Output:", movie)

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Pre-provided Final Challenge: Write a program that takes a dictionary of students and their grades, 
# then prints each student's name and whether they passed or failed.

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

# ===========================
# final challenge ---------> My Version Created
# ===========================

# My Version: Write a program that takes a dictionary of employees and their sales numbers, 
# then prints each employee's name and whether they met their sales goal (consider the goal to be 100).

employees = {
    'Eve': 150,
    'Mallory': 90,
    'Trent': 120,
    'Peggy': 50
}

for employee, sales in employees.items():
    if sales >= 100:
        print(f"{employee} met the sales goal.")
    else:
        print(f"{employee} did not meet the sales goal.")
