# 입력 받기
n = int(input())
records = []

for _ in range(n):
    record = input()
    records.append(record)

# 백준 문제와 다른 공부 기록 분리
baekjoon_records = []
other_records = []

for record in records:
    if record.startswith("boj.kr/"):
        baekjoon_records.append(record)
    else:
        other_records.append(record)

# 다른 공부 기록 정렬
other_records.sort(key=lambda x: (len(x), x))

# 백준 문제 기록 정렬
baekjoon_records.sort(key=lambda x: int(x.split("/")[-1]))

# 결과 출력
for record in other_records + baekjoon_records:
    print(record)