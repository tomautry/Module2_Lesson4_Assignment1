# Task 1

import random
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['happy', 'sad', 'energetic', 'calm']
times_of_day = ['morning', 'afternoon', 'evening']

for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f'\nOn {day} {time} you were {mood}')