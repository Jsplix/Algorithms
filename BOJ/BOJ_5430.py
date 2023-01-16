from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 5430 AC / 문자열, 파싱, 자료 구조, 덱
for _ in range(int(input())):
    func = input().rstrip()
    n = int(input())
    li = deque(input().rstrip()[1:-1].split(','))
    reverse_flag, exit_flag = 0, 0

    if n == 0: li = deque([])
    for f in func:
        if f == 'R': reverse_flag += 1
        else:
            if len(li) == 0: 
                exit_flag = 1
                print("error")
                break
            else: # 첫 번째를 버림 -> 입력된 배열을 기준으로 버리게 됨. 따라서 뒤집으면 마지막 원소를 pop해줌
                if reverse_flag % 2: li.pop()
                else: li.popleft()

    if not exit_flag:
        if reverse_flag % 2 == 0    :
            print("[" + ','.join(li) + "]")
        else:
            li.reverse()
            print("[" + ','.join(li) + "]")