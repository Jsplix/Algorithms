import sys
input = sys.stdin.readline

study_record = []
chk, boj = [], []
for _ in range(int(input())):
    study = input().rstrip()
    if 'boj.kr/' in study:
        boj.append((study, int(study[7:])))
    else:
        chk.append((study, len(study)))

chk.sort(key=lambda x:(x[1], x[0]))
boj.sort(key=lambda x:x[1])
for i in range(len(chk)):
    study_record.append(chk[i][0])
for j in range(len(boj)):
    study_record.append(boj[j][0])
print(*study_record, sep='\n')
