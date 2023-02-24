import sys
input = sys.stdin.readline
# [BOJ] 16206 롤케이크 / 그리디
n, m = map(int, input().split())
rollcakes = sorted(list(map(int, input().split())), key=lambda x: (x%10, x//10))

eat_count = 0
for rollcake in rollcakes:
    if m > 0:
        if rollcake < 10: continue
        elif rollcake % 10 == 0:
            q = rollcake//10
            if q-1 == 0: eat_count += 1
            else:
                if m >= q-1:
                    eat_count += q
                    m -= q-1
                else:
                    eat_count += m
                    break
        else:
            q = rollcake//10
            if m >= q:
                eat_count += q
                m -= q
            else:
                eat_count += m
                break
    else: break
                            
print(eat_count)