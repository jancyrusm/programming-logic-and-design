# Jan Cyrus M. Villar 
# BS CoE 1-6

'''
Instructions: 
    Write a program that ask a number from the user from 1 to 7 only. 
    Displays the name of the weekday represented by the number. (1 is Monday, and so on)
        Input number: 3
        Wednesday
'''
print()
semana = input("Choose a number between 1 - 7: ")

if semana == "1":
    print("Monday")
    print()
elif semana == "2":
    print("Tuesday")
    print()
elif semana == "3":
    print("Wednesday")
    print()
elif semana == "4":
    print("Thursday")
    print()
elif semana == "5":
    print("Friday")
    print()
elif semana == "6":
    print("Saturday")
    print()
elif semana == "7":
    print("Sunday")
    print()
else:
    print("Error, please input a valid number between 1 - 7.")
    print()

