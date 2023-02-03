import sys
input = sys.stdin.readline
# [BOJ] 5426 비밀 편지 / 수학, 구현, 문자열
for _ in range(int(input())):
    letter = input().rstrip()
    n = int(len(letter)**0.5)
    let = ''
    for i in range(n):
        let += letter[n-1-i:len(letter):n]
    print(let)
# 굳이 2차원 행렬을 만들지 않고 슬라이싱을 이용해서 구할 수 있음.
# 가장 마지막 열, 첫번째 행부터 마지막 행까지 열을 바꿔가며 내용 복원 가능