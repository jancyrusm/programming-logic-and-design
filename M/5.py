'''
Jan Cyrus M. Villar 
BS CoE 1-6
    Write a Python program that ask a number then construct the following pattern base on user input:
        Input a number? 9
        1
        22
        333
        4444
        55555
        666666
        7777777
        88888888
        999999999
'''
print()
tantum = int(input('Input a number: '))

print()
tantum = tantum + 1

for tantum in range(1, tantum):
    print(str(tantum) * tantum)
print()