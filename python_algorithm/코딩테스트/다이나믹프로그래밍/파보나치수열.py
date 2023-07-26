# 230725 
# 중복제거


d = [0] * 100

def pibo(x):
    print('f('+str(x)+')')
    if x == 1 or x ==2 :
        return 1
    if d[x] != 0:
        return d[x]#
    # like DFS
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6)