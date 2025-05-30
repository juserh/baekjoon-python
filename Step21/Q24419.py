import sys
sys.setrecursionlimit(10000)

def recursion(n) :
    global cnt_r
    li = [1, 1]
    for i in range(2, n) :
        li.append(li[i-1]+li[i-2])
    return li[n-1]

def dynamic(n) :
    return n-2

num = int(sys.stdin.readline())
cnt_r = recursion(num)
cnt_d = dynamic(num)
print(cnt_r, cnt_d)