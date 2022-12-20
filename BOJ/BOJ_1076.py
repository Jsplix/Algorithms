import sys
input = sys.stdin.readline
# [BOJ] 1076 저항 / 구현, 해쉬
resistance_value = {"black" : 0, "brown" : 1, "red" : 2, "orange" : 3, "yellow" : 4, "green" : 5, "blue" : 6, "violet" : 7, "grey" : 8, "white" : 9}
r = ''
for i in range(3):
    color = input().rstrip()
    if i == 2:
        r = int(r)
        r *= 10**(resistance_value[color])
    else:
        r += str(resistance_value[color])
print(r)