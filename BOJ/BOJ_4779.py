import sys
input = sys.stdin.readline
# [BOJ] 4779 칸토어 집합 / 분할 정복, 재귀
# 2447 별 찍기 10과 거의 동일한 문제
def solve(n):
    if n == 1:
        return '-'

    Cantor = solve(n // 3)
    s = []

    for c in Cantor:
        s.append(c)
    for c in Cantor:
        s.append(' ')
    for c in Cantor:
        s.append(c)
    
    return s

while True:
    try:
        n = int(input())
        print(''.join(solve(3**n)))
    except:
        break
