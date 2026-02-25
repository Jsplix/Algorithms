import sys
input = sys.stdin.readline
# [BOJ] 2310 어드벤처 게임 / 그래프 이론, 그래프 탐색, BFS, DFS
def dfs(room_id, money):
    global N, result

    if rooms[room_id][0] == 3 and rooms[room_id][1] > money:
        return
    
    if room_id == N:
        result = True
        return

    if rooms[room_id][0] == 3:
        money -= rooms[room_id][1]
    elif rooms[room_id][0] == 2:
        money = max(rooms[room_id][1], money)

    for i in range(2, len(rooms[room_id])):
        next_room_id = rooms[room_id][i]
        if not visited[next_room_id]:
            visited[next_room_id] = True
            dfs(next_room_id, money)
            visited[next_room_id] = False
    
while True:
    N = int(input())

    if not N: break
    rooms = [[]]
    result = False
    visited = [False for _ in range(N + 1)]
    for i in range(1, N + 1):
        info, *room_info = input().split()
        # 1: 빈 방, 2: 레프리콘, 3: 트롤
        if info == 'E':
            rooms.append([1] + list(map(int, room_info[:-1])))
        elif info == 'L':
            rooms.append([2] + list(map(int, room_info[:-1])))
        elif info == 'T':
            rooms.append([3] + list(map(int, room_info[:-1])))
    
    visited[1] = True
    dfs(1, 0)
    
    print("Yes" if result else "No")