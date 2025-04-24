# #Q1037
# import sys
#
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# mx = max(arr)
# mn = min(arr)
# print(mx*mn)

#Q25192
# import sys
#
# n = int(sys.stdin.readline())
# emoji = set()
#
# cnt = 0
# for _ in range(n) :
#     chat = sys.stdin.readline().rstrip()
#
#     if chat == "ENTER" :
#         cnt += len(emoji)
#         emoji.clear()
#     else :
#         emoji.add(chat)
# cnt += len(emoji)
# print(cnt)

#Q26069
import sys

n = int(sys.stdin.readline())
dance = set(["ChongChong"])

for _ in range(n) :
    p1 , p2 = sys.stdin.readline().split()

    if p1 in dance:
        dance.add(p2)
    elif p2 in dance :
        dance.add(p1)
print(len(dance))