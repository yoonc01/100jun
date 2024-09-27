import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    quiz = input().rstrip()
    cnt = 0
    score = 0
    for i in quiz:
        if i == "O":
            cnt = cnt + 1
            score = score + cnt
        else:
            cnt = 0
    print(score)