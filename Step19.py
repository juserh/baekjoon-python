#Q27433
import sys
def factorial(num) :
    if num <=1 :
        return 1
    return factorial(num-1)*num

n = int(sys.stdin.readline())
print(factorial(n))
