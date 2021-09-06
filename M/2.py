'''
Jan Cyrus M. Villar 
BS CoE 1-6
   Write a program that get your name and print is backward one line per letter.
      What is your name? Danilo
      o
      l
      i
      n
      a
      D
'''

pangalan = []

print()
pangalan = input("What is your name? ")
if pangalan not in pangalan: 
      pangalan.append(pangalan)
for char in reversed(pangalan):
    print(char)