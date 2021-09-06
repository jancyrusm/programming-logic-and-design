patinig = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

string = input("Enter string:")
vowels = 0
for i in string:
      if(i == patinig):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

