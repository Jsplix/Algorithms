# [BOJ] 4344 평균은 넘겠지 / 수학, 사칙연산
case = int(input())
n_sc = [list(map(int, input().split())) for i in range(case)] # n - 학생 수 / sc

index = 0
t_sum = [] # sum of test score
st = [] # 평균을 넘은 학생 수를 기록
for i in range(case):
    t_sum.append(0)
    st.append(0)

for i in range(case):
    for j in range(1, len(n_sc[index])):
        t_sum[i] = sum(n_sc[i]) - n_sc[i][0] # 0번째는 학생 수이므로 성적과는 무관하다. 따라서 총 점수에서 빼준다.
        if n_sc[i][j] > t_sum[i] / (len(n_sc[index]) - 1):
            st[i] += 1
    index += 1

for i in range(case):
    print(format((st[i] / n_sc[i][0]) * 100, ".3f") + "%")