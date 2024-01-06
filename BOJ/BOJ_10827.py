import sys
input = sys.stdin.readline
# [BOJ] 10827 a^b / 임의 정밀도, 큰 수 연산
a, b = input().split()
f_len = len(a[a.index('.') + 1:])
a = int(a.replace('.', ''))
b = int(b)

res = a**b
dot_index = len(str(res)) - len(str( (10**f_len)**b) ) + 1 
# 뒤에 1 더해주는 이유: len(str( (10**f_len)**b) )은 결국 10의 제곱승임.
# 즉, 1이 포함된 길이. 소수점에서는 1의 길이가 아니라 0의 개수에 따라 소수점이 결정됨.
# 1의 길이가 포함되서 최종 길이에서 뺐으므로 다시 1을 더해줌.
res = str(res)

if dot_index >= 0:
    print(res[:dot_index] + "." + res[dot_index:])
else:
    print('0.' + '0'*(-dot_index)+res)