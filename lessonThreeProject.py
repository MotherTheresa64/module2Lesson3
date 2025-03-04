# 📓🧠 Engage & Apply: Create a Dictionary  ------------> Original

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

print(book)

# Output
"""
{
    'title': '1984',
    'author': 'George Orwell',
    'year': 1950,
    'genre': 'Dystopian',
    'publisher': 'Secker & Warburg'
}
"""

# 📓🧠 Engage & Apply: Create a Dictionary (Your Own Way) ------------> My Example

movie = {
    'title': 'The Matrix',
    'director': 'The Wachowskis',
    'year': 1999,
    'genre': 'Sci-Fi',
    'rating': 8.7
}

# Add a new key for lead actor
movie['lead_actor'] = 'Keanu Reeves'

# Modify the value for rating
movie['rating'] = 9.0

print(movie)

# Output
"""
{
    'title': 'The Matrix',
    'director': 'The Wachowskis',
    'year': 1999,
    'genre': 'Sci-Fi',
    'rating': 9.0,
    'lead_actor': 'Keanu Reeves'
}
"""

# 👾 Final Challenge: Student Grade Program  ------------> Original

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

# Output 
"""
Alice passed.
Bob failed.
Charlie passed.
David failed.
"""

# 👾 Final Challenge: Student Grade Program (Your Own Way) ------------> My Example

players = {
    'Michael': 30,
    'Kobe': 25,
    'LeBron': 18,
    'Durant': 22
}

for player, score in players.items():
    if score > 20:
        print(f"{player} scored over 20 points.")
    else:
        print(f"{player} scored 20 or fewer points.")

"""
Michael scored over 20 points.
Kobe scored over 20 points.
LeBron scored 20 or fewer points.
Durant scored over 20 points.
"""