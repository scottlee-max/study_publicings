# 문제 1 
변수 이름 
NameError가 발생하는 원인은 변수 이름의 오타 때문.

오류 찾기
변수를 선언하는 첫 줄의 frist를 first로 수정하면 문제가 해결.

first = 5

while   first> 0:
    print(f"while 값 : {first}")
    first = first - 1

# 문제 2 
들여쓰기(Indentation) 오류 찾고 수정
while 루프 본문의 들여쓰기가 일관되지 않기 때문.
while 루프 본문에 속하는 모든 문장(print와 first = first - 1)이 동일한 수준으로 들여쓰기 되어야 합니다.

first = 5

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1

# 문제 3 
논리적 오류(조건문) 찾기
if 조건식이 first == 3일 때 break가 실행되도록 요구했는데, 현재는 first < 3일 때 실행되도록 설정되어 있기 때문.
first가 5, 4일 때는 first < 3이 거짓이므로 계속 진행됩니다.

first가 3이 되면, first = first - 1에 의해 2가 됩니다.

다음 반복에서 first가 2일 때, first < 3 조건이 참이 되어 break가 실행됩니다.

요구사항은 first가 3일 때 루프를 종료하는 것이므로, 조건식을 수정.

first 변수의 값이 3과 같을 때(first == 3) break를 실행하도록 조건식을 수정.

first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first == 3:
        print("break 실행.")
        break
    first = first - 1