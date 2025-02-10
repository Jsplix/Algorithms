import sys
input = sys.stdin.readline
# 6378 디지털 루트 / 수학, 구현, 임의 정밀도, 큰 수 연산
while True:
    num = input().rstrip()
    
    if num == '0': break

    if len(num) == 1:
        print(num)
    else:
        answer = 0
        while len(num) != 1:
            temp = sum(list(map(int, num)))
            num = str(temp)
        print(num)