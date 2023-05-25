n, m = map(int, input().split())
# [BOJ] 19944 뉴비의 기준은 뭘까? / 구현
if m == 1 or m == 2:

    print("NEWBIE!")

elif m <= n and m != 1 and m != 2:

    print("OLDBIE!")

else:

    print("TLE!")
