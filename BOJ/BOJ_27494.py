import sys
input = sys.stdin.readline
# [BOJ] 27494 2023년은 검은 토끼의 해 / 문자열, 브루트 포스
n = int(input())

def solve(num):
    lotto = str(num)
    two_index = lotto.find('2')
    if two_index == -1:
        return False
    zero_index = lotto.find('0', two_index)
    if zero_index == -1:
        return False
    two_index_2 = lotto.find('2', zero_index)
    if two_index_2 == -1:
        return False
    three_index = lotto.find('3', two_index_2)
    if three_index == -1:
        return False
    
    if two_index < zero_index < two_index_2 < three_index: return True
    else: return False

if n < 2023: print(0)
else:
    count = 0
    for i in range(2023, n+1):
        if solve(i): count += 1
    print(count)