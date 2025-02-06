arr = ['L', 'E', 'B', 'R', 'O', 'S']


st = input()

# 배열에서 문자 위치 찾기
if st in arr:
    print(arr.index(st))  # 해당 문자의 인덱스 출력
else:
    print(None)  # 배열에 없으면 None 출력
    