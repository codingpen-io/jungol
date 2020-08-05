# 문제 : http://www.jungol.co.kr/theme/jungol/contestproblem.php?cid=1330&pid=2&stx=2
# a 낱개 가격
# b 송이에 달린 바나나갯수, c 한송이 가격
a, b, c = map(int, input().split())

n, m = map(int, input().split())

a_count = 0  # a 낱개로 사는게 유리한 경우의 수
b_count = 0  # b 송이로 사는게 유리한 경우의 수

# 낱개로 사는게 더 비싼 경우는 무조건 송이로 산다.
total_count = m - n + 1

if a < c/b:
    b_count = total_count
else:
    for i in range(n, m+1):
        a_cost = i * a
        b_cost = i // b * c
        # 송이에 있는 바나나와 원숭이 갯수가 나눠떨어지지 않으면 추가 송이 구입
        if i % b > 0:
            b_cost += c
        # 비용이 같을 경우 낱개로 구입하라고 문제 전제조건에 있음.
        if a_cost <= b_cost:
            a_count += 1
        else:
            b_count = total_count - a_count
            break

print(a_count)
print(b_count)
