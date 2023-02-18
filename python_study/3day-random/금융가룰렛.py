import random as rd


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
choice = rd.randint(0, len(names)-1)
print(names[choice], "가 모든 음식값을 다 내야한다.")
