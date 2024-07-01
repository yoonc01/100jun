from collections import deque
import sys

N, L = map(int, input().split())

input_deq = deque(list(map(int, sys.stdin.readline().split())))
min_ = deque([])
min_list = []

for i in range(N):
    if min_ and min_[0][0] <= i - L:
        min_.popleft()
    
    new = (i, input_deq.popleft())
    
    while len(min_) >= 1 and new[1] < min_[-1][1]:
        min_.pop()
    
    min_.append(new)
    
    min_list.append(min_[0][1])
    

for i in range(N):
    print(min_list[i], end = " ")
    

        