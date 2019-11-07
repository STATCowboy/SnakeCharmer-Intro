#
# Author: Jamey Johnston
# Title: Code Like a Snake Charmer: Introduction to Python!
# Date: 2019/11/07
# Blog: http://www.STATCowboy.com
# Twitter: @STATCowboy
# Git Repo: https://github.com/STATCowboy/SnakeCharmer-Intro
#

#
# Comments
#

# Single Line Comment


'''
Multi Line Comment (Three Single Quotes Before and After)
You can have more then one line!
'''


# Print Statements
print('Welcome to PASS Summmit 2019!!')


#
# Numbers
#

x = 3 + 5
print(x)

taxRate = 8.25 / 100
price = 100
tax = price * taxRate
finalPrice = price + tax

print('Tax: ${:,.2f}'.format(tax))
print('Final Price: ${:,.2f}'.format(finalPrice))



#
# Strings
#

# Simple string
simpleString = 'This is a simple string!'
print(simpleString)

simpleStringDouble = "This is a simple string!"
print(simpleStringDouble)

# Escape "'" (single qoutes) with "\" (slash)
print('Isn\'t Pass Summit Awesome')

# Span String Literals Multiple Lines
print("""\
Usage: magicSummitPass [OPTIONS]
     -h                        Display this usage message
     -S year                   Magically get me into Summit that year for free!
""")

# Repeat Strings with "*" and concatenate with "+"
espn = 3*'duh '+' (we still wish MJ was playing!)  '+3*'duh '
print(espn)


# Slicing/Indices on Strings (positive indexes start at 0 and negative start with -1)

passSummit = 'PASS Summit 2019'
passSummit[0]
passSummit[15]
passSummit[-1]
passSummit[-16]

passSummit[0:8]  # characters from position 0 (included) to 8 (excluded)

# Start is always included, End always excluded, So s[:i] + s[i:] is always equal to s:
passSummit[:8] + passSummit[8:]

# Guide to help with Indices
'''
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | A | S | S |   | S | u | m | m | i | t |   | 2 | 0 | 1 | 9 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
-16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  
'''

# Strings are Immutable (i.e. you can't change them - following will error)
passSummit[12:16] = '2020 in Houston!'


# len() function returns length of string
len(passSummit)


#
# List
#
myList = [1,2,3,4]
print(myList)

# Indices and Slicing
myList[0]
myList[-3:] # slicing returns a new list

# Concatenate Lists
myNewList = myList + [5,6,7,9]
print(myNewList)

# List are mutable (you can change them!)
myNewList[7] = 8
print(myNewList)

# Append to a List
myNewList.append(9)
print(myNewList)

# Replace a slice (even with a different size)
myNewList[2:4] = [1,1]
print(myNewList)

# len() will return length of list
len(myNewList)




#
# Tuples
#

# Tuple consists of a number of values separated by commas
t = 'PASS', 'Summit', '2019'
print(t)

# Tuples may be nested
nt = t, ('is', 'awesome', '!')
print(nt)

# Tuples are Immutable (i.e. you can't change them - following will error)
t[2] = '2020 in Houston!'

# Tuples can contain mutable objects like list, for example
tl = [1,2], [3,5]
print(tl)

tl[1][1] = 4
print(tl)



#
# Dictionaries
#

# Dictionaries are unordered key/value pairs
yearBirth = {'jamey': 1974, 'melanie': 1975, 'jeanna': 1989, 'stefanie': 1976, 'robyn': 1979}
print(yearBirth['jamey'])

# Delete item in Dictionary
del yearBirth['robyn']
print(yearBirth)

# List Keys (unordered)
list(yearBirth.keys())

# List Keys (Sorted)
sorted(yearBirth.keys())



#
# Pandas
#

# Import Pandas and Read CSV
import pandas as pd
baseball = pd.read_csv('baseball.csv', sep=',', encoding='UTF-8')

# Type of object (DataFrame)
type(baseball)

# Print header of pandas DataFrame
baseball.head()

#  Print tail of pandas DataFrame
baseball.tail(3)

# Print column names
baseball.columns

# Describe DataFrame
baseball.describe()

# Sort by Column
baseball.sort_values(by='Attendance')

# Select one Column
baseball[['Team']]

# Group By
baseballMean = baseball.groupby('Team').mean()
print(baseballMean.sort_values(by='Attendance')[['Attendance']])




#
# Control Flows
#

#
# if ... elif ... else
#
n = 5
m = 10
if n < 10 and m <  10:
    print('n and m are single digit numbers!')
elif n >= 10 and m < 10:
    print('n is a big number and m is a single digit number!')
elif n < 10 and m >= 10:
    print('n is a single digit number and m is a big number!')
else:
    print('n and m are big number!')

# In operator on List
if 2 in [1, 2, 3, 4]:
    print('Found it!')
else:
    print('Keep looking!')


#
# for Loops
#

# Simple For Loops
for i in [1, 2, 3, 4]:
    print(i)

wordList = ['Jamey', 'Melanie', 'Stefanie', 'Robyn']
for word in wordList:
    print('Family member name:', word)

# Range function
r = range(5)
print(r)
for num in r:
    print(r[num])


# Loop over two or more lists
questions = ['name', 'birth year', 'occupation']
answers = ['Jamey Johnston', '1974', 'Data Scientist']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# Retrieve Key/Value of List in Loop, Sorted by Key
yearBirth = {'jamey': 1974, 'melanie': 1975, 'jeanna': 1989, 'stefanie': 1976, 'robyn': 1979}
for k, v in sorted(yearBirth.items()):
    print(k, 'was born in the year ', v)

# break, continue and else in for loops
# (https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


#
# while Loops
#

# Simple while Loop
num = 0
while num < 10:
    print(num)
    num = num+1


# break and continue in while loops and try ... except
while True:
    txt = input('Enter number (integers only!):')
    try:
        integer = int(txt)
    except:
        print('Please enter integer only!')
        continue
    print('You entered the integer,', integer)
    break
print('Done!')



#
# Functions
#

# Simple Function
# NOTE: non-default parameters must be first!
def greetSummit(year, name=None):
    if name is not None:
        print('Welcome to PASS Summit ', year, ', ', name, '!', sep='')
    else:
        print('Welcome to PASS Summit ', year, '!', sep='')

greetSummit(2019)
greetSummit(2019, 'James')

# Print Fibonacci series (https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
def fib(n=100):    # write Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fibDef = fib()
fib50 = fib(50)

print(fibDef)
print(fib50)



#
# Packages
#

# import sys and show Python version and distibution
import sys
sys.version

# PYODBC/Pandas Example with Plots in Seaborn and Matplotlib
import pyodbc
import pandas.io.sql as psql

import seaborn as sns
import matplotlib.pyplot as plt

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=analytics;Integrated Security=TRUE')
cursor = cnxn.cursor()
sql = ("""SELECT [Team]
      ,[Attendance]
      ,[Temp]
      ,[Win%]
      ,[OpWin%]
      ,[Weekend]
      ,[Promotion]
  FROM [analytics].[dbo].[Baseball]""")

df = psql.read_sql_query(sql, cnxn)
cnxn.close()

df.to_csv('baseball.csv', sep=',', encoding='utf-8', index=False)

sns.pairplot(df)

g = sns.PairGrid(df, diag_sharey=False)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot, lw=3)
