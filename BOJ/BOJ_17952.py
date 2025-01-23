import sys
input = sys.stdin.readline
# [BOJ] 17952 과제는 끝나지 않아! / 구현, 자료 구조, 시뮬레이션, 스택
n = int(input())
prev = []

flag = False
working = []

scores = 0
for _ in range(n):
    chk, *at = map(int, input().split())

    if chk == 1 and not flag: # 최초의 과제 or 진행중이던 과제가 없고 과제를 받음음
        working.append(at)
        working[-1][1] -= 1
        if not working[-1][1]: scores += working[-1][0] ; working.pop()
        flag = True
    elif chk == 1 and flag: # 과제 진행하던 중 새로운 과제를 받음
        working.append(at)
        working[-1][1] -= 1
        if not working[-1][1]: scores += working[-1][0] ; working.pop()
    elif not chk: # 과제를 받지 않음
        if flag: # 과제는 시작함
            if not working: flag = False; continue # 진행중인 과제가 없는 경우 넘어감감
            working[-1][1] -= 1 # 진행하던 과제 계속 진행행
            if not working[-1][1]: scores += working[-1][0] ; working.pop()
        else: # 받은 과제도 없고, 이전에 진행하던 과제도 없음.
            continue

print(scores)