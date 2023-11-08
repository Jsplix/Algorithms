import sys
input = sys.stdin.readline
# [BOJ] 7785 회사에 있는 사람 / 자료 구조, 해시를 사용한 집합과 맵
now = set()
for _ in range(int(input())):
    name, state = input().split()
    if state == 'enter':
        now |= set([name])
    else:
        now -= set([name])
now = sorted(list(now), reverse=True)
print(*now, sep='\n')