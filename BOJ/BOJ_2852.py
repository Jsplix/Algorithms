import sys
input = sys.stdin.readline
# [BOJ] 2852 NBA 농구 / 구현, 문자열
n = int(input())
record = 0 # 1팀이 득점할 경우 +1, 2팀이 득점한 경우 -1
winTime_t1, winTime_t2 = 0, 0

for i in range(n):
    team, time = input().split()
    mm, ss = map(int, time.split(':'))

    if team == '1':
        if record == 0:
            winTime_t1 += 60*48 - (60*mm + ss)
        record += 1
        if record == 0:
            if winTime_t2 > 0:
                winTime_t2 -= (60*48 - (60*mm + ss))
    else:
        if record == 0:
            winTime_t2 += 60*48 - (60*mm + ss)
        record -= 1
        if record == 0:
            if winTime_t1 > 0:
                winTime_t1 -= (60*48 - (60*mm + ss))

print("{:0>2}:{:0>2}".format(winTime_t1//60, winTime_t1%60))
print("{:0>2}:{:0>2}".format(winTime_t2//60, winTime_t2%60))