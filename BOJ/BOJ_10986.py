import sys
input = sys.stdin.readline

# [BOJ] 10986 나머지 합 / 구간 합

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
sum_arr = 0
m_remainder = [0] * m

for i in range(n):
    sum_arr += num_arr[i] # 구간 합을 구하고
    m_remainder[sum_arr % m] += 1   # m으로 modulo 연산을 해줌
                                    # 구간 합에서 나머지가 같은 구간의 개수를 확인

ans = m_remainder[0] # m으로 나눠지는 구간의 개수를 ans에 추가

for r in m_remainder:
    ans += r * (r - 1) // 2 # 나머지가 같은 구간끼리 빼준다 -> 나머지가 0인 구간이 된다.
    # 나머지가 같은 구간들 중에서 임의로 2개를 뽑는 것이므로 combinations 연산을 해준다.

print(ans)