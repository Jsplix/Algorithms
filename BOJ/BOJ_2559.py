import sys
input = sys.stdin.readline
# [BOJ] 2559 수열 / 구간 합
n, k = map(int, input().split())
l = list(map(int, input().split()))
chk = [sum(l[:k])]
# 각 구간의 슬라이싱의 합을 구함 -> 시간초과
for i in range(n - k):
    chk.append(chk[i] - l[i] + l[i + k]) 
    # 위와 같이 sum연산을 하지 않고 최초 1회에만 chk에 구간 합을 구하고
    # 그 이후는 구간의 가장 첫번째 element는 빼고 구간 바로 옆 element를 추가해줌
    # 구간이 자리를 옮기는 듯한 처리를 통해서 구간 합을 구할 수 있음 -> sum연산을 통한
    # 시간 복잡도가 개선됨

print(max(chk))