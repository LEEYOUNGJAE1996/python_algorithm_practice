# # 230315

# # 파일 열고 데이터 가져오기
# with open('D:\\workstation\\python_algorithm_practice\\python_study\\24day-CSVdata\\weather_data.csv') as dataFile:
#     data = dataFile.read()
#     print(data)

# # 파이썬에서 제공하는 csv 모듈을 사용하는 경우
# import csv
# with open('D:\\workstation\\python_algorithm_practice\\python_study\\24day-CSVdata\\weather_data.csv') as dataFile:
#     data = csv.reader(dataFile)
#     # csv 객체의 형태로 저장되어있다.
#     # csv 형태로 저장하고, 라인을 기준으로 하나의 값으로 저장되어 있다.
#     # TODO: 온도값만 뽑아오기
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(row[1])

#     print(temperatures)


import pandas
# csv 파일을 읽을려고 하는 중이므로
data = pandas.read_csv(
    'D:\\workstation\\python_algorithm_practice\\python_study\\24day-CSVdata\\weather_data.csv')
print(data)
print(data["temp"])
print(type(data))
print(type(data["temp"]))

# Series 활용
# 평균 .mean() 메서드
print("평균 : ", data["temp"].mean())
# 최고값
print("최대값 : ", data["temp"].max())

# get data in column
print(data["condition"])
print(data.condition)

# get data in row
print(data[data["day"] == "Monday"])

# row 데이터 중 특정 데이터 가져오기
print("최고 온도 날 \n", data[data["temp"] == data["temp"].max()])

# 월요일 온도 섭씨를 화씨로 바꾸기
monday_temp = int(data[data['day'] == "Monday"].temp)
f_temp = monday_temp*9/5+32
print("f temp : ", f_temp)

# pandas를 통해 DataFrame 객체 만들기 by dictionary

dictionary = {
    "Student": ["young", "one", "hmm"],
    "scores": [90, 80, 10]
}

# 객체 생성
data = pandas.DataFrame(dictionary)
print(data)
# csv형태로 저장
data.to_csv("./python_study/24day-CSVdata/new_data.csv")
