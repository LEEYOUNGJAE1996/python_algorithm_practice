# 0808

# 문자열 압축

string  = input()


countingLength = 9999999 
for letterLength in range(1,len(string)//2+1):
    previous = string[0:letterLength]
    result = []
    count = 1
    for i in range(letterLength,len(string),letterLength):
        now = string[i:i+letterLength]
        if previous == now:
            count += 1
        else :
            # 축약된 숫자
            result.append(count)
            count = 1 
            result.append(previous)
            previous = now
    countingLength = min(countingLength, len(result))


