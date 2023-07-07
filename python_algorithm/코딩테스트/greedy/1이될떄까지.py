# 230707

# 1이 될 때까지
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다. (단. 2번의 과정은 K로 N이 딱 나누어지는 경우 진행한다.)

# 이 과정을 수행해야 한느 최소 횟수를 구하는 프로그램을 작성하세요
import time
n, k = map(int, input().split())
startTime = time.time()
count = 0
while n != 1:
    if n % k == 0 :
        n /=k
    else :
        n -= 1
    count += 1 

print(count)
endTime = time.time()
print(endTime - startTime)


# 책에서 설명한 방법이 더욱 시간이 절약된다. 
# Why???
n, k = map(int, input().split())
startTime = time.time()
count = 0
while n >= k:
    while n % k != 0:
        n -=1
        count +=1
    n //= k 
    count += 1 
print(count)
endTime = time.time()
print(endTime - startTime)


# reason 두 코드는 기본적으로 동일한 알고리즘을 사용하지만, 두 코드의 실행 시간 차이는 입력 값인 ‘N’의 크기에 따라 결정됩니다. 
# 첫 번째 코드에서는 while문을 한 번 돌 때마다 'N'에서 1을 빼면서, 몫(quotient)을 계산합니다. 이 작업은 'N'의 크기가 커질수록 오래 걸립니다. 
# 두 번째 코드에서는 먼저 'N'을 'K'로 나누어 떨어지게끔(나머지가 0이 되도록) 하고, 그 몫을 'N'에 대입합니다. 
# 이 작업으로 'N'이 'K'의 배수가 되는 경우 'N'이 크게 줄어듭니다. 이후 'N'이 'K'보다 작아지면 이제는 1을 빼줍니다. 앞선 방법에 비해 while문의 반복 횟수가 적어져서 수행 시간이 감소됩니다.