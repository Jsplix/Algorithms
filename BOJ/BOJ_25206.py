import sys
input = sys.stdin.readline
# [BOJ] 25206 너의 평점은 / 수학, 구현, 문자열
score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
n = 20
sm, sub_score = 0, 0
for _ in range(20):
    subject, gpa, grade = input().split()
    if grade == 'P': n -= 1; continue
    sm += float(gpa)
    sub_score += (score[grade] * float(gpa))
print('%6f' % (sub_score/sm))