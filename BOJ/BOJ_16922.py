import sys
input = sys.stdin.readline
# [BOJ] 16922 로마 숫자 만들기 / 수학, 구현, 브루트 포스, 백트래킹, 조합론
rome_num = ['I', 'V', 'X', 'L']
rome_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
answer = []
def back(idx, val, chk: list):
    global n
    if len(chk) == n:
        answer.append(val)
        return
    
    for r in range(idx, 4):
        chk.append(rome_num[r])
        val += rome_val[rome_num[r]]
        back(r, val, chk)
        val -= rome_val[rome_num[r]]
        chk.pop()

n = int(input())
back(0, 0, [])
print(len(set(answer)))