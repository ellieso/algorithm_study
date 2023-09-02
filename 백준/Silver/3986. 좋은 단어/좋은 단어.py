from collections import deque

n = int(input())
word_list = []
for _ in range(n) :
    word = list(input())
    word_list.append(word)

# 좋은 단어 : 단어 위로 아치형 곡선을 그어 같은 글짜끼리 쌍을 지을 때 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝지을 수 있으면 좋은 단어
# 예) A B B A 가 있으면
#       └┛  가 좋은 단어
#    └     ┛가 좋은 단어가 되는거다

cnt = 0
for w in word_list :
    stack = deque()
    for char in w:
        # 스택이 비어있다면, 현재 문자를 스택에 추가합니다.
        if len(stack) == 0:
            stack.append(char)
        else:
            # 스택의 마지막 문자와 현재 문자가 같다면, 스택에서 마지막 문자를 제거합니다.
            if stack[-1] == char:
                stack.pop()
            else:
                # 스택의 마지막 문자와 현재 문자가 다르다면, 현재 문자를 스택에 추가합니다.
                stack.append(char)
    # 스택이 비어있다면, 좋은 단어이므로 개수를 증가시킵니다.
    if len(stack) == 0:
        cnt += 1
print(cnt)