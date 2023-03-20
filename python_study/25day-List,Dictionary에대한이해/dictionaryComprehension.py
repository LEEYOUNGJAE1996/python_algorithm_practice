# 230321

# Dictionary Comprehension

# # list 데이터를 키 값으로 활용한 경우
# names = ['이영재', '원', '이', '최', '진', '준', '소다']

# student_score = {student: int(input()) for student in names}
# print(student_score)

# # dictionary를 활용한 경우(조건문 추가)
# # dictionary.items()를 통해  dictionary의 값들을 가져오는 것이 키포인트
# passed_students = {student: grade for (
#     student, grade) in student_score.items() if grade > 60}
# print(passed_students)

# 예제 1
# 단어를 리스트
import pandas
sentence = "What is the airspeed velocity of an swallow?"
sentence_list = sentence.split(" ")
# 단어를 키로 사용하고 단어의 길이를 값으로 가지는 dictionary를 생성
new_dictionary = {word: len(word) for word in sentence_list}
print(new_dictionary)

# 예제2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: temp*9/5+32 for (day, temp) in weather_c.items()}

print('weather_c : ', weather_c)
print('weather_f : ', weather_f)


# pandas 활용한 예제
# pandas 데이터 프레임에서 반복하는 방법
students = {
    "student": ['이영재', '원', '최'],
    'score': [56, 76, 98]
}
student_data_frame = pandas.DataFrame(students)
print(student_data_frame)

# # case 1
# for (key, value) in student_data_frame.items():
#     print(value)
# case 2 loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # dictionary 에서 row값 중 원하는 데이터 가져오기
    print(row.student)
