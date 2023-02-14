import sys
input = sys.stdin.readline
# [BOJ] 19583 싸이버개강총회 / 구현, 자료 구조, 문자열, 해시를 사용한 집합과 맵
s, e, q = input().split()
check = {}
while True:
    try:
        time, nick_name = input().split()
        s_h, s_m = map(int, s.split(':'))
        e_h, e_m = map(int, e.split(':'))
        q_h, q_m = map(int, q.split(':'))
        h, m = map(int, time.split(':'))

        if (60*h)+m <= (60*s_h)+s_m:
            check[nick_name] = 1
        elif (60*e_h)+e_m <= (60*h)+m <= (60*q_h)+q_m and nick_name in check.keys():
            check[nick_name] = 0
        else:
            continue
    except:
        break

print(list(check.values()).count(0))