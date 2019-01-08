print("Muhammad Osama   18b-003-cs  CS-(A)")
print("Lab-08   28/12/2018")
print("Programming Exercise: Q-7")
"""7. Implement function cheer() that takes as input a team name (as a string) and prints a cheer as shown:
>>> cheer('uitians')
How do you spell winner?
I know, I know!
U I T I A N S !
And that's how you spell winner!
Go Uitians!"""
def cheer(x):
    print('How do you spell winner?')
    print('I know, I know!')
    for i in x:
        print(i.upper(),end=' ')
    print('!')
    print('And thats how you spell winner!')
    print('Go', x.title(),'!')
cheer('uitians')