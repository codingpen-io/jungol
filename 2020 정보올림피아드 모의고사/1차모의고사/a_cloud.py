# N 도시의 수, M 구름의 수, K 날짜
# p[i](구름의 위치), s[i](구름의 크기), v[i](구름의 속도)

N, M, K = map(int, input().split())

p = []
s = []
v = []

for i in range(M):
    p1, s1, v1 = map(int, input().split())
    p.append(p1)
    s.append(s1)
    v.append(v1)

count = 0
# 첫날 부터 K일까지 루프를 돌면서 비가내리는 도시를 탐색
for i in range(0, K+1):
    # 도시를 순서대로 탐색
    for j in range(1, N+1):
        sum_cloud = 0  # 구름의 합 초기화
        for k in range(len(p)):
            if p[k] == j:
                sum_cloud += s[k]
        if sum_cloud >= 100:
            count += 1

    # 속도 v만큼 하루가 지나면 구름을 전진
    for x in range(len(p)):
        p[x] += v[x]

print(count)
