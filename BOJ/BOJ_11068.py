import sys
input = sys.stdin.readline
# [BOJ] 11068 회문인 수 / 수학, 브루트포스
def conv(decimal, base):
    values = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    ret = ''
    while decimal:
        ret += values[decimal % base]
        decimal //= base
    return ret 

for _ in range(int(input())):
    x = int(input())
    flag = False
    for i in range(2, 65):
        temp = conv(x, i)
        if temp == temp[::-1]: flag = True; break
    
    print(1 if flag else 0)