import sys
input = sys.stdin.readline
# [BOJ] 26535 Chicken Pen / 구현
n = int(input())
a = 1

while n > a**2:
    a += 1

answer = []
answer.append('x'*(a+2))
for i in range(a):
    answer.append('x' + '.' * a + 'x')
answer.append('x'*(a+2))

for r in answer:
    print(r)