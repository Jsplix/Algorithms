import sys
input = sys.stdin.readline
# [BOJ_SCUPC_C] 26266 비즈네르 암호 해독 / 브루트 포스, 문자열
clear_text = input().rstrip()
coded_text = input().rstrip()

coded = []
for t in coded_text:
    coded.append(ord(t) - ord('A') + 1)

key = []
for i in range(len(clear_text)):
    v = coded[i] - (ord(clear_text[i]) - ord('A') + 1)
    if v < 0:
        v += 26
    key.append(chr(v + ord('A') - 1))

num_list = []
t_len = len(clear_text)
for i in range(len(clear_text)):
    if t_len % (i + 1) == 0:
        num_list.append(i + 1)

if len(num_list) == 1:
    print(*key)
else:
    for x in range(len(num_list)):
        flag = False
        for i in range(1, t_len // num_list[x]):
            if num_list[x] == t_len:
                break
            for j in range(num_list[x]):
                if key[j] != key[(num_list[x] * i) + j]:
                    flag = True
                    break
        if not flag:
            print(''.join(key[:num_list[x]]))
            break