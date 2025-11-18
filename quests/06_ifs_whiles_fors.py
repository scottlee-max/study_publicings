

✅ 문제 1 — 문자열 포맷 오류 수정하기
아래 코드는 문자열을 합치는 과정에서 오류가 발생.
 오류를 찾아서 올바른 코드로 수정하시오.

문자열과 변수를 합치려는 과정에서 + 연산자와 중괄호 { }를 잘못 사용

second = "Programming"
# f-string을 사용하여 문자열 내부에 변수 값을 삽입
first = f"Welcome to Python Strings {second}" 
print(first)

Welcome to Python Strings Programming

✅ 문제 2 — while 조건 오류 찾기
아래 코드는 first가 문자열인데, while 조건에서 비교 연산을 수행하려고 한다.
 발생하는 오류를 설명하고, 정상 작동하도록 수정하시오.

문자열은 크기 비교의 대상이 아니며, while 루프는 반복 횟수를 결정할 수 있는 숫자형이나 리스트와 같은 반복 가능한 객체를 기반으로 조건을 설정해야 함.

first = "Hello Python"
# 정수형 변수를 조건으로 사용
first = 5
while first > 0:
   # 루프를 멈추기 위해 변수 값을 감소
     print(first)
     first = first - 1



✅ 문제 3 — 리스트 누적 합 오류 찾기
아래 코드의 오류를 찾고 올바르게 수정하시오.
sum_all = sum_all + kor + eng 부분에서 오류가 발생.
kor의 합계만 구하는 것이 아니라면, 두 리스트의 모든 요소를 누적 합산하도록 코드를 수정.

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0
# kor 리스트의 모든 요소를 sum_all에 누적
for k in kor:
    sum_all = sum_all + k
# eng 리스트의 모든 요소를 sum_all에 추가로 누적
for e in eng:
    sum_all = sum_all + e
print(f"총 누적 합계: {sum_all}")


✅ 문제 4 — for-range 인덱스 문제 해결
아래 코드에서 IndexError가 발생한다.
 오류 원인을 설명하고 올바른 코드를 작성하시오.

kor과 eng 리스트의 길이는 각각 5.
리스트의 유효한 인덱스는 $\mathbf{0}$부터 $\mathbf{4}$까지 
(길이 $-1$).

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_total = 0
# 리스트의 길이(5)만큼만 반복하도록 range의 상한을 len(kor)로 설정
list_length = len(kor) 
for i in range(list_length):  # range(5)는 0, 1, 2, 3, 4를 생성
    # kor[i]와 eng[i]를 동시에 더해 누적
    sum_total = sum_total + kor[i] + eng[i]
print(f"총 합산 결과: {sum_total}")