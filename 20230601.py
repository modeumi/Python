import numpy
# numpy.arange( )
import random
random.randint(1,3) # 1이상 3이하의 랜덤수 1,2,3 / [1,3] 으로 적용됨
random.random() # 0부터 1까지의 난수가 나오게 설정됨 / 사이값 입력불가
random.uniform(1,100) # 1~100까지의 난수가 나오게 설정  / 입력한 값만큼 그 사이 값 출력 가능
# 참고
# (a,b) a 초과 b 미만
# [a,b] a 이상 b 이하
# [a,b) a 이상 b 미만
# (a,b} a 초과 b 이하

lists = [ 'barbatos', 'moracs' , 'buer','baal']
#1 choice
print(random.choice(lists))

#2 choices [리스트이름 ,확률 (생략가능),꺼낼 갯수)
print(random.choices(lists,weights=[50,20,20,10],k=3))

#3 randint
integer = 0
while integer < 5:
    print(random.randint(1,4))
    integer +=1

#4 ramdum // 0부터 1까지의 난수가 나오게 설정됨 / 사이값 입력불가
integer = 0
while integer <5 :
    print(random.random())
    integer += 1

#5 uniform //  # a~b까지의 난수가 나오게 설정
integer = 0
while integer <5 :
    print(random.uniform(1,10))
    integer += 1

#6 sample  // 리스트로부터 x개를 임의로 추출
print(random.sample(lists,2))

#7 seed
# print(random.seed(lists))

# 연습
ranlist = []
while True :
    rannum = random.randint(1,100)
    if rannum <=10 :
        print('{} 번째에서 10 이하가 나옴. 나온 숫자는 {} 임'.format(len(ranlist),rannum))
        break
    else:
        ranlist.append(rannum)
print(ranlist)
print(len(ranlist))

# for --  // for 변수 in 열거형객체 :

# 객체가 i에 대입되고 그 i를 실행
for i in lists :
    print("신명 : ", i , '/ 글자수 :' , len(i))
print("="*20 ,"반복문 종료")
# for 안에 string을 넣는다면 string의 lenght 만큼 진행

#rnage --
# range(10) : 0~9까지 정수
# range(start,stop,step) : start 부터 stop의 전까지 / step의 간격으로

#중첩 반복문 for : for : for:
for i in range(4) :
    for j in lists[i] :
        print("스페링 대문자로 " , j.upper())
    print("여기까지 {}의 스펠링 끝".format(lists[i]))

senst = []
words = []
info = """나히다는 풀의 신
나이는 약 500살
신명은 buer"""
for i in info.split(sep= "\n") :
    senst.append(i)
    print("문장 저장 완료 : {}".format(i))
    for j in i.split(sep=" ") :
        words.append(j)
        print('딘어 저장 완료 : {}'.format(j))
    print()
print('총 문장수 : ', len(senst))
print('총 단어수 : ', len(words))

# 자료구조
# 순서형 - 인덱스 슬라이싱 사용가능
# str - ' ' , " " , """ """
string = str(object='Stringtype')
print(string)
print(string[0])
print(string[-1])

# list - [1,2,"3",[a,b] ]
list = list(range(1,6))
print(list)
for i in list :
    print(list[:i])

#리스트 결합 (추가)
fir_list = [1,2,3,4,5]
sec_list = [6,7,8,9,10]
total_list = fir_list+sec_list
print(total_list)
#리스트 확장 /결과는 결합과 같다
fir_list.extend(sec_list)
print(fir_list)
# 리스트 추가
fir_list = [1,2,3,4,5]
fir_list.append(sec_list)
print(fir_list)
#리스트 두배로 확장 / str *2와 같은 방식
fir_list = [1,2,3,4,5]
total_list = fir_list*2
print(total_list)
# tuple - (1,2,3)
# 비순서형 - 인덱스 슬라이싱 사용불가
# set {1,2,3}
# dict {1:3,"한개":10} // map 구조 처럼 key : value  형태
