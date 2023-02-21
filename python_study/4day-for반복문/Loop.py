# 반복문을 사용하는 연습을 해보자.
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruit + " Juice")


# 평균 높이?
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
sum_high = 0

for n in range(0, len(student_heights)):
    sum_high += int(student_heights[n])
print("반복문" + str(sum_high))
print("제공 함수" + str(sum(student_heights)))
print("반복문" + str(sum_high/len(student_heights)))
print("제공 함수" + str(sum(student_heights)/len(student_heights)))


# 최고 점수 구하기 ?
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores >>").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
max = 0
for score_num in range(0, n):
    if max < student_scores[score_num]:
        max = student_scores[score_num]

print(max)

# for 반복문과 range() 함수S

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(0, 101, 2):
    total += number

print(total)
