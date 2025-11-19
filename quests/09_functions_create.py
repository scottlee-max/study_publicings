공통 사항 : 제출 문제마다 function 실행은 최소 3회 호출

🔹 문제 1
섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

def avg_celsius(t1, t2, t3):
    average = (t1, t2, t3) / 3
    return = average
print(f"평균 온도 1: {avg_celsius(10, 20, 30) }도")
print(f"평균 온도 2: {avg_celsius(25.5, 30.1, 28.4) }도")
print(f"평균 온도 3: {avg_celsius(-5, 0, 5) }도")

🔹 문제 2
이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
홍길동님의 선호 언어는 Python, Java입니다.

def favorite_languages(name, lang1, lang2):

print_favorite_languages("오상훈", "Python", "Java")
print_favorite_languages("이상로", "C++", "JavaScript")
print_favorite_languages("이용기", “ Ruby", "C#")

🔹 문제 3
점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.

def sum_pass_scores(scores):
    total = 0
    for score in scores:
        if score>=60:
          total += score

    return total
scores1 = [100, 95, 90, 55]
scores2 = [80, 55, 40, 65]
scores3 = [55, 60, 45,30]

print(f“60점 이상 합계 1: {sum_pass_(scores1)}”)
print(f“60점 이상 합계 2: {sum_pass_(scores2)}”)
print(f“60점 이상 합계 3: {sum_pass_(scores3)}”)

🔹 문제 4
문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

def combine(str1, str2):
    return str1 + str2

print(combine(“Welcome”, “to seoul”))
print(combine(“Good”, “Nightl”))
print(combine(“Have a”, “Nice day”))

🔹 문제 5
온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.

def to_celsius(temp_list):
    celsius_list = [  ]
    for temp in temp_list:
        celsius = (f - 32) * 5 / 9
        celsius_list = celsius_list + [celsius] 
    return celsius_list

temps_f1 = [32, 212, 100] 
temps_f2 = [50, 60, 70, 80]
temps_f3 = [0, -40, 98.6]

print(to_celsius([32, 212, 100]))
print(to_celsius([50, 60, 70, 80]))
print(to_celsius([0, -40, 98.6]))