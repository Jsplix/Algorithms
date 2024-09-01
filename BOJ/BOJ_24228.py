import sys
input = sys.stdin.readline
# [BOJ] 24228 젓가락 / 구현, 비둘기집 원리
n, r = map(int, input().split())
print(n+(2*r)-1)