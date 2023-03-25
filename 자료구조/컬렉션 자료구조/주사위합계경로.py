# 230326

# 주사위 합계 경로
# 주사위 두 번 던져서 합계가 특정 수가 나오는 경우의 수와 경로를 구한다.
from collections import Counter, defaultdict

def find_dice(s, n_faces = 6):
    if s > 2 * n_faces or s < 2 :
        return None
    
    cdict = Counter()
    ddict  = defaultdict(list)

    # 두 주사위의 합을 모두 더해서 딕셔너리에 넣는다.
    for dice in range(1, n_faces+1):
        for dice2 in range(1,n_faces+1):
            t = [dice, dice2]
            cdict[dice+dice2] +=1
            ddict[dice+dice2].append(t)
    return [cdict, ddict]

def find():
    s = 5
    result = find_dice(s)
    print(result)
    if(result[0][s] == len(result[1][s])):
        print('success')

if __name__ == '__main__':
    find()
