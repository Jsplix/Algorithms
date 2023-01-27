import sys
input = sys.stdin.readline
# [BOJ] 1744 수 묶기 / 그리디, 정렬, 많은 조건 분기
arr = []
for _ in range(int(input())):
    arr.append(int(input()))

arr.sort()
arr_sum = sum(arr)

i, v = len(arr) - 1, 0

while i >= 0:
    if i == 0: # arr의 원소가 1개인 경우:
        v += arr[i]
        break
    if arr[i] > 0 and arr[i - 1] > 0:
        if arr[i] + arr[i - 1] > arr[i] * arr[i - 1]:
            v += arr[i]
            i -= 1
        else:
            v += (arr[i] * arr[i - 1])
            i -= 2
    elif arr[i] >= 0 and arr[i - 1] <= 0:
        if arr[i] == 0 and arr[i - 1] == 0: # 둘 다 0
            v += arr[i]
            i -= 1
        else: # 둘 중 한 개가 0일 경우(양수, 0 / 0, 음수) + 양수, 음수인 경우
            if arr[i] > 0 and arr[i - 1] == 0:
                v += arr[i]
                i -= 1
            elif arr[i] == 0 and arr[i - 1] < 0:
                if len(arr[:i + 1]) % 2 == 1:
                    v += arr[i]
                    i -= 1
                else:
                    v += arr[i] * arr[i - 1]
                    i -= 2
            else:
                if len(arr[:i]) >= 2:
                    if len(arr[:i + 1]) % 2 == 1:
                        v += arr[i]
                        i -= 1
                    else:
                        v += arr[i] + arr[i - 1]
                        i -= 2
                else:
                    v += arr[i] + arr[i - 1]
                    i -= 2
    else: # 남은 수가 모두 음수일 경우
        if len(arr[:i + 1]) >= 2:
            if len(arr[:i + 1]) % 2 == 1:
                v += arr[i]
                i -= 1
            else:
                v += arr[i] * arr[i - 1]
                i -= 2
        else:
            v += arr[i] * arr[i - 1]
            i -= 2
print(max(v, arr_sum))