import sys
input = sys.stdin.readline
# [BOJ] 12782 비트 우정지수 / 그리디
for _ in range(int(input())):
    a_bit, b_bit = map(list, map(str, input().rstrip().split()))
    diff = abs(a_bit.count('0') - b_bit.count('0'))
    cnt = 0
    chng = False
    if not diff:
        for i in range(len(a_bit)):
            if a_bit[i] != b_bit[i]:
                if chng: chng = False; continue
                else: cnt += 1; chng = True
                a_bit[i] = b_bit[i]
    else:
        idx = 0
        k = diff
        while k:
            if a_bit[idx] != b_bit[idx]:
                a_bit[idx] = b_bit[idx]
                k -= 1
            idx += 1

        for i in range(len(a_bit)):
            if a_bit[i] != b_bit[i]:
                if chng: chng = False; continue
                else: cnt += 1; chng = True
                a_bit[i] = b_bit[i]
    print(diff + cnt)