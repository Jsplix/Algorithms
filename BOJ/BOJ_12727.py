import sys
import decimal
input = sys.stdin.readline
# [BOJ] 12727 Numbers(Small) / 수학, 임의 정밀도, 큰 수 연산, 런타임 전의 전처리
a = decimal.Decimal('3')
b = decimal.Decimal('5').sqrt()
for i in range(1, int(input())+1):
    res = str(int((a+b)**int(input())))
    if len(res) < 3: res = '0' * (3 - len(res)) + res
    else: res = res[-3:]
    print("Case #%d:" % i, res)