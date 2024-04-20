import sys
input = sys.stdin.readline
# [BOJ] 13325 이진 트리 / DP, 트리, 트리에서의 DP
k = int(input())
edge_weight = [0] + list(map(int, input().split()))

start = 2**k - 1
end = 2**(k+1) - 1

total = sum(edge_weight)
while end: # 자식 노드부터 루트 노드까지 위로 올라가면서 구함. (bottom-up)
    for i in range((end - start) // 2):
        c_edge = start + (2 * i)
        next = c_edge // 2

        # 입력받은 가중치(edge_weight)에 자식 노드(왼, 오)에서 부모 노드까지의 가중치 중 큰 것을 기존 부모 노드의 가중치에 더함
        edge_weight[next] += max(edge_weight[c_edge], edge_weight[c_edge + 1])
        # left, right child 노드의 차이를 더해줌
        total += abs(edge_weight[c_edge] - edge_weight[c_edge + 1])
    
    end = start
    start = start // 2

print(total)