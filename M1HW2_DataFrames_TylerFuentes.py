# A brief description of the project
# 09/04/2021
# CSC221 M1HW2 – DataFrame
# Tyler Fuentes

import pandas as pd



#a) Defining the dictionary
temps = []
dic = {
       'Maxine' :[65,97,82],
       'James' :[57,86,67],
       'Amanda':[64,78,72] 
       }
#Create the dataframe
temps = pd.DataFrame(dic)
#Print the dataframe
print('a):')
print(temps)
print()

#b) Recreate the dataframe
temps = pd.DataFrame(dic,index=['Morning', 'Afternoon', 'Evening'])
print('b):')
print(temps)
print()

#c) Select the column "Maxine"
print('c):')
c=temps[['Maxine']]
print(c)
print()

#d) Select the row "Morning using the loc[] method
print('d):')
d=temps.loc[['Morning'],:]
print(d)
print()

#e) Select the rows for "Morning" and "Evening using the loc[] method
print('e):')
e=temps.loc[['Morning', 'Evening'],:]
print(e)
print()

#f) Select the data under column "Amanda and row "Morning"
print('f):')
f=temps[['Amanda']].loc[['Morning'],:]
print(f)
print()

#g) Select the data under columns "Amanda, Maxine" and rows "Morning, Afternoon"
print('g):')
g=temps[['Amanda', 'Maxine']].loc[['Morning', 'Afternoon']]
print(g)
print()

#h) Demonstrate use of the describe() method
print('h):')
h=temps.describe()
print(h)
print()

#i) Demonstrate the transpose of the dataframe
print('i):')
i=temps.transpose()
print(i)
print()

#j) Sorting the columns is nothing but reordering the columns.
#   We can use the reorder() method and sorted() method to sort and reorder the columns.
print('j):')
j=temps.reindex(sorted(temps.columns),axis=1)
print(j)
print()









