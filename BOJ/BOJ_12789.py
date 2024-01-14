import sys
input = sys.stdin.readline
# [BOJ] 12789 도키도키 간식드리미 / 자료 구조, 스택
def check_temp(tmp: list):
    global now
    while tmp:
        if tmp[-1] == now:
           chk.append(tmp.pop())
           now += 1
        else:
            return

n = int(input())
wait = list(map(int, input().split()[::-1]))
temp = []

now = 1
chk = []
while wait:
    check_temp(temp) # 뽑기 전 기존의 대기열에 마지막에 다음 순번이 있는지 확인하고 있다면 빼줌
    if wait[-1] == now:
        chk.append(wait.pop())
        now += 1
    else:
        temp.append(wait.pop())
    check_temp(temp) # 뽑은 후 다음 순번이 temp 마지막에 먼저 들어가 있는지 확인하고 있다면 빼줌

temp.reverse()
if chk + temp == [i for i in range(1, n+1)]:
    print("Nice")
else:
    print("Sad")