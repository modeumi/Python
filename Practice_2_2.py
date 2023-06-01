var = total = 0
# list = [] # 올바른 값이 들어가는지 확인하기위한 list
while var < 100 :
    var += 1
    if var %2 != 0 :
        if total >= 0 :
            total -= var
            # list.append(-var)
        elif total<0 :
            total += var
            # list.append(var)
print(total)
# print(list[:25]) # list 출력물이 한줄로 너무 길게나와서 두줄로 잘랐음!
# print(list[25:])