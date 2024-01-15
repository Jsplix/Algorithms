import sys
input = sys.stdin.readline
# [BOJ] 1351 무한 수열 / DP, 자료 구조, 해시를 사용한 집합과 맵
def recursive(n):
    global answer, p, q
    if not n in answer: answer[n] = recursive(n//p) + recursive(n//q)

    return answer[n]

n, p, q = map(int, input().split())
answer = {} ; answer[0] = 1
print(recursive(n))