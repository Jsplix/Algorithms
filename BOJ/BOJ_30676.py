import sys
input = sys.stdin.readline
# [BOJ] 30676 이 별은 무슨 색일까 / 구현
n = int(input())

if n >= 620 and n <= 780: print("Red")
elif n >= 590: print("Orange")
elif n >= 570: print("Yellow")
elif n >= 495: print("Green")
elif n >= 450: print("Blue")
elif n >= 425: print("Indigo")
elif n >= 380: print("Violet")