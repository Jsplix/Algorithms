import sys
input = sys.stdin.readline
# [BOJ] 13547 수열과 쿼리 5 / 오프라인 쿼리, mo's
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
queries = [[i] + list(map(int, input().split())) for i in range(M)]

size = int(N ** 0.5)
queries.sort(key=lambda x:(x[1] // size, x[2]))

def find(left, right, prev: tuple):
    if prev:
        p_left, p_right, p_set = prev

        while p_right < right:
            p_right += 1
            if arr[p_right] in p_set.keys():
                p_set[arr[p_right]] += 1
            else:
                p_set[arr[p_right]] = 1
        
        while p_right > right:
            p_set[arr[p_right]] -= 1
            if p_set[arr[p_right]] == 0:
                del p_set[arr[p_right]]
            p_right -= 1

        while p_left < left:
            p_set[arr[p_left]] -= 1
            if p_set[arr[p_left]] == 0:
                del p_set[arr[p_left]]
            p_left += 1
        
        while p_left > left:
            p_left -= 1
            if arr[p_left] in p_set.keys():
                p_set[arr[p_left]] += 1
            else:
                p_set[arr[p_left]] = 1
        
        prev = (p_left, p_right, p_set)
    
    else:
        p_set = {}
        for i in range(left, right + 1):
            if arr[i] in p_set.keys():
                p_set[arr[i]] += 1
            else:
                p_set[arr[i]] = 1
        
        prev = (left, right, p_set)

    return len(p_set), prev

prev = 0
answer = [0 for _ in range(M)]
for idx, l, r in queries:
    size, prev = find(l - 1, r - 1, prev)
    answer[idx] = size

for ans in answer:
    print(ans)