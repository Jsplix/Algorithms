import sys
input = sys.stdin.readline

# [BOJ] 1644 소수의 연속합 / 수학, 정수론, 에라토스테네스의 체, 소수 판정, 투 포인터

def sieve_eratosthenes():
    global answer, n
    prime_nums = [i for i in range(n+1)]
    prime_nums[1] = 0
    for i in range(2, n+1):
        if not prime_nums[i]: continue
        for j in range(i*i, n+1, i):
            prime_nums[j] = 0
    
    if prime_nums[n]: answer += 1

    return [prime_num for prime_num in range(2, n+1) if prime_nums[prime_num]]

n = int(input())
l, r = 0, 1
answer = 0
if n == 1: print(0)
elif n == 2: print(1)
else:
    solve = sieve_eratosthenes()
    chk = solve[0]
    while True:
        if chk < n:
            chk += solve[r]
            if r != len(solve)-1: r += 1
        else:
            if chk == n:
                answer += 1
                chk -= solve[l]
                l += 1
            else:
                chk -= solve[l]
                l += 1
        
        if l == len(solve)-1: break
    print(answer)
