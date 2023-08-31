num = int(input())
hansu = 0

for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    #  자리 숫자는 등차수열인지 비교대상이 없기 때문에 모두 한수
    if i < 100:
        hansu += 1 
    # 변수 i가 100 이상인 경우 3자리 숫자를 앞의 두 자리의 차이와 뒤의 두 자리의 차이가 같으면 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1
print(hansu)