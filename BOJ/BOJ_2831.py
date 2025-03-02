import sys
from bisect import bisect_left
input = sys.stdin.readline
# [BOJ] 2831 댄스 파티 / 그리디, 정렬, 투포인터
def solve(shorter, higher):
    global result
    left = 0
    right = len(higher)-1

    while left < len(shorter) and right >= 0:
        if shorter[left] + higher[right] < 0:
            result += 1
            left += 1
            right -= 1
        else:
            right -= 1


n = int(input())
men = sorted(map(int, input().split()))
women = sorted(map(int, input().split()))
result = 0

# mpi - 남자 키가 양수가 되는 인덱스 / wpi - 여자 키가 양수가 되는 인덱스
mpi = bisect_left(men, 0)
wpi = bisect_left(women, 0)

solve(men[:mpi], women[wpi:])
solve(women[:wpi], men[mpi:])
print(result)