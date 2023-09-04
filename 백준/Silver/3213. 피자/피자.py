# 상근이의 친구들은 매우 어려서 피자 한 판을 먹을 수 없음
# 각 친구들은 자신의 먹을 수 있는 피자의 양을 알고 있음 --> 1/4, 1/2, 3/4 중 하나
# 상근이는 피자 최소 몇 판을 시키면 친구들이 모두 피자를 자신이 먹을 수 있는 양만큼 먹을 수 있는지 구하는 프로그램을 작성
# 상근이는 피자를 먹지 않으며 모든 친구들이 정확히 한 조각씩 피자를 가져가야 함.
import sys
input = sys.stdin.readline

n = int(input())
arr = []
pizza1 = []
pizza2 = []
pizza3 = []
cnt = 0
for _ in range(n):
    arr.append(input().strip())

# 친구들이 먹을 수 있는 피자 양에 따른 각각의 리스트를 만들어줌 
for i in range(n): 
  if arr[i][2] == '2':
      pizza1.append(arr[i])
  elif arr[i][2] == '4' and arr[i][0] == '1':
      pizza2.append(arr[i])
  else:
      pizza3.append(arr[i])

# 1/4과 3/4은 피자 한 판으로 먹을 수 있음 
while pizza2 and pizza3:
    pizza2.pop()
    pizza3.pop()
    cnt +=1 
    
# 1/2 하나와 1/4 2개 또한 피자 한 판으로 가능
while pizza1 and pizza2:
  pizza2.pop()
  if not pizza2:
    pizza1.pop()
    cnt +=1 
    break
  pizza2.pop()
  pizza1.pop()
  cnt += 1

# 각각의 피자 양을 처리해줌 
while pizza1:
   pizza1.pop()
   if not pizza1:
      cnt += 1
      break
   pizza1.pop()
   cnt += 1

while pizza2:
   pizza2.pop()
   cnt += 1

while pizza3:
   pizza3.pop()
   cnt += 1


print(cnt)