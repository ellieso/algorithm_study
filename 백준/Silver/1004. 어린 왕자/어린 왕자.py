# 진입/이탈횟수가 추가되는 경우
# 1. 출발점이나 도착점이 행성 내부에 위치한 경우
# 단, 출발점과 도착점이 모두 행성 내부에 위치해 있다면 진입/이탈횟수가 0이 된다.
# 테스트 케이스 개수
t = int(input())
for _ in range(t) :
    # 출발점, 도착점
    x1, y1, x2, y2 = list(map(int, input().split()))
    # 행성계의 개수
    n = int(input())
    count = 0
    for _ in range(n) :
        cx, cy, cr = map(int, input().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        pow_cr = cr**2

        if pow_cr > dis1 and pow_cr > dis2 :
            pass
        elif pow_cr > dis1 :
            count += 1
        elif pow_cr > dis2:
            count += 1
    print(count)        