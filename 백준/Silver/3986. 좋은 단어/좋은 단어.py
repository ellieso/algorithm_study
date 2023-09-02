from collections import deque

n = int(input())
word_list = []
for _ in range(n):
    word = list(input())
    word_list.append(word)

cnt = 0
for w in word_list:
    stack = deque()
    for char in w:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    
    if len(stack) == 0:
        cnt += 1

print(cnt)