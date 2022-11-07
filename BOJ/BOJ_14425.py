# BOJ_14425 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
init_dict = {}
for _ in range(n):
    d = input().rstrip()
    init_dict[d] = 0
for _ in range(m):
    s = input().rstrip()
    if s in init_dict: # 딕셔너리에서의 in은 시간복잡도가 O(1)
        init_dict[d] += 1 # 딕셔너리에 있는 경우 해당 key 값의 value를 +1 증가시켜줌

print(sum(init_dict.values()))