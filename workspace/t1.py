from collections import deque
import sys
input = sys.stdin.readline

# [BOJ] 1005 ACM Craft / 위상 정렬, 그래프 이론, DP

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))

    inDegree = [0 for _ in range(n+1)] # 진입 차수에 대한 정보 저장
    graph = [[] for _ in range(n+1)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y) # 그래프 형성
        inDegree[y] += 1 # 진입 차수 증가
    
    target = int(input())
    
    queue = deque([])
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if inDegree[i] == 0: # 진입 차수가 0인 노드를 찾아 큐에 저장
            queue.append(i)
            dp[i] = d[i-1] # dp를 활용해 거리 저장

    path = []
    while queue:
        v = queue.popleft()
        path.append(v)
        for i in graph[v]:
            inDegree[i] -= 1 # 큐에서 노드를 뺐으므로, 해당 노드의 진출과 이어진 노드는 진입 차수를 1씩 감소시켜줌
            dp[i] = max(d[i-1]+dp[v], dp[i]) # 최댓값을 선택하도록 함.
            # 최댓값을 선택하는 이유 - 입력 예제를 보면 2의 건설 시간은 1초이지만, 4를 건설하기 위해선 2, 3 모두 건설되어야 하기 때문에
            # 가장 오래걸리는(최댓값) 시간을 선택해줘야 함.
            if inDegree[i] == 0: # 다시 진출 차수가 0인 노드는 큐에 넣음
                queue.append(i)

    print(dp[target]) 