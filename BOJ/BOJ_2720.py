import sys
input = sys.stdin.readline
# [BOJ] 2720 세탁소 사장 동혁 / 수학, 그리디, 사칙연산
for _ in range(int(input())):
    coin = { 'Quarter': 25, 'Dime': 10, 'Nickel': 5, 'Penny': 1 }
    money = { 'Quarter': 0, 'Dime': 0, 'Nickel': 0, 'Penny': 0 }
    c = int(input())

    if c >= 25:
        money['Quarter'] = c // coin['Quarter']
        c %= 25
    if c >= 10:
        money['Dime'] = c // coin['Dime']
        c %= 10
    if c >= 5:
        money['Nickel'] = c // coin['Nickel']
        c %= 5
    if c >= 1:
        money['Penny'] = c // coin['Penny'] 
        c %= 1

    print(*list(map(int, money.values())))