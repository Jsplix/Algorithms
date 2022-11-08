import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2 
    # 문제에서는 배열의 개수가 홀수개일 때, 1 2 3 4 5 에서 1 2 3 / 4 5 이런 식으로
    # divide하고 정렬 후 conquer 하기 때문에 mid를 계산할 때 +1 한 값을 2로 나눠준다.
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])
    
    i, j = 0, 0
    merged_arr = []
    while i < len(low) and j < len(high):
        if low[i] < high[j]:
            merged_arr.append(low[i])
            chk.append(low[i])
            i += 1
        else:
            merged_arr.append(high[j])
            chk.append(high[j])
            j += 1

    while i < len(low):
        merged_arr.append(low[i])
        chk.append(low[i])
        i += 1
    while j < len(high):
        merged_arr.append(high[j])
        chk.append(high[j])
        j += 1
    return merged_arr


n, k = map(int, input().split())
arr = list(map(int, input().split()))
chk = []
sorted_arr = merge_sort(arr)
if len(chk) >= k:
    print(chk[k - 1])
else:
    print(-1)