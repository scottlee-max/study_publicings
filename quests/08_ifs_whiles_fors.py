✅ 문제 1 — return 누락 오류
아래 함수는 섭씨 변환 후 값을 반환해야 한다.
 현재 코드에서 발생하는 오류를 찾고 수정하시오.

주어진 함수 to_celsius(temp)는 결과 값을 반환하는 return 문이 누락.
celsius 변수에 계산된 값을 반환하도록 return 문을 추가.

def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    retune celsius
result = to_celsius(77)
print(result)




✅ 문제 2 — 매개변수 이름 오류
아래 프로그램은 실행 시 오류가 발생한다.
 오류 위치를 찾고 올바르게 수정하시오.

convert 내부에서 매개변수 이름이 잘못 사용.

def convert(temp):
    return (temp - 3) * 5 / 9   

print(convert(95))


✅ 문제 3 — 함수 호출 인자 오류
아래 코드는 함수 호출이 잘못되어 있다.
 오류를 설명하고 고치시오.

def to_celsius(temp):
    return (temp - 32) * 5 / 9

value = to_celsius(77)
print(value)


✅ 문제 4 — 타입 오류(TypeError)
아래 코드는 문자열을 함수에 전달하여 오류가 발생한다.
 이 오류가 왜 발생하는지 설명하고 해결하시오.

def to_celsius(temp):
    return (temp - 3) * 5 / 9

print(to_celsius(77)) 또는
print(to_celsius(int("77")))



✅ 문제 5 — 반복 구조 + 함수 사용 오류
아래 코드는 여러 값을 함수로 변환하려 하지만 오류가 발생한다.
 오류 원인을 찾고 고치시오.
def to_celsius(temp):
    return (temp - 3) * 5 / 9

temps = [77, 95, 50]
results = []

for t in temps:
    result = to_celsius(t)
    print(results)