import sys
input = sys.stdin.readline
# [BOJ] 1308 D-Day / 구현
def isLeap(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: return True
    return False

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6:30, 7:31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
today = list(map(int, input().split()))
dday = list(map(int, input().split()))

if dday[0] - today[0] >= 1000:
    if dday[0] - today[0] == 1000 and dday[1] >= today[1] and dday[2] >= today[2]: print("gg") ; exit(0)
    elif dday[0] - today[0] > 1000: print("gg") ; exit(0)

yday = 0
for y in range(today[0], dday[0]):
    if isLeap(y): yday += 366
    else: yday += 365

l = 0
for m in range(1, dday[1]):
    if m == 2 and isLeap(dday[0]): l += days[m] + 1 ; continue
    l += days[m]
l += dday[2]

k = 0
for m in range(1, today[1]):
    if m == 2 and isLeap(today[0]): k += days[m] + 1 ; continue
    k += days[m]
k += today[2]

yday += l
print("D-", yday-k, sep='')