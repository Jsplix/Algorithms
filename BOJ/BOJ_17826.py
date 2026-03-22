import sys
input = sys.stdin.readline
# [BOJ] 17826 나의 학점은? / 구현
scores = list(map(int, input().split()))
hong = int(input())

rank = scores.index(hong)
if 0 <= rank <= 4: print("A+")
elif 5 <= rank <= 14: print("A0")
elif 15 <= rank <= 29: print("B+")
elif 30 <= rank <= 34: print("B0")
elif 35 <= rank <= 44: print("C+")
elif 45 <= rank <= 47: print("C0")
else: print("F")