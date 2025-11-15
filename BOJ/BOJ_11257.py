import sys
input = sys.stdin.readline
# [BOJ] 11257 IT Passport Examination / 수학, 구현, 사칙연산
for _ in range(int(input())):
    std, *scores = map(int, input().split())

    sm = sum(scores)
    cline = [35 * 0.3, 25 * 0.3, 40 * 0.3]

    if sm >= 55 and scores[0] >= cline[0] and scores[1] >= cline[1] and scores[2] >= cline[2]:
        print(std, sm, "PASS")
    else:
        print(std, sm, "FAIL")