# 1번쨰 칸부터 옆칸과 비교를 진행하며
# 그 과정이 끝까지 진행되는 정렬

def bubleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break ;
    if isSorted:
        print(" 정렬완료")
    else:
        print("정렬 오루 발생")

import random , time

N = 5000
a = []
a.append(None)
for i in range (N) :
    a.append(random.randint(1,N))
start_time = time.time()
bubleSort(a,N)
end_time = time.time() - start_time
print("버블 정렬 시간 (N = %d) : %f0.3"%(N,end_time))
checkSort(a,N)

