import sys
input = sys.stdin.readline
# [BOJ] 11943 파일 옮기기 / 수학, 구현
a, b = map(int, input().split())
c, d = map(int, input().split())

c1 = b + c
c2 = a + d
answer = c1 if c1 < c2 else c2
print(answer)