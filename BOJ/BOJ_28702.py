import sys
input = sys.stdin.readline
# [BOJ] 28702 FizzBuzz / 수학, 문자열
num = [0, 0]
for i in range(3):
    fb = input().rstrip()

    if fb.isalpha():
        continue
    else:
        num[0] = int(fb)
        num[1] = i

result = num[0] + (3 - num[1])
if result % 3 == 0 and result % 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0 and result % 5 != 0:
    print("Fizz")
elif result % 3 != 0 and result % 5 == 0:
    print("Buzz")
else:
    print(result)