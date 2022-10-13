import sys
input = sys.stdin.readline

x, y = map(int, input().split())
calendar = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }
day = { 0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN" }
total = 0
for i in range(1, x):
    total += calendar[i]
total += y - 1

print(day[total % 7])