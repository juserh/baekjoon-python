#Q15649
import sys

def backtracking(li, num) :
    global m
    if len(li) == m :
        print(' '.join(map(str, li)))

    for i in range(1, num+1) :
        if i not in li :
            li.append(i)
            backtracking(li, num)
            li.pop()


n, m = map(int, sys.stdin.readline().split())
backtracking([], n)
