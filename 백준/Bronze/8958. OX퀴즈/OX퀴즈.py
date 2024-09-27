import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    quiz = input().rstrip()

    count = 0
    score = 0    
    for i in quiz:
        if i  == "O":
            count = count + 1
        else:
            score = score + count * (count + 1) // 2
            count = 0
    if (count != 0):
        score = score + count * (count + 1) // 2
    print(score)
    
