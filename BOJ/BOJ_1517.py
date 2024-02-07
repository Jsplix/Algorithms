import sys
input = sys.stdin.readline
# [BOJ] 1517 버블 소트 / 자료 구조, 정렬, 세그먼트 트리, 분할 정복
def mergeSort(start, end):
    global arr, count
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        temp = []
        left, right = start, mid + 1
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else: 
                # 이 시점에서 left ~ mid에 해당하는 arr값은 모두 arr[right] 보다 큰 값이므로 left부터 mid까지 원소 개수로 더함.
                temp.append(arr[right])
                right += 1
                count += (mid - left) + 1
        
        if left <= mid:
            temp += arr[left:mid+1]
        if right <= end:
            temp += arr[right:end+1]
        
        for i in range(len(temp)):
            arr[start+i] = temp[i]

n = int(input())
arr = list(map(int, input().split()))
count = 0
mergeSort(0, n-1)
print(count)