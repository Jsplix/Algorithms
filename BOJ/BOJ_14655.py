import sys
input = sys.stdin.readline
# [BOJ] 14655 욱제는 도박쟁이야!! / 그리디
# 동전 뒤집기의 조건을 보면 결국 동전의 앞, 뒷면을 내 마음대로 할 수 있음. 결국 동전들의 절댓값에 2배를 해주면 됨.
n = int(input())
rounds= [list(map(abs, map(int, input().split()))) for _ in range(2)]
print(sum(rounds[0])*2)