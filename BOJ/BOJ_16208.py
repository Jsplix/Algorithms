import sys
input = sys.stdin.readline

# [BOJ] 16208 귀찮음 / 수학, 정렬, 그리디
# 곱한 값이 최소가 되게 하려면 길이의 최댓값과 최솟값을 곱해주면 됨
# 길이의 총합에서 가장 작은 길이를 만들기 위해서 나눠주고 곱하면 됨

n = int(input())
a = list(map(int, input().split()))
a.sort()
total_len = sum(a)
price = 0
for i in range(n):
    total_len -= a[i] # 막대 나눔
    price += (a[i]*total_len) # 비용 구해서 최종 비용에 더함
print(price)