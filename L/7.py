# Jan Cyrus M. Villar 
# BS CoE 1-6

'''
    Ask three numbers from the user then print the greatest number.
        Input the 1st number: 26
        Input the 2nd number: 79
        Input the 3rd number: 89
        The greatest: 89
'''

print()
primero_float = input("Please input the 1st number: ")
segundo_float = input("Please input the 2nd number: ")
tercero_float = input("Please input the 3rd number: ")

primero = float(primero_float)
segundo = float(segundo_float)
tercero = float(tercero_float)

if primero < segundo < tercero:
    print("The greatest number is:", tercero)
    print()
elif primero < tercero < segundo:
    print("The greatest number is:", segundo)
    print()
elif tercero < segundo < primero:
    print("The greatest number is:", primero)
    print()