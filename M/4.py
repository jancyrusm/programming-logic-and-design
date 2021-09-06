'''
Jan Cyrus M. Villar 
BS CoE 1-6
    Write a Python program that ask width and height of a box then print the box:
        Input a width? 6
        Input a height? 6
        * * * * * *
        *         *
        *         *
        *         *
        *         *
        * * * * * *
'''

tangkad = int(input('Input a height? '))
lapad = int(input('Input a width? '))

#width ng taas
print(("*" + " ") * lapad)

#center
for i in range(tangkad):
    spaces = (lapad - 2) * "  "
    print("*" + spaces + " " + "*")

#width ng baba
print(("*" + " ") * lapad)


