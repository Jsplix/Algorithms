import sys
input = sys.stdin.readline
# [BOJ] 2600 구슬게임 / DP, 게임 이론, 스프라그-그런디
# 스프라그-그런디 알고리즘의 개념이 너무 어려워서 비슷한 게임 문제를 풀어봐야 할 듯함.
b_arr = list(map(int, input().split()))
dp = [0 for _ in range(501)]

for i in range(1, 501):
    chk = [False for _ in range(4)] # 13행에 의해 0~3을 확인하기 위해 만들어줌.
    for j in range(3):
        if i - b_arr[j] >= 0:
            chk[dp[i - b_arr[j]]] = True

    # 그런디 수: 0 이상의 정수이면서 check 에서 False인 수 (위 문제에서는 0~3사이의 범위: 4개)
    # 0이상의 정수 집합 중 다음 갈 수 있는 단계(값)을 제외한 가장 작은 정수값
    # 즉, N = 4일 경우, 다음 갈 수 있는 단계(값)은 (b1, b2, b3가 1, 3, 4라면) 0, 1, 3이 됨(각각 4, 3, 1개씩 뽑을 경우)
    # 0, 1, 3에 대한 그런디 수는 N = 4 이전에 정의되므로 mex값이 구해짐 (mex: Minimum EXcluded number) 
    mex = 0 # 그런디 수를 구하는 과정
    while chk[mex]:
        mex += 1
    
    dp[i] = mex

for _ in range(5):
    k1, k2 = map(int, input().split())
    if dp[k1] ^ dp[k2] == 0: print("B") # XOR연산의 결과가 0이 될 경우 후공이 무조건 이김
    else: print("A") # 그 외의 경우는 선공 필승