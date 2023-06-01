# 별찍기 왼쪽 정렬
for k in range(2,7):
    for j in range(1,k):
        print("*", end="")
    print("")

# 왼쪽 정렬 다른 풀이
for i in range(1,6) :
    print("*"*i)

# 별찍기 오른쪽 정렬
for k in range(1,6).__reversed__() :
    for j in range(1,6) :
        if k<=j :
            print("*",end ="")
        else:
            print(" ",end = "")
    print()
# 오른쪽 정렬 다른 풀이
for k in range(1,6) :
    print(" "*(5-k)+"*"*k)

#별찍기 거꾸로 왼쪽 정렬
for k in range(1,6).__reversed__() :
    for j in range (1,k+1) :
        print("*",end="")
    print()

# 거꾸로 왼쪽 정렬 다른 풀이
for k in range(1,6).__reversed__() :
    print("*"*k)

# 별찍기 거꾸로 오른쪽 정렬
for k in range(1,6):
    for j in range(1,6):
        if k<=j :
            print("*",end="")
        else:
            print(" ",end="")
    print()
# 거꾸로 오른쪽 정렬 다른 풀이
for k in range(1,6).__reversed__() :
    print(" "*(5-k)+"*"*k)

# 가운데 정렬
list = [4]
for k in range(1,5) :
    for j in range(1,8) :
            if list[0]<=j<=list[-1] :
                print("*",end="")
            else:
                print(" ",end="")
    list.append(list[-1]+1)
    list.append(list[0]-1)
    list.sort()
    print()

# 피라미드식 정렬 다른 풀이 :
for k in range(1,6) :
    print(" "*(5-k)+"*"*k+"*"*(k-1))