# 230808

numbers = input()
first = 0
second = 0

for numberIndex in range(len(numbers)//2):
    first += int(numbers[numberIndex])
for numbersIndsex in range(len(numbers)//2, len(numbers)):
    second += int(numbers[numberIndex])

if first % 6 == 0 and second %6  == 0 :
    print("LUCKY")
else :
    print('READY')