from decimal import Decimal

# sum안에 동작 ==> 0.1이 10개가 포함된 list를 생성 --> sum을 통해 list내의 값 전부 합
print(sum(0.1 for i in range(10)) == 1.0)
# decimal 모듈을 통해
print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
