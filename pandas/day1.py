import pandas as pd
import numpy as np
# str or object dtype
# country = ['USA', 'Canada', 'London', 'Kingston', 'Germany']

# print(pd.Series(country)) we are creating one object of class "Series".

# integer
# run = [24,56,89,100]

# print(pd.Series(run))

#custom Index

# marks = [100, 67, 67, 89, 88]
# subjects = ['English', 'Physics', 'Chemistry', 'Maths', 'Computer Science']

# print(pd.Series(marks, index=subjects))

#Series from dictionary

# marks = {
#     'English':100,
#     'Physics':69,
#     'Chemistry':67,
#     'Maths':88,
#     'Computer Science': 89
# }

# LUCKYsMARKS = pd.Series(marks, name="Lucky's Marks")


### Most used attributes in Series class

# print(LUCKYsMARKS.size)

# print(LUCKYsMARKS.dtype)

# print(LUCKYsMARKS.name)

# print(LUCKYsMARKS.is_unique)

# print(LUCKYsMARKS.index)

# print(LUCKYsMARKS.values)

# Deal with CSV

## csv with one column

# subs = pd.read_csv("/home/lucky/KPP/subs.csv").squeeze()
# print(type(subs))
# print(subs)

##csv with two columns

# runs = pd.read_csv("kohli_ipl.csv",index_col='match_no').squeeze()
# print(runs)

# Head and Tail - prints first five rows or we can pass a by default how many rows we want to see
movies = pd.read_csv("bollywood.csv",index_col='movie').squeeze()
# print(movies.tail(10))
# print(movies.head())

#sample - takes out one row -"Randomly"

# print(movies.sample(5))
print(movies.value_counts())