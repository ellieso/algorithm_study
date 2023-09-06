# 경민이를 위해 메모장에서 비밀번호를 찾는 프로그램을 만들기
n, m = list(map(int, input().split())) # 첫째 줄에 저장된 사이트 주소의 수,  비밀번호를 찾으려는 사이트 주소의 수
password_dict = {}
for _ in range(n) : 
    url, password = list(map(str, input().split()))
    password_dict[url] = password
for _ in range(m) :
    find_password = input()
    print(password_dict[find_password])