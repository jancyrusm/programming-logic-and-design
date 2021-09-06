# Jan Cyrus M. Villar 
# BS CoE 1-6

'''
    Write a program that accepts three numbers and prints "All numbers are equal" if all three numbers are equal, "All numbers are different" if all three numbers are different. If only one is different, print that number.
        Input first number: 256
        Input second number: 352
        Input third number: 256
        352 is different
'''
print()
panguna = int(input("Please input the 1st number: "))
pangalawa = int(input("Please input the 2nd number: "))
pangaltlo = int(input("Please input the 3rd number: "))

if panguna == pangalawa == pangaltlo:
    print("All numbers are equal.")
    print()
elif panguna != pangalawa != pangaltlo:
    print("All numbers are different.")
    print()
elif panguna == pangalawa != pangaltlo:
    print(pangaltlo, "is different.")
    print()
elif pangaltlo == pangalawa != panguna:
    print(panguna, "is different.")
    print()
elif panguna == pangaltlo != pangalawa:
    print(pangalawa, "is different.")
    print()

