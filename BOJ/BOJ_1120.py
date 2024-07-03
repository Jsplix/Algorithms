import sys
input = sys.stdin.readline
# [BOJ] 1120 문자열 / 문자열, 브루트포스
def compare(str_a: str, str_b: str):
    ret = 1000
    cnt = 0
    if len(str_a) == len(str_b):
        if str_a == str_b: ret = 0
        else:
            for i in range(len(str_a)):
                if str_a[i] != str_b[i]: cnt += 1
            ret = cnt        
    else:
        if str_a not in str_b:
            for i in range(len(str_b)-len(str_a)+1):
                cnt = 0
                for j in range(len(str_a)):
                    if str_a[j] != str_b[i+j]:
                        cnt += 1
                ret = min(cnt, ret)
        else:
            ret = 0
    
    return ret

a, b = input().split()
print(compare(a, b))