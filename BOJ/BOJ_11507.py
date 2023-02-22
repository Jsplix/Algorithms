import sys
input = sys.stdin.readline
# [BOJ] 11507 카드 셋트 / 자료 구조, 문자열, 파싱, 해시를 사용한 집합과 맵
s = input().rstrip()
deck = {}
chk = [[] for _ in range(4)]
let = {'P': 0, 'K': 1, 'H': 2, 'T': 3}
for i in range(0, len(s), 3):
    num = s[i+1:i+3]
    if let[s[i]] not in deck:
        deck[let[s[i]]] = 1
        chk[let[s[i]]].append(num)
    else: 
        deck[let[s[i]]] += 1
        if num in chk[let[s[i]]]:
            print("GRESKA")
            exit(0)
        else:
            chk[let[s[i]]].append(num)

print(13-len(chk[0]), 13-len(chk[1]), 13-len(chk[2]), 13-len(chk[3]), sep=' ')