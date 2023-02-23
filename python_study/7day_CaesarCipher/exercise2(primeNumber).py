# Write your code below this line 👇
def prime_checker(number):
    check = True
    for n in range(2, number):
        if number % n == 0:
            check = False
            break
    if check == True:
        print("it is prime number")
    else:
        print("it is not prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
