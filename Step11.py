#Q24262
print(1) #수행시간 O(1)
print(0)

#Q24263
n = int(input())
print(n) #수행시간 O(n)
print(1)

#Q24264
n = int(input())
print(n**2) #수행시간 O(n**2)
print(2)

#Q24265
n = int(input())
print(n*(n-1)//2) #수행시간 n*(n-1)/2 -> O(n**2)
print(2)

#Q24266
n = int(input())
print(n**3) #수행시간 O(n**3)
print(3)

#Q24267
n = int(input())
print(n*(n-1)*(n-2)//6) #수행시간 O(n**3)
print(3)

#Q24313
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
if (a1*n0+a0 <= c*n0) and (a1<=c) :
    print(1)
else :
    print(0)
