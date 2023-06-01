from builtins import print

a = 10
b = 20
c = a+b
print(c)
# 30 이라는 값 출력

# if 조건문
a = 1
if a in [1,2,3,4]:
    print("good")

# 문장형
d = "python"
# d만 입력시 'python'
d
# print 와 사용시 python
print(d)

#if문
a = 10
if a >1:
    print("a는 1보다 큼")

# 반복문 while
i = 0
while i<3:
    i=i+1
    print(i)
# 출력 결과는 1,2,3

#함수
def add(a,b):
    return a+b
add(4,7)
# 결과는 11 def가 함수의 예약문

# if와 함수 대입
def test (a,b):
    if a>3 :
        i =0
        while i<a:
            i=i+1
            return print("작다%d" %(b-a))
    else:
        i =0
        while i < a:
            i=i+1
            return print("크다%d" %(b-a) )
    # 숫자와 문장을 같이 쓰고싶으면 문자열 안에 %d를 넣고 밖에 %값을 해주고
    # 문자를 넣고싶다면 %s 를 사용한다
test(2,5)

#문자열
a = "modeumi"
b = ' modeumjeon'
print(a+b)
# 문자열끼리의 합은 문자 그대로를 나열한 값, 고로 'modeumi modeumjeon'이 출력
print(a*2)
# 문자열의 곱은 같은 문자열이 두번 나열되는 값, 고로 'modeumimodeumi'로 출력

# 문자열 연산
a = "안녕하세요. python 공부 중 입니다."
b = "오늘은 1일차 입니다."
print("-"*20)
print(a+b)
print("-"*20)

a = "modeumi"
print(a[2])
print(a[0:2])
print(a[:3])
print(a[3:])
print(a[2:5])
# 0= m / 1= o / 2 = d / 3 = e  를 의미
# 혹은 -1 = i / -2 = m / -3 = u /-4 = e 을 의미

print(a[0:3])
#- > "mod"
print(a[0:4])
#-> "mode"

a = "Pithon"
print(a[0] + 'y' + a[2:])


# 마지막 인덱스는 생략한다  a:b 면 a이상 b미만 같은 의미 

#a [start;end:step] 
#step = 간격  / default 값은 1 

#응용 - 
#a[1:3] / a[2:]  / a[:3]

print("%10s" % "hi")
print("%-10s" % "by")
# '          hi'
# %10s 는 앞에 10칸을 띄우라는것

print("i'm a %s" %"modeumi") # 문자는 포맷팅 할 곳에 %s를 한뒤 %""로 넣어준다
print("i'm a {0}".format("modeumi")) #.format ("")도 가능

print("i'm a %d old" %29) # 정수는 %d를 한뒤 $ 로 넣어준다
print("i'm a {0} old".format(29))  #.format()도 가능

name = "모듬전"
age = 29
print(f'{name}의 나이는 내년에 {age+1}입니다')
# f를 앞에 붙임으로서 문자열 포맷팅이 가능
d = {'name' :'모듬전' ,'age': '29'}
print(f'{d["name"]}의 나이는 {d["age"]}입니다')
# 위와같이 딕셔녀리는 key:value 같은 느낌으로도 사용 가능.

#정렬
print(f'{"hi": <10}')
# 왼쪽 정렬 'hi          '
print(f'{"hi": >10}')
# 오른쪽 정렬 '          hi'
print(f'{"hi": ^10}')
# 중앙 정렬 '     hi     '
print(f'{"hi":=^10}')
# 왼쪽 정렬 후에 공백을 =로 대체
a = 3.1415928283
print (f'{a:10.4f}')
# 10칸을 출력 하는데 a의 값을 소수점 4자리까지 출력함
# 고로 10칸중 4칸은 공백 6칸은 값 '    3.1415'
print (f'{{center}}')
# 출력값에 {}를 넣고싶다면 {{}}를 사용
# 출력값은 {center}

a = "i'm a boy, i will be man"
print(a.split())
#["i'm", 'a', 'boy,', 'i', 'will', 'be', 'man'] 으로 출력될것
#split 으로 default기준인 공백을 기준으로 문장을 자른다
print(a.upper())
#'I'M A BOY, I WILL BE MAN'
#upper은 모든 글자를 대문자로 바꾸는것것

# ----------------------------------------
#list 자료
a = [1,2,3,4,5]
print(a[4])
print(a[-1])
print(a[0]+a[3])
# 세개다 모두 같은값을 출력할것
b = [1,2,3,['a','b','c']]
print(b[3])
print(b[3][2])
print(b[3][-1])
# 각 [a,b,c]  / 'c' / 'c' 를 출력할것
#배열안에 배열안에 배열안에 배열안에... 가능 b[][][][][][]같은식으로 호출
a = [1,2,3]
print(a*2)
print(a+a)
#둘다  [1,2,3,1,2,3]의 값을 출력
print(len(a))

a = "buer"
b = [1,2,3]
# a+b[2] 하면 error
print(str(b[2]) + a)
# b를 string으로 변경해줘야 에러없이 출력가능

a = [1,2,3,4]
a[2] = 5
print(a)
# a = [1,2,5,4] 가 됨
del(a[2])
print(a)
# a = [1,2,4] 가 됨
a.append(5)
print(a)
#a =[1,2,4,5] 가 됨 [1,2] 처럼 배열도 추가가능
a.reverse()
print(a)
# a = [5,4,2,1] 처럼 역순으로 정렬
a.sort()
print(a)
# a = [1,2,4,5] 처럼 순서정렬
print(a.index(5))
# 3 을 출력  // 5라는 값을 가진 인덱스번호를 출력
a.insert(0,4)
print(a)
# a의 0번째 인덱스에 4를 추가 a = [4,1,2,4,5]
a.remove(4)
print(a)
# a의 배열에서 가장 첫 4를 제거 a = [1,2,4,5]
print(a.pop(2))
print(a)
# a의 배열에서 2번째 인덱스 값을 추출후 삭제
# 값은 4/ [1,2,5] 로 출력
print(a.count(2))
# a의 배열 안에서 2라는 숫자의 갯수를 출력 값은 1
a.extend([6,7])
print(a)
#extend()에는 배열만 가능하며 배열+배열과 같은값을 출력
# 값은 [1,2,5,6,7]
