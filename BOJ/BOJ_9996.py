import sys
input = sys.stdin.readline
# [BOJ] 9996 한국이 그리울 땐 서버에 접속하지 / 문자열, 정규 표현식
n = int(input())
patterns = input().rstrip('\n').split('*')
files = [input().rstrip() for _ in range(n)]

for file_name in files:
    lm, rm = patterns[0], patterns[1]
    
    cnt = 0
    if len(lm) + len(rm) > len(file_name): # 패턴이 파일이름보다 더 긴 경우
        print("NE")
    else:
        if lm == file_name[:len(lm)] and rm == file_name[-len(rm):]:
            print("DA")
        else:
            print("NE")