import sys
input = sys.stdin.readline
# [BOJ] 25757 임스와 함께하는 미니게임 / 자료구조, 문자열, 해시
# Y - 윷놀이(2), F - 같은 그림 찾기(3), O - 원카드(4)
n, g = input().split()
players = [input().rstrip() for _ in range(int(n))]
players = list(set(players))
answer = 0
if g == 'Y':
    answer = len(players)
elif g == 'F':
    answer = len(players) // 2
elif g == 'O':
    answer = len(players) // 3
print(answer)