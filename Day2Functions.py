"""def myFun(x):
    x[0]=20
lst=[12,11,13,14,15]
myFun(lst)
lst[0]=100
print(lst)"""
"""def juice(n):               #sugarcane
        return n*50-((n*50*70)//100)
n=4
print(juice(n))"""
"""def juice(n):
        return n*50-((n*50*70)//100)
def tc():
    i=int(input())
    while(i!=0):
        i=i-1
tc() 
print(juice(int(input()))) """
"""def j(n):
     print(n*50 - ((n*50*70)//100))
def tc():
     i=int(input())
     while(i!=0):
          i=i-1
          n=int(input())
          j(n)
tc() """
#watching movie
"""def movie(x,y):
    print(y//2 + ( x-y))
def tc():
    i =int(input())
    while(i!=0):
        i=i-1
        x=int(input())
        y=int(input())
        movie(x,y)
tc()"""
"""def movie(x,y):         #with parameters without return type  
    print((x-y) + (y//2))
a,b=map(int,input().split())
movie(a,b) """
"""for i in range(int(input())):         #number of 4's
    n=int(input())
    c=0
    while(n>0):
        if (n%10==4):
            c=c+1
        n=n//10
    print(c) """
"""def four(n,c):
    if n==0:
        return c
    if(n%10)==4:
        c=c+1
    return four(n//10,c)
for i in range(int(input())):
    n=int(input())
    print(four(n,0)) """
"""n=int(input())              #recursive app-1
r=1
while n>0:
    r=r*n
    n=n-1
print(r)"""
"""n=int(input())   #recursive app-2
r=1
for i in range(1,n+1):
    r=r*i
print(r) """
"""def fact(n):          #recursive app 3
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))"""
##append three
n=int(input())
c=0
d=n
while d!=0:
    d=d//10
    c=c+1
n=(n*10)+3
n=n+(3*(10**(c+1)))
print(n)  


