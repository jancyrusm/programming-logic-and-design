# Jan Cyrus M. Villar 
# BS CoE 1-6

'''
    Write a program that accepts three numbers from the user and prints "increasing" if the numbers are in increasing order, "decreasing" if the numbers are in decreasing order, and "Neither increasing or decreasing order" otherwise.
'''

print()
una = float(input("Please input the 1st number: "))
ikalawa = float(input("Please input the 2nd number: "))
ikatlo = float(input("Please input the 3rd number: "))

if una > ikalawa > ikatlo: 
    print("The numbers are decreasing in order.")
    print()
elif una < ikalawa < ikatlo: 
    print("The numbers are increasing in order.")
    print()
else:
    print("The numbers are neither increasing or decreasing in order.")
    print()

