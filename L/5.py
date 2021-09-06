# Jan Cyrus M. Villar 
# BS CoE 1-6

'''
    Ask a letter from the user, print Vowel or Consonant, depending on the user input. If the user input is not a letter, or or more than 1 character, print an error message.
        Input an alphabet: x
        Input letter is Consonant
'''

patinig = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
katinig = ["b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

print()
letra = str(input("Input a letter: "))

if letra in patinig:
    print("The letter is a vowel.")
    print()
elif letra in katinig:
    print("The letter is a consonant.")
    print()
else:
    print("Error! That's not a letter.")
    print()