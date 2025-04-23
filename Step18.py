# #Q1037
# import sys
#
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# mx = max(arr)
# mn = min(arr)
# print(mx*mn)

#Q25192
import sys

n = int(sys.stdin.readline())
emoji = set()

cnt = 0
for _ in range(n) :
    chat = sys.stdin.readline().rstrip()

    if chat == "ENTER" :
        cnt += len(emoji)
        emoji.clear()
    else :
        emoji.add(chat)
cnt += len(emoji)
print(cnt)