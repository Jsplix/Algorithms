import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    r, c = map(int, input().split())
    layer = min(r, c)
    size = max(r, c)
    if r == c: # 정사각형 일 경우 필요한 화이트 초콜릿의 개수
        t_w = (((layer*(layer + 1)*(2 * layer + 1)) // 6) * 2 - layer**2)
        t_d = (((layer*(layer + 1)*(2 * layer + 1)) // 6) * 2 - layer**2 - layer)
    else: # 직사각형 일 경우 필요한 화이트 초콜릿의 개수
        t_w = (((layer*(layer + 1)*(2 * layer + 1)) // 6) * 2 + layer**2 * (size - layer - 1))
        t_d = (((layer*(layer + 1)*(2 * layer + 1)) // 6) * 2 - layer + layer**2 * (size - layer - 1))        
    print(t_w, t_d)