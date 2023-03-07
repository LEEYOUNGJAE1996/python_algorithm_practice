# 230307

class User:
    # 생성자
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        print("new user being created")

    # method 정의
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "0jae")
user_2 = User("002", "bo1")

print(user_1.id, user_1.username, user_1.followers)
print(user_2.id, user_2.username, user_2.followers)

user_1.follow(user_2)
print(user_1.id, user_1.username, user_1.followers)
print(user_2.id, user_2.username, user_2.followers)
