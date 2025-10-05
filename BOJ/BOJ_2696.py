import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M = int(input())
    A = []

    if M % 10 == 0:
        for __ in range(M // 10):
            A += list(map(int, input().split()))
    else:
        for __ in range(M // 10 + 1):
            A += list(map(int, input().split()))

    result = [A[0]]
    mid = A[0]
    mn, mx = [], []

    for i in range(1, M):
        if A[i] > mid:
            heapq.heappush(mx, A[i])
        else:
            heapq.heappush(mn, -A[i])

        if i % 2 == 0:
            if len(mn) < len(mx):
                heapq.heappush(mn, -mid)
                mid = heapq.heappop(mx)
            elif len(mn) > len(mx):
                heapq.heappush(mx, mid)
                mid = -heapq.heappop(mn)
            result.append(mid)

    print(len(result))
    for i in range(len(result)):
        if i > 0 and i % 10 == 0: print()
        print(result[i], end=' ')
    print("")
