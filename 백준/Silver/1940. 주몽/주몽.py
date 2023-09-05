# 갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다

n = int(input()) # 재료의 개수
m = int(input()) # 갑옷을 만드는데 필요한 수
n_material = list(map(int, input().split())) # N개의 재료들이 가진 고유한 번호

# 고유한 번호를 정렬한다
n_material.sort()
cnt = 0

# 양 끝값에서 둘의 합이 m과 같으면 cnt를 더하고 위치를 하나씩 옮긴다
i, j = 0, n-1
while i<j :
    if n_material[i] + n_material[j] == m :
        cnt += 1
        i += 1
        j -= 1
    elif n_material[i] + n_material[j] < m :
        i += 1
    else :
        j -= 1
print(cnt)