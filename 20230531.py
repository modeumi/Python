#대입 연산자

print ( "출력1,")
print ("출럭2,")
print("출력3")
# -> 출력1,
# 출력2,
# 출력3

print ( "출력1" ,end =" ,")
print ("출럭2",end = ".")
print("출력3")
# - > 출력1,출력2,출력3

a = b = c = 100
# a= 100/ b= 100 / c=100
d,e,f = 100,200,300
print(a,b,c,d,e,f)
v1, v2 = 100, 200
print (v1,v2)
# v1 = 100, v2 = 200
v1, v2 = v2, v1
print (v1,v2)
# v1 = 200, v2 = 100

list = [1,2,3,4,5]
var1, *var2 = list
# *는 패킹의 역할 var
# list의 값은 5개인데 받는게 2개뿐 var2에 * (패킹)을 적용하면
# var1 = 1 , var2 = [2,3,4,5]
print(var1,var2)

*var1, var2 = list
# 반대로 var1에 [1,2,3,4] var2에 5가 할당됨.
print(var1,var2)

#응용
var1,var2,*var3 = list
print(var1,var2,var3)
#1 2 [3,4,5]
print("-" *20)
var1,*var2,var3 = list
print(var1,var2,var3)
#1 [2,3,4] 5
print("-" *20)
*var1,var2,var3 = list
print(var1,var2,var3)
#[1,2,3]4 5
*var1,var2,var3 =list
print(var1,var2,var3)
# 3개의 값에 대입, 한개의 값만 패킹 이므로 두개는 정수값, 한개는 배열값이 나온다.

#표준 입출력 장치
# 자바의 scanner 같은 기능
a = input("숫자를 입력하세요 str") # 입력값은 str의 형태를 띔
print(type(a))
b = int(input("숫자를 입력하세여 int")) # 입력값을 int 로 변경
print(type(b))

#포맷
print('v1 값은' , v1)
# 위도 간단한 포맷

# format( 값 , 값을 표현할 포맷)
print("원주율 = " ,format(3.141592 , "*>8.3f"))
# 3,141592 를 8자리 안에 넣는데 소수점은 3자리만 표현하며 공백은 *을 넣겠다 .
# f 는 float
print("금액 = ", format(1000, "*^10d"))
#1000 이라는 값을 10칸안에 넣겠다. 보기 편하게 가운데 정렬 + 공백 *표시함.
print("금액 = ", format(1250000,"3,d"))
# 1250000 이라는 값을 3자리마다 ,을 찍겠다.

#양식 문자 인수
name = "모듬전"
age = 29
price = 1234.5678
print("name : %s, age : %f , price : %.2f" %(name,age,price))
print("name : %s, age : %d , price : %.3f" %(name,age,price))

# 외부 상수 출력
print("이름 :{}, 나이 : {} . 금액 : {}".format(name,age,price))
print("이름 :{2}, 나이 : {1} . 금액 : {0}".format(price,age,name))

#format 축약형
age = input( "나이 입력 : ")
question = f"당신의 나이는 몇살 ? {age}"
print(question)

# 문자열 자료형
#Q. oneline 에서 one만 추출하기
one = "oneline"
print(one[:3])
print(one[:1]+one[5:])
print(one[0] + "n" + one[-1])

s = "English Words"
print(s.upper()) # 대문자로 문자 변경
print(s.lower()) # 소문자로 문자 변경
print(s.swapcase()) #대문자를 소문자로 소문자를 대문자로 변경
print(s.replace("Word","spell")) #word를 spell로 변경
print(s.find('s')) # 첫 s를 찾기 없다면 -1
print(s.index('s')) # 첫 s를 찾기 없다면 error
print(s.split(" ")) #" "(공백) 을 기준으로 문자열을 자른다.
print(s.count('s')) # s라는 글자의 수를 출력
print(','.join(s))
# join - s의 string 의 글자마자 ,를 추가해준다.
str_list = ['apple', 'tomato' , 'banana', 'grape']
print('과일 들 :' + ','.join(str_list))
# list 형태를 ,를 추가하여 문장으로 만들때도 사용

# 3장
# if 문
#if :   -> if 후 : 필수 + 다음 줄부터 if 끝날때까지 들어쓰기
var = 4
print("if문 시작\n"+"="*20)
if var >=5 :
    print("if로 진입")
elif 5>var >=3:
    print("elif로 진입")
else :
    print("elif도 if도 아닐때")
print("="*20 , "\nif문 종료  ")

# 응용
korea = int(input("국어 점수를 입력하세요 : "))
if korea >= 90 :
    print(f"점수는 {korea}입니다. 등급은 A 입니다.")
elif 70 <= korea < 90 :
    print(f"점수는 {korea}입니다. 등급은 B입니다.")
elif 40 <= korea <70 :
    print(f"점수는 {korea}입니다. 등급은 C 입니다.")
else :
    print(f"점수는 {korea}입니다. 등급은 D 입니다.")


var  = 4
print(var, " if문 진입 전 ")
var = var+1 if var > 3 else var -2
print(var, " if문 진입 후 ")

#반복문
var = 5
while var <10 :
    print(f"var의 값이 9가 될때까지 \n 현재 var 값은 : {var} ")
    var += 1

# 반복문 + 조건문
var = total = 0
list = []
while var < 100 :
    var += 1
    if var % 3 == 0 :
        total += var
        list.append(var)
print(total)
print(list)
print(len(list))

# 문제1
# 100 이하 숫자 중 5의 배수이면서 3의 배수가 아닌 값 합 계산
var = total = 0
list = []
while var <= 100 :
    var+=1
    if var % 5 == 0 and var % 3 != 0 :
        total += var
        list.append(var)
print(total)
print(list)
# 문제 2
# -1, 3,-5,7,-9~99까지의 합을 구하시오.
var = total = 0
list = []
while var < 100 :
    var += 1
    if var %2 != 0 :
        if total >= 0 :
            total -= var
            list.append(-var)
        elif total<0 :
            total += var
            list.append(var)
print(total)
print(list[:25])
print(list[25:50])