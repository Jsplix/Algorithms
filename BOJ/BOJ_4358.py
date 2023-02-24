import sys
input = sys.stdin.readline
# [BOJ] 4358 생태학 / 자료 구조, 문자열, 해시를 사용한 집합과 맵
count = 0
trees = {}
while True:
    tree = input().rstrip()
    if tree == "": break
    if tree not in trees.keys(): trees[tree] = 1
    else: trees[tree] += 1
    count += 1

distribution = [(k, v) for (k, v) in trees.items()]
distribution.sort()
for i in range(len(trees.keys())): 
    print(distribution[i][0], '%.4f' % ((distribution[i][1]*100)/count))