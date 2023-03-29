import sys
input = sys.stdin.readline
# [BOJ] 12933 오리 / 그리디, 문자열, 구현
crying_sound = input().rstrip()
if len(crying_sound) % 5 != 0: print(-1); exit(0)
visited = [0 for _ in range(len(crying_sound))]
duck = 0

def solve(start):
    global duck
    sound = 'quack'
    idx = 0
    check = True
    
    for i in range(start, len(crying_sound)):
        if crying_sound[i] == sound[idx] and not visited[i]:
            idx += 1
            visited[i] = 1 # 한 마리가 여러번 우는 것은 visited 처리만 함
            if crying_sound[i] == 'k':
                if check: duck += 1; check = False # check 부분을 통해서 건너뜀, 
                # 첫 울음소리가 끝나면 False되고, 그 이후는 해당 오리의 다른 울음 소리만 확인하고 넘어감
                idx = 0
                continue
            # idx += 1

for i in range(len(crying_sound)):
    if crying_sound[i] == 'q' and not visited[i]:
        solve(i)

if not all(visited) or not duck: print(-1)
else: print(duck)