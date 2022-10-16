n = int(input())
li = []

for _ in range(n):
    li.append(input())
# 값 넣기

li = sorted(list(set(li)))
# 중복 값 제거한 뒤 알파벳 순으로 정렬
a = []

for l in range(1, 51):
    for st in li:
        if len(st) == l:
            a.append(st)
#길이가 적은 순으로 배열에 넣기 길이는 50까지로 정해져 있음
#미리 알파벳순으로 정렬해서 같은 길이라도 앞파벳 순으로 들어가짐

print(a)
