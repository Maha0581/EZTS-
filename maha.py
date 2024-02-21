#a,b=map(int,input().split())
#if(a>b):""" print(a)
#else:
   # print(b)
"""
a,b,c=map(int,input().split())
if(a>b and a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)
'''
#2nd largest app-1
a,b,c=map(int,input().split())
if(a>b and a>c):
    a=0
elif(b>c):
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif(b>c):
    print(b)
else:
    print(c)
#a=list(map(int,input().split()))
#a.sort()
#print(a[-2])
'''
#2nd largest app-2
"""
"""a,b,c=map(int,input().split())
if(a>b>c or c>b>a):
    print(b)
elif(b>a>c or c>a>b):
    print(a)
else:
    print(c)
    """
#print many hello world
#for i in range(0,1000):
  #  print("Hello World")
#print("hello\n"*10)
""" small,large,equal
a,b=map(int,input().split())
if(a==b):
    print("a == b")
elif(a<b):
    print("a < b")
else:
    print("a > b")
"""
#valid triangle
""" a,b,c=map(int,input().split())
if(a+b>c and b+c>a and c+a>b):
    print("valid")
else:
    print("not valid") """
#student and apples
"""n,k=map(int,input().split())
while(k>=n):
    k-=n
print(k)"""
#reverse of a number app-1
"""
a=int(input())
if a<0:
    t=-a
else:
    t=a
temp=0
while(t!=0):
    temp=temp*10 + t%10
    t//=10
if a>0:
    print(temp)
else:
    print(-temp)
"""
""" reverse of a num   app-2
n=int(input())
if n>0:
    r=0
    while(n>0):
        r1=n%10
        r=r*10 + r1
        n=n//10
    print(r)
elif n==0:
    print(n)
else:
    r=0
    n=n*-1
    while n>0:
        r1=n%10
        r=r*10 + r1
        n=n//10
    print(r*-1)
    """
#watermelon equally dividing and the divided part should be even
"""w=int(input())
if(w>2 and w%2==0):
    print("yes")
else:
    print("no")"""
#fever
"""
for i in range(int(input())):   #app 1
    n=int(input())
    if(n>98):
        print("yes")
    else:
        print("no")"""
"""t=int(input())  #app 2
while(t):
    n=int(input())
    if(n>98):
        print("yes")
    else:
        print("no")
    t=t-1
"""
""" discount
for i in range(int(input())):
    n=int(input())
    print(100-n)
"""
"""for i in range(int(input())):  #APP 2
    a,b,c,d=map(int,input().split())
    x=a-c
    y=b-d
    if(x==y):
        print("any")
    elif(x>y):
        print("second")
    else:
        print("first")"""
"""  app-1
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=a-((a*c)//100)
    y=b-((b*d)//100)
    if(x==y):
        print("any")
    elif(x>y):
        print("second")
    else:
        print("first")
"""
""" #chef and candy packets
for i in range(int(input())):
    n,x=map(int,input().split())
    if n>x:
        if((n-x)%4==0):
            print((n-x)//4)
        else:
            print(((n-x)//4)+1)
    else:
        print(0)
"""
 """ for i in range(int,input()):  #total pizzas
    n,x=map(int,input().split())
    if(x%4==0):
        print(n*(x//4))
    else:
        print((n*(x//4))+1)
"""

#t=int(input())
#for i in range(t):   #brute force approach
 #   n,x=map(int,input().split())
  #  ts=n*x
   # tp=0
 #   while ts>=4:
 #       tp=tp+1
 #       ts=ts-4
  #  if tp == 0:
 #       print(tp)
 #   else:
 #       print(tp+1)
