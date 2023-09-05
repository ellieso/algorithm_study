# 알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 
# 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구한다.

n = int(input()) # 채팅방의 기록 수를 나타내는 값
chat_list = set()
cnt = 0
for _ in range(n) : #n개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어짐
    chat = input()
    # ENTER가 아니고, 새로 접속한 사람이 아니면 횟수 증가
    if chat != 'ENTER' :
        if chat not in chat_list :
            cnt += 1
            chat_list.add(chat)
    # ENTER이면, 기존에 접속한 회원 정보 초기화
    elif chat == 'ENTER' :
        chat_list.clear()
print(cnt)