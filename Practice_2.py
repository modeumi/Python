#연습문제
# 1번
su = 5
dan = 800
# su, dan id 확인
print("su의 id값 : " + str(id(su)))
print("dan의 id값 : " + str(id(dan)))
# 금액 계산
print("거래 금액 : " +str(su*dan))

#2번
x = int(input("X의 값을 입력하시오"))
y =  2.5*(x**2)+3.3*x+6
print("2차 방정식 결과 = ", y)

#3번
pat = int(input("지방의 그램을 입력하세요 : "))
car = int(input("탄수화물의 그램을 입력하세요 : "))
pro = int(input("단백질의 그램을 입력하세요 : "))
total = format(pat*9 + pro*4 + car*4, "3,d")
print(f"총 칼로리량 : {total} cal")

#4번
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
abbr = word1[0]+word2[0]+word3[0]
print("첫번째 단어 : ",word1 )
print("두번째 단어 : ",word2 )
print("세번째 단어 : ",word3 )
print("=" *30)
print(f"약자 : {abbr}")

# 5번
# Korea, Baseball , Orag, Victory 를 변수에 입력받고
#Love를 출력

fir_word = "Korea"
sec_word = "Baseball"
thr_word = "Orag"
for_word = "Victory"

print(sec_word[-1].upper() + thr_word[0].lower()+for_word[0].lower()+fir_word
      [-2])
# 다른풀이
abbr2 = sec_word[-1] + thr_word[0]+for_word[0]+fir_word[-2]
# capitalize 앞글자만 대문자 나머지는 소문자로
print(abbr2.capitalize())

# 6번
# Be Korea.org 출력
fir_word = "Korea"
sec_word = "Baseball"
thr_word = "Orag"
for_word = "Victory"

abbr3 = sec_word[0:5:3] +" "+fir_word.lower() +"." +thr_word[0:2].lower()+thr_word[-1]
# abbr3 = sec_word[0:5:3] ,fir_word.lower() +"." +thr_word[0:2].lower()+thr_word[-1]
# 위처럼 공백 대신에 , 를 찍으면 공백이 자동적으로 생성된다.
print(abbr3)