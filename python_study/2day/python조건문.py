# 조건문을 실행 할 수 있다.
# 20230218

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# 짝수  or 홀수 ?
# 주의할점 input으로 받는 데이터는 전부 문자열로 저장된다.
# 출력  또는 계산할 때 숫자와 문자열 데이터 타입을 신경써야한다.
num = input("enter the number >>")
if int(num) % 2 == 0:
    print(num + " is even number. ")
else:
    print(num + " is odd number. ")


# 중복 if 와 elif를 적용
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? >>"))
age = int(input("What is your age? >>"))
if height > 120:
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")

# upgrade BMI 계산기
height = float(input("what's your height?(m) >> "))
weight = float(input("what's your weight?(kg) >> "))

BMI = round(weight / height**2, 2)

print("You're BMI is " + str(BMI))
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal weight")
elif BMI < 30:
    print("overweight")
else:
    print("clinically obese")

# 윤년 계산기
# 4로 나눠지는 경우 366  / 100으로 나눠지는 경우는 제외/ 단! 400으로 나눠지는 경우 윤년이다.
year = int(input("enter the year >> "))

if year % 4:
    if year % 400:
        print("윤년")
    elif year % 100:
        print("윤년 아님")
    else:
        print("윤년")
else:
    print("윤년 아님")
