import sys
input = sys.stdin.readline
# [BOJ] 2783 삼각 김밥 / 수학, 구현, 사칙연산
x, y = map(int, input().split())
gimbap = []
for _ in range(int(input())):
    gimbap.append(tuple(map(int, input().split())))

gimbap.sort(key=lambda x:(float(x[0])/float(x[1]))) # 1g당 가격으로 정렬
print("%.2f" % min(((float(gimbap[0][0])/float(gimbap[0][1]))*1000), ((float(x)/float(y))*1000)))