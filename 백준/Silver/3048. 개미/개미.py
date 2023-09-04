# 두 그룹이 만났을 때, 1초에 한번씩 개미는 서로를 뛰어 넘는다.
# 하지만 모든 개미가 점프를 하는 것은 아니다. 자신의 앞에 반대 방향으로 움직이던 개미가 있는 경우에만 점프를 하게 된다.
# 첫 번째 개미 그룹은 왼쪽에서 오른쪽으로 움직이고, 두 번째 그룹은 반대 방향으로 움직인다.

n1, n2 = list(map(int, input().split())) # 첫 번째 줄에 첫 번째 그룹의 개미의 수 N1과 두 번째 그룹의 개미의 수 N2가 주어진다.
n1_ant = list(input())
n2_ant = list(input())
t = int(input()) # 마지막 줄에는 T

n1_ant.reverse()
total_ant = n1_ant + n2_ant

# t초동안 반복
for _ in range(t):
    # 반복문을 통해 두 개미 그룹을 확인
    for i in range(len(total_ant) - 1):
        # 두 개미 그룹이 만났다면 위치를 바꾼다.
        if total_ant[i] in n1_ant and total_ant[i + 1] in n2_ant:
            total_ant[i], total_ant[i + 1] = total_ant[i + 1], total_ant[i]

            # 위치를 바꾼 개미가 선두 개미이면 반복을 멈춘다.
            if total_ant[i + 1] == n1_ant[-1]:
                break

print("".join(total_ant))