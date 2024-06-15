#Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#Load dataframe paths
book_path = r"C:\Users\kwame\git\book_rec2024\book_rec2024-1\Ratings.csv"
users_path = r"C:\Users\kwame\git\book_rec2024\book_rec2024-1\Users.csv"
bookdata = pd.read_csv(book_path)
usersdata = pd.read_csv(users_path)
#Merge dataframe & test the raw results
bookdf = pd.concat([bookdata, usersdata])
bookdf['Location'] = bookdf['Location'].fillna("USA")
bookdf['Age'] = bookdf['Age'].fillna(bookdf['Age'].mean())
bookdf['ISBN'] = bookdf['ISBN']
print(bookdf.head(5))


