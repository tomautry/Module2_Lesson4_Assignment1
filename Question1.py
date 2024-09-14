# Task 1
import random
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['Happy', 'Sad', 'Energetic', 'Calm']

for day in days_of_week:
    mood = random.choice(moods)
    print(f"On {day} you were feeling {mood}")