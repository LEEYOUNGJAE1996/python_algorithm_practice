score = 0
height = 1.8
isWinning = True
# f-string
print(
    f"your score is {score}, your height is {height}, you are winning? {isWinning}")

# 90세까지 살 수 있다는 가정하에 남은 주를 구하는 방법
age = input("What is your current age?")
years_remaining = 90 - int(age)
days_remainng = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(
    f"You have {days_remainng} days, {weeks_remaining} weeks, {months_remaining} months")
