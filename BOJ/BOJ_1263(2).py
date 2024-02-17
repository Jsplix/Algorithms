import sys
input = sys.stdin.readline
# [BOJ] 1263 시간 관리 / 그리디, 정렬
n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]
schedules.sort(key= lambda x:(x[1], x[0]))

overTime = 0
flag = False # 마감시간 초과 확인

if schedules[0][0] > schedules[0][1]:
    wakeTime = -1
    flag = True
else: 
    wakeTime = schedules[0][1] - schedules[0][0] # 늦잠 잘 수 있는 시간 (기상 시간)

now = schedules[0][1]
for i in range(1, n):
    now += schedules[i][0] # 일한 시간 더해줌
    if now > schedules[i][1]: # 마감 시간 초과
        flag = True
        overTime += (now-schedules[i][1]) # 초과 시간을 변수에 더해줌
        now = schedules[i][1] # 시간이 초과 된 경우 현재 시간을 가장 최근 작업의 마감시간으로 설정해줌
        # 기존의 경우, 초과된 시간이 계속 중첩됨 (즉, 1시간 초과했는데 그 이후의 작업에서 계속 1시간씩 중복 초과됨.)

if not flag: # 마감 초과하지 않은 경우
    print(wakeTime)
else:
    if overTime > wakeTime: # 초과 시간이 기상 시간보다 큰 경우
        print(-1) # 일을 마칠 수 없으므로 -1 출력
    else: # 늦잠 잘 시간이 초과 시간보다 더 많다면
        print(wakeTime - overTime) # 늦잠 잘 시간을 초과시간 만큼 줄임