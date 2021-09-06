ilan = int(input('How many numbers? '))
tick = 0

numero = [] 
for i in range(0, ilan):
    numero.append(input('Enter number #%d: ' %(1 + tick)))
    tick = tick + 1