import sys
input = sys.stdin.readline
# [BOJ] 17479 정식당 / 구현, 자료 구조, 해시를 사용한 집합과 맵
a, b, c = map(int, input().split())
menu = {}
normal, special, service = set(), set(), set()

for i in range(a):
    name, price = input().split()
    menu[name] = int(price)
    normal.add(name)

for i in range(b):
    name, price = input().split()
    menu[name] = int(price)
    special.add(name)

for i in range(c):
    name = input().rstrip()
    menu[name] = 1
    service.add(name)

n = int(input())
normal_total, special_total, service_total = 0, 0, 0
flag = False
for _ in range(n):
    order = input().rstrip()
    if order in normal:
        normal_total += menu[order]
    elif order in special:
        special_total += menu[order]
    elif order in service:
        if service_total: 
            flag = True
            break
        else:
            service_total += menu[order]

if service_total:
    if not (normal_total + special_total >= 50000):
        flag = True

if special_total:
    if not (normal_total >= 20000):
        flag = True

print("Okay" if not flag else "No")