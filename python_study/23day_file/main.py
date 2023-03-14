# 230315
# open method

# 넣을 변수 = open("열고자 하는 파일 이름.확장자까지")

with open(
        "D:\\workstation\\python_algorithm_practice\\python_study\\23day_file\\my_file.txt", mode="a", encoding='UTF8') as file:
    file.write("\n꼭 잘될거다!! 계속 배우며 만족하는 삶을 살거다!!!")


# read
with open(
        "D:\\workstation\\python_algorithm_practice\\python_study\\23day_file\\my_file.txt", encoding='UTF8') as file:
    print(type(file))
    contents = file.read()
    print(contents)
# file = open(
#     "D:\\workstation\\python_algorithm_practice\\python_study\\23day_file\\my_file.txt", encoding='UTF8')
# print(type(file))
# contents = file.read()
# print(contents)
