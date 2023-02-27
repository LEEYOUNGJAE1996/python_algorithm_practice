# 230227

# Instructions
# You are going to write a program that adds to a travel_log.
# You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.

# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above


def add_new_contry(country, times, visited):
    new_country = {}
    new_country["country"] = country
    new_country["visites"] = times
    new_country["cities"] = visited
    # travel_log 정의된 함수 위에 존재해서?? 전역변수 형태로 존재하는 것인가?
    # list가 자체는 레퍼런스 타입이라서 가능한 것인가???
    travel_log.append(new_country)


# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
add_new_contry("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
