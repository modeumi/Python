import random
#1 10kg 이상아면 수수료 10000원 , 10kg 미만이면 무료
weight = int(input("짐의 무게를 입력해주세요 (단위 Kg) : "))
if weight >= 10 :
    print('수수료는 10,000 원 입니다')
elif weight <10 :
    print("수수료는 없습니다.")

#2 10kg 이상 수수료 10 kg = 10000원 , 이후 10kg 마다 10000원 추가
weightst = input("짐의 무게를 입력해주세요 (단위 Kg) : ")
weight = int(weightst)
fir_weight = int(weightst[0])
if weight <10 :
    print("수수료는 없습니다")
elif weight>=10 :
    print("수수료는 {} 원 입니다".format(fir_weight*10000))

#3  1~10 의 난수 , 입력해서 맞으면 정답 크면 작은 숫자 입력 작으면 큰 숫자 입력  출력
random_num = random.randint(1,10)
while True :
    input_num = int(input("숫자를 입력하세요!"))
    if input_num == random_num :
        print("== 성공 ==")
        break
    elif input_num >10 or input_num<=0 :
        print("1~10사이의 숫자만 입력해줘여")
        print("-"*20)
        continue
    elif input_num > random_num :
        print("작은 숫자 입력해줘여")
        print("-"*20)
        continue
    elif input_num < random_num :
        print("큰숫자 입력 해줘여")
        print("-"*20)
        continue


#4 100 사이에서 3의 배수면서 2의 배수가 아닌 수의 합
number = total = 0
list = []
while number <= 100 :
    number += 1
    if number % 3 == 0 and number % 2 != 0 :
        total += number
        list.append(number)
print(total)
print(list)

#5 문자열 객체에서 단어추출 단어 갯수 출력
list = []
string = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
for i in string.split(sep=  "\n" ) :
    for j in i.split(sep=" ") :
        print(j)
        list.append(j)
print("단어의 갯수", len(list))

