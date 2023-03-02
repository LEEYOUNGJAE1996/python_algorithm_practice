# 230302
################### Scope ####################

enemies = 1


def increase_enemies(enemies):
    # 전역 변수임을 알림
    # global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
