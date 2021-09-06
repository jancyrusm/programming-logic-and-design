'''
Jan Cyrus M. Villar 
BS CoE 1-6
    Write a program to read n numbers and count the odd numbers and even numbers.
    How many numbers? 5
    Enter number #1: 12
    Enter number #2: 11
    Enter number #3: 13
    Enter number #4: 10
    Enter number #5: 5
    Even numbers count is 2
    Odd number count is 3
'''
ilan = int(input('How many numbers? '))
tick = 0

numero = [] 
for i in range(0, ilan):
    numero.append(input('Enter number #%d: ' %(1 + tick)))
    tick = tick + 1 #para to sa enter number#

#convert string to integer sa list na nasa numero 
numero = [int(i) for i in numero] 

mga_even = [i for i in numero if i % 2 == 0 or i == 0] 
bilang_ng_even = len(mga_even) 
mga_odd = len(numero) - bilang_ng_even
   
print("Odd number count is", mga_odd) 
print("Even number count is", bilang_ng_even) 
  
