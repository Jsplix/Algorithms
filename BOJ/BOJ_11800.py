import sys
input = sys.stdin.readline
# [BOJ] 11800 Tawla / 구현
alias = {1: 'Yakk', 2: 'Doh', 3: 'Seh', 4: 'Ghar', 5: 'Bang', 6: 'Sheesh'}
equals = {1: 'Habb Yakk', 2: 'Dobara', 3: 'Dousa', 4: 'Dorgy', 5: 'Dabash', 6: 'Dosh'}
for i in range(1, int(input())+1):
    a, b = map(int, input().split())
    if a == b: print("Case %d:" % i, equals[a])
    else:
        if (a == 6 and b == 5) or (a == 5 and b == 6): print("Case %d:" % i, "Sheesh Beesh"); continue 
        print("Case %d:" % i, alias[a] + ' ' + alias[b] if a > b else alias[b] + ' ' + alias[a])