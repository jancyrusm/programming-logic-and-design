'''
Jan Cyrus M. Villar 
BS CoE 1-6
    Write a program that get your name and print and number of vowels.
        What is your name? Danilo
        You have 3 vowels
'''

patinig = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
name = []

pangalan = input('What is your name? ')
name.append(pangalan)

#separate word sa list na "name" into seperate letters
#ex: ['cyrus'] to ['c', 'y', 'r', 'u', 's']
name = [i for char in name for i in char] 

#bilangan kung ilan yung vowels sa list na "name"
count = 0
for char in name:
    if char in patinig: 
        count += 1
print ('You have ' + str(count) + ' vowels.') 
