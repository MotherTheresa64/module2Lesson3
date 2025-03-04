# Module 2 Lesson 3
# Noah Ragan
## 📓🧠 Engage & Apply: Create a Dictionary 

### 📝 Exercise: Create a dictionary that represents a book 📖

Include keys like title, author, year, and genre. Write code to add a new key for publisher, and modify the value for year.

In this exercise, we use dictionaries to model more complex data. By adding new keys 🔑 and modifying existing ones, students get a hands-on understanding of dictionary dynamics.

```python
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
```

The dictionary `book` starts with basic information ℹ️. We then add a new key 🔑 'publisher' and update the 'year' to show how easy it is to manipulate dictionary data.

## 👾 Final Challenge: Student Grade Program

### 🏆 Challenge: Write a program that takes a dictionary of students 👨‍🎓 and their grades, then prints 🖨️ each student's name and whether they passed ✅ or failed ❌ (consider passing as a grade ≥ 50).

This challenge aims to reinforce iteration 🔄 through a dictionary and using conditional logic to determine outcomes based on data stored within.

```python
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
```

In this example, the program iterates over each student in the `students` dictionary, checks their grade, and prints whether they passed or failed. This demonstrates how to efficiently access key-value pairs and apply logic to data.