import sys
input = sys.stdin.readline

n = int(input())
mm_list = []

for i in range(n):
    mm_list.append(tuple(input().split()))

mm_list.sort(key= lambda x : x[1], reverse=True)
mm_list.sort(key= lambda x : x[0])

# (단어, 단어)의 튜플을 정렬할 때, 각각 서로다른 차순으로 정렬할 경우
# 정렬도 각각의 기준에 맞게 반대 순서로 따로따로 정렬 해줌

# 문제에서는 멘토는 오름차순, 멘티는 내림차순 정렬을 시킴
# 따라서, 멘티를 내림차순 정렬 해주고 그 결과를 다시 멘토에 대해서 오름차순 정렬을 해주었음.
for l in mm_list:
    print(*l)