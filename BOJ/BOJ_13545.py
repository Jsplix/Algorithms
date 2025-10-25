import sys
import math
from collections import defaultdict, deque
# [BOJ] 13545 수열과 쿼리 0 / 누적 합, 오프라인 쿼리, 제곱근 분할법, mo's
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i, v in enumerate(arr, start=1):
    prefix[i] = prefix[i - 1] + v

q = int(input().strip())
queries = []
for idx in range(q):
    s, e = map(int, input().split())
    queries.append([s - 1, e, idx]) 

sz = int(math.sqrt(n))

cnt = [0] * (n + 1) 
bucket = [0] * (n // sz + 3)
pos = defaultdict(deque)
answers = [0] * q

def add(idx: int, direction: int) -> None:
    val = prefix[idx]
    dq = pos[val]
    if dq:
        length = dq[-1] - dq[0]
        cnt[length] -= 1
        bucket[length // sz] -= 1

    if direction == 0:
        dq.appendleft(idx)
    else:
        dq.append(idx)

    length = dq[-1] - dq[0]
    cnt[length] += 1
    bucket[length // sz] += 1

def remove(idx: int, direction: int) -> None:
    val = prefix[idx]
    dq = pos[val]

    length = dq[-1] - dq[0]
    cnt[length] -= 1
    bucket[length // sz] -= 1

    if direction == 0:
        dq.popleft()
    else:
        dq.pop()

    if dq:
        length = dq[-1] - dq[0]
        cnt[length] += 1
        bucket[length // sz] += 1

def current_answer() -> int:
    for bi in range(len(bucket) - 1, -1, -1):
        if bucket[bi] == 0:
            continue
        upper = min(n, (bi + 1) * sz - 1)
        lower = bi * sz
        for length in range(upper, lower - 1, -1):
            if cnt[length] > 0:
                return length
    return 0

queries.sort(key=lambda item: (item[0] // sz, item[1] // sz))

cur_l, cur_r, idx = queries[0]
for pos_idx in range(cur_l, cur_r + 1):
    add(pos_idx, 1)
answers[idx] = current_answer()

for l, r, idx in queries[1:]:
    while cur_l > l:
        cur_l -= 1
        add(cur_l, 0)
    while cur_r < r:
        cur_r += 1
        add(cur_r, 1)
    while cur_l < l:
        remove(cur_l, 0)
        cur_l += 1
    while cur_r > r:
        remove(cur_r, 1)
        cur_r -= 1
    answers[idx] = current_answer()

print("\n".join(map(str, answers)))