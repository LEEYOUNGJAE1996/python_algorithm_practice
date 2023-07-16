# 230716

stack = []
count = 0
def stackPush(stack, data, count):
    count += 1
    stack.append(data)
    return stack, count

def stackPop(stack, count):
    if count <= 0 :
        print("안에 데이터가 없습니다.")
        return stack, None, count
    else :
        count -= 1
        return stack, stack.pop(), count

stack, count = stackPush(stack,10,count)
print(stack)
stack, data, count = stackPop(stack, count)
print(stack , data)
stack, data, count = stackPop(stack, count)
print(stack , data)