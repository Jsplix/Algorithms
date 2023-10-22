import sys
input = sys.stdin.readline
# [BOJ] 11557 Yangjojang of The Year / 구현, 정렬
for _ in range(int(input())):
    mx = 0
    mx_school = ''
    for __ in range(int(input())):
        school, drink = input().split()
        drink = int(drink)
        if drink > mx:
            mx = drink
            mx_school = school
    print(mx_school)