import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 1963 소수 경로 / 수학, 그래프 이론, 그래프 탐색, BFS, 정수론, 소수 판정, 에라토스테네스의 체 
def eratosthenes_sieve():
    prime_number = [1 for _ in range(10000)]
    prime_number[0] = prime_number[1] = 0

    for i in range(2, 101):
        if not prime_number[i]: continue
        for j in range(i * i, 10000, i):
            prime_number[j] = 0
    
    return prime_number

def bfs(s, l):
    queue = deque([[s, 0]])

    while queue:
        lst, cnt = queue.popleft()

        if lst == l:
            return cnt

        for i in range(4):
            for j in range(10):
                if lst[i] == j: continue
                num = int(''.join(map(str, lst[:i] + [j] + lst[i + 1:])))
                if p[num] and not visited[num] and num >= 1000: 
                    queue.append([list(map(int, str(num))), cnt + 1])
                    visited[num] = cnt + 1
    
    return "IMPOSSIBLE"
                

p = eratosthenes_sieve()
for _ in range(int(input())):
    a, b = map(int, input().split())
    mn, mx = min(a, b), max(a, b)
    visited = [0 for _ in range(10000)]
    visited[mn] = 1
    print(bfs(list(map(int, str(mn))), list(map(int, str(mx)))))
