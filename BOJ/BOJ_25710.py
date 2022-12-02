import sys
input = sys.stdin.readline
# [BOJ] 25710 점수 계산 / 브루트 포스
n = int(input())
l = list(map(int, input().split()))
chk = [0 for _ in range(1000)]

for x in l:
    chk[x] += 1 
# 배열의 크기는 최대 10만까지 가능하나, 수의 범위가 1~999까지임.
# 그래서, 999를 2중 반복문으로 실행 -> O(1000**2)

num_list = []

for i in range(1, 1000):
    if chk[i] == 1: 
        num_list.append(i)
    elif chk[i] >= 2: # 2이상인 경우 똑같은값 2개를 추가해줌.
        num_list.append(i)
        num_list.append(i)
# 2이상인 경우 결국 자기 자신의 제곱의 값을 구하는 것이기 때문에 아무리 커도 2개만 추가해주면 됨
ans = []

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        temp = num_list[i] * num_list[j]
        ans.append(sum(list(map(int, str(temp)))))

print(max(ans))