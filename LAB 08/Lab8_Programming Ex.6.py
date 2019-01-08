print("Muhammad Osama   18b-003-cs  CS-(A)")
print("Lab-08   28/12/2018")
print("Programming Exercise: Q-6")
"""6. Write a function month() that takes a number between 1 and 12 as input and returns the three-character abbreviation of the corresponding month. Do this without using an if
statement, just string operations. Hint: Use a string to store the abbreviations in order.
>>> month(1)
'Jan'
>>> month(11)
'Nov'"""

def month(x):
    months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
    print(months[x-1])
month(1)
month(11)

