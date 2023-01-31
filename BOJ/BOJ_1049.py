import sys
input = sys.stdin.readline
# [BOJ] 1049 기타줄 / 수학, 그리디
n, m = map(int, input().split())
brand = [tuple(map(int, input().split())) for _ in range(m)]
pay = 0

package_sort = sorted(brand)
individual_sort = sorted(brand, key=lambda x:x[1])

p_all = package_sort[0][0]*((n//6)+1)
pi_pair = package_sort[0][0]*(n//6)+individual_sort[0][1]*(n%6)
i_all = individual_sort[0][1]*n

if n <= 6:
    pay += min(package_sort[0][0], i_all)
else:
    if pi_pair < i_all:
        if p_all < pi_pair:
            pay += p_all
        else: pay += package_sort[0][0]*(n//6)+individual_sort[0][1]*(n%6)
    else: pay += i_all

print(pay)