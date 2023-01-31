import sys
input = sys.stdin.readline
# [BOJ] 20436 ZOAC 3 / 구현, 시뮬레이션
keyboard_l = {'q':(0, 0), 'w':(0, 1), 'e':(0, 2), 'r':(0, 3), 't':(0, 4),
            'a':(1, 0), 's':(1, 1), 'd':(1, 2), 'f':(1, 3), 'g':(1, 4),
            'z':(2, 0), 'x':(2, 1), 'c':(2, 2), 'v':(2, 3), }

keyboard_r = {'y':(0, 5), 'u':(0, 6), 'i':(0, 7), 'o':(0, 8), 'p':(0, 9),
              'h':(1, 5), 'j':(1, 6), 'k':(1, 7), 'l':(1, 8),
              'b':(2, 4), 'n':(2, 5), 'm':(2, 6) }

sl, sr = input().split()
cmp = input().rstrip()
now_l, now_r = keyboard_l[sl], keyboard_r[sr]

answer = 0
for c in cmp:
    if c == now_l or c == now_r:
        answer += 1
        continue

    if c in ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']:
        answer += abs(now_l[0]-keyboard_l[c][0]) + abs(now_l[1]-keyboard_l[c][1]) + 1
        now_l = keyboard_l[c]
    else:
        answer += abs(now_r[0]-keyboard_r[c][0]) + abs(now_r[1]-keyboard_r[c][1]) + 1
        now_r = keyboard_r[c]

print(answer)