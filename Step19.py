# #Q27433
# import sys
# def factorial(num) :
#     if num <=1 :
#         return 1
#     return factorial(num-1)*num
#
# n = int(sys.stdin.readline())
# print(factorial(n))

#Q10870
import sys
def fibo(num) :
    if num <= 1 :
        return num
    return fibo(num-1) + fibo(num-2)

n = int(sys.stdin.readline())
print(fibo(n))