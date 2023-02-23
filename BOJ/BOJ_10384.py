from curses.ascii import isalpha
import sys
input = sys.stdin.readline
# [BOJ] 10384 팬그램 / 구현, 문자열
for test_case in range(int(input())):
    alphabet = [0 for _ in range(26)]
    pangram = input().lower()
    for c in pangram:
        if 97 <= ord(c) <= 122 : alphabet[ord(c)-ord('a')] += 1
    
    if min(alphabet) == 0: print("Case %d: Not a pangram" %(test_case+1))
    elif min(alphabet) == 1: print("Case %d: Pangram!" %(test_case+1))
    elif min(alphabet) == 2: print("Case %d: Double pangram!!" %(test_case+1))
    elif min(alphabet) == 3: print("Case %d: Triple pangram!!!" %(test_case+1))