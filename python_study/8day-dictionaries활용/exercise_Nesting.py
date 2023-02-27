# 230227
# France를 기준으로 cities_visited dictionary 안에 도시들 list형태로

# 강의를 듣기전 방식
cities_visited = {
    "France": ["Prais", "Lille", "Dijon"]
}

travel_log = {
    "France": cities_visited["France"]
}

# 강의에서 한 방식
# 다른 점
# France에서 바로 Dictionary형태의 값을 중괄호로 만들어준 후
# 그 안에서 값을 구분
# 강의를 보기 전에 나의 경우는 외부에서 또 하나의 Dictionary를 만들어 값을 지정
# 강의에서 한 방식은 다른 딕션어리를 통해 다른 Key를 계속 추가하기 good
travel_log_lec = {
    "France": {"cities_visited": ["Prais", "Lille", "Dijon"], "total_visites": 12}
}

print(travel_log)
print(travel_log_lec)
