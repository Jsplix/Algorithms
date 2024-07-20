import sys
input = sys.stdin.readline
# [BOJ] 10453 문자열 변환 / 애드 혹, 문자열
for _ in range(int(input())):
    A, B = input().rstrip().split()
    A = list(A)
    B = list(B)

    # a의 위치만 고려 → a의 위치만 B의 a위치에 동일하게 맞춰준다
    length = len(A)

    # A에서 a의 위치를 저장
    check_A = []
    # B에서 a의 위치를 저장
    check_B = []
    for i in range(length):
        if A[i] == 'a':
            check_A.append(i)
        if B[i] == 'a':
            check_B.append(i)
    
    count = 0
    for j in range(len(check_A)):
        if check_A[j] != check_B[j]:
            count += abs(check_A[j] - check_B[j])
    print(count)