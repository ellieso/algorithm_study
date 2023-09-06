import sys
import math

n = int(sys.stdin.readline().rstrip())

# 나무들 모아
tree = []
for _ in range(n) :
    tree.append(int(sys.stdin.readline().rstrip()))
tree.sort()

# 간격 모아 모아 
interval_lis = []
for t in range(1,n) :
        interval_lis.append(tree[t]-tree[t-1])
        
# 이 간격들의 최대공약수
gcdd = interval_lis[0]
for n in range(len(interval_lis)) :
    gcdd = math.gcd(interval_lis[n], gcdd)
# print(gcdd)
# 필요한 나무의 갯수 =
# 전체 나무 갯수(간격으로 했을시) - 기존 주어진나무갯수

total_tree_num = (tree[-1]-tree[0])//gcdd+1
print(total_tree_num-len(tree))