import pandas as pd
import numpy as np
# str or object dtype
# country = ['USA', 'Canada', 'London', 'Kingston', 'Germany']

# print(pd.Series(country))

# integer
# run = [24,56,89,100]

# print(pd.Series(run))

#custom Index

# marks = [100, 67, 67, 89, 88]
# subjects = ['English', 'Physics', 'Chemistry', 'Maths', 'Computer Science']

# print(pd.Series(marks, index=subjects))

#Series from dictionary

marks = {
    'English':100,
    'Physics':67,
    'Chemistry':67,
    'Maths':88,
    'Computer Science': 89
}

print(pd.Series(marks, name="Lucky's Marks"))