import sys
input = sys.stdin.readline
# [BOJ] 12018 Yonsei TOTO / 그리디, 구현
n, m = map(int, input().split())
check = []
for _ in range(n):
    p, l = map(int, input().split())
    mileages = sorted(map(int, input().split()), reverse=True)

    if p > l: # 신청한 사람 수 > 수강 인원
        # 투자 순위가 (수강 인원 - 1)번째인 사람의 마일리지와 동일하게 투자 (마일리지 동일하면 우선순위로 인해 수강함)
        check.append(mileages[l-1])
    elif p == l: # 신청한 사람 수 = 수강 인원
        # 최소 마일리지 투자한 사람의 마일리지와 동일하게 투자 (마일리지 동일하면 우선순위로 인해 수강함)
        check.append(mileages[-1])
    else: # 신청한 사람 수 < 수강 인원
        check.append(1)

if sum(check) <= m: # 수강신청에 필요한 최소 마일리지가 주어진 마일리지보다 작거나 같다면
    # 모든 과목 수강 가능
    print(n) 
else:
    check.sort()
    idx = n-1
    now = n # 현재 수강 가능한 과목 수
    cnt = 0 # 포기하는 과목 수
    while idx >= 0:
        check.pop() # 마일리지가 가장 많이 드는 과목 포기
        cnt += 1 # 과목 포기
        if sum(check) <= m: # 수강 신청에 필요한 마일리지 합계를 다시 주어진 마일리지와 비교 
            print(n-cnt)
            exit(0)
    print(n-cnt) # 모든 경우를 벗어난다면 0