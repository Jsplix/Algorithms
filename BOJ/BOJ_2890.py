import re # 정규표현식 사용을 위한 모듈 추가
import sys
input = sys.stdin.readline
# [BOJ] 2890 카약 / 구현, 문자열, 정렬
r, c = map(int, input().split())
lane = []
seq = []
for _ in range(r):
    lane = re.split('[0-9]{2}', input().rstrip()) # 숫자를 기준으로 두개로 split됨
    if lane[0].count('.') != c - 2:
        seq.append((int(lane[1][0]), ((c - 5) - lane[0].count('.'))))
        # (카약 번호, 순위[0-8])인 튜플 형태를 리스트에 저장

seq.sort(key = lambda x:x[1]) # 등수에 대해 정렬
k = 0
rank = {}

for t in range(len(seq)):
    if seq[t][1] not in rank.values() and seq[t-1][1] != seq[t][1]:
        rank[seq[t][0]] = k
        k += 1
    if seq[t - 1][1] == seq[t][1]:
        if t == 0:
            rank[seq[t][0]] = k
            k += 1
        else:
            rank[seq[t][0]] = rank[seq[t-1][0]]
        # if t == len(seq) - 1:
        #     rank[seq[t][0]] = rank[seq[t-2][0]]
    # '.'의 개수를 통해서 순위를 매기기 때문에 중간에 비는 숫자가 생김.
    # 순위에 대해서 다시 counting을 해줌.
for i in range(1, 10):
    print(rank[i] + 1) # dictionary는 정렬이 되지 않은 상태이므로, 반복문을 통해서 카약의 번호가 몇등인지 출력


# 첫 제출에서 KeyError가 발생 -> 27번째 줄에서 rank[i]의 key가 없어서 발생했음. (첫 번째 예제 입력을 한 경우)
# 처음에 seq에 카약에 정보를 저장할 때, 등수를 0-8로 저장했고, rank에 저장할 때 k값을 통해서 저장함 [k = 1로 시작했음]
# 이 때, 예제 입력 1에서 1번 카약이 등수가 1이므로 1: 1의 형태로 딕셔너리에 저장되어 있었음. 그리고, seq에서 2번 카약이
# 2등인데 0부터 counting 되었기 때문에 (2, 1)로 되어서 19번째 줄의 if 줄에서 1이 이미 저장되어 있어서 건너뛰게 되었음(2로 저장되지 않고)
# 그래서, k를 0부터로 바꿔주면 위와 같은 중첩 현상이 발생하지 않음 seq 튜플의 순위도 0부터이고, k도 0부터 counting 되므로

# 2차 제출에서도 KeyError 발생 -> 왜??????????????????????????????????????????????????????
# 반례 => 
# 10 10
# S.....111F
# S.....222F
# S.....333F
# S.....444F
# S.....555F
# S.....666F
# S.....777F
# S.....888F
# S.....999F
# S........F
# 22번째 줄 if seq[t - 1][1] == seq[t][1]: 에서 1번 카약과 9번 카약이 같은 경우 기존의 코드
# rank[seq[t][0]] = rank[seq[t-1][0]] 에서 rank[seq[t - 1][0]]의 key값이 정의되지 않았기 때문에 발생 
# (즉, 1번(키 값) 카약에 대한 등수 저장을 하려는데 모든 카약의 등수가 같기 때문에 이전에 저장된 키 값이 없는데 키 값의 밸류값을 참조했기 때문임.)