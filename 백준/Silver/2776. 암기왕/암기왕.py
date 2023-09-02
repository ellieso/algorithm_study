t = int(input()) # 테스트케이스 개수 T
for _ in range(t) :
    note_one = int(input()) # 수첩 1에 적어 놓은 정수의 개수
    note_one_number = set(map(int, input().split())) # 수첩 1에 적혀 있는 정수
    note_two = int(input()) # 수첩 2에 적어 놓은 정수의 개수
    note_two_number = list(map(int, input().split())) # 수첩 2에 적혀 있는 정수
    # 수첩2에 적혀있는 M개의 숫자 순서대로 수첩 1에 있으면 1을 없으면 0을 출력
    for n in note_two_number :
        if n in note_one_number :
            print(1)
        else :
            print(0)