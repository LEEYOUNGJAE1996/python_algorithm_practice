# 230720

# 빠르게 입력 받기
# 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
# 위와 같은 상황에서 input()함수를 이용하게 되면 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다
# 이를 피하기 위해 다음과 같은 방법을 사용한다.

import sys

input_data = sys.stdin.readline().rstrip()
# rstrip  > enter로 인한 공백 문자 제거
print(input_data)