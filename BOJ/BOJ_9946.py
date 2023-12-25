import sys
input = sys.stdin.readline
# [BOJ] 9946 단어 퍼즐 / 문자열, 정렬
id = 1
while True:
    a = list(input().rstrip())
    b = list(input().rstrip())

    if ''.join(a) == 'END' and ''.join(b) == 'END': break
    a.sort()
    b.sort()

    if a == b:
        print(f"Case {id}: same")
    else:
        print(f"Case {id}: different")
    id += 1