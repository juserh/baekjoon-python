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

# #Q26069
# import sys
#
# n = int(sys.stdin.readline())
# dance = set(["ChongChong"])
#
# for _ in range(n) :
#     p1 , p2 = sys.stdin.readline().split()
#
#     if p1 in dance:
#         dance.add(p2)
#     elif p2 in dance :
#         dance.add(p1)
# print(len(dance))

# #Q2108
# import sys
#
# n = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(n)]
# arr = sorted(arr)
#
#
# #산술평균
# print(round(sum(arr)/n))
# #중앙값
# print(arr[n//2])
# #최빈값
# dic = dict()
# for a in arr :
#     if a in dic :
#         dic[a] += 1
#     else :
#         dic[a] = 1
# mx = max(dic.values())
# oft = []
#
# for a in dic :
#     if mx == dic[a] :
#         oft.append(a)
# if len(oft) == 1:
#     print(oft[0])
# else :
#     print(oft[1])
# #범위
# print(max(arr) - min(arr))

#Q20920
import sys

n, m = map(int, sys.stdin.readline().split())
dic = dict()

for _ in range(n) :
    word = sys.stdin.readline().rstrip()

    if len(word) >= m :
        if word in dic :
            dic[word] += 1
        else :
            dic[word] = 1

wordlist = sorted(dic.keys(), key = lambda word : (-dic[word], -len(word), word))
for word in wordlist :
    print(word)