# Jan Cyrus M. Villar 
# BS CoE 1-6

'''
    Write a program that ask a number (with or without decimal point). 
        Print "zero" if the number is zero. 
        Otherwise, print "positive" or "negative". 
        Add "Small" if the number is less than 1, or "Large" if it exceeds 1,000.
'''

print()
numero_str = input("Input a number: ")
numero = float(numero_str)

if numero == 0:
    print("The number is zero.")
    print()
elif 0 < numero and numero > 1000:
    print("The number is large.")
    print()
elif numero <= 1 and numero > 0:
    print("The number is small.")
    print()
elif numero > 1:
    print("The number is positive.")
    print()
elif numero < 0:
    print("The number is negative.")
    print()
