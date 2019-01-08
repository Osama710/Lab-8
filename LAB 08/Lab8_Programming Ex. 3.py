print("Muhammad Osama   18b-003-cs  CS-(A)")
print("Lab-08   28/12/2018")
print("Programming Exercise: Q-3")
"""3. Write function even() that takes a positive integer n as input and prints on the screen all
numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
even(17)
2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,"""
def even(n):
    for i in range(2,n):
        if i%2 == 0 and i%3 == 0:
            print(i,'divisible by both 2 and 3', end='\n')
        elif i%2 == 0:
            print(i, 'divisible by 2', end='\n')
        elif i%3 == 0:
            print(i,'divisible by 3', end='\n')
even(17)
