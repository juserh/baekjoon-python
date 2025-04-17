# #Q15439
# import sys
# n = int(sys.stdin.readline())
# print(n*(n-1))

# #Q24723
# import sys
# n = int(sys.stdin.readline())
# print(2**n)

#Q10872
import sys
n = int(sys.stdin.readline())
result = 1

for i in range(2, n+1) :
    result *= i
print(result)