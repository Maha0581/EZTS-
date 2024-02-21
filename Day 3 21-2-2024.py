#LISTS
"""n=int(input())               # single duplicate value
l=list(map(int,input().split()))
for i in range(n):
    if l[i] in l[i+1:n]:
        print(l[i])
        break """
""" n=int(input())
a=list(map(int,input().split()))   # 2 pointer approach
a.sort()
for i in range(n):
    if a[i]==a[i+1]:
        print(a[i])
        break  """
"""n=int(input())
a=list(map(int,input().split()))   #approach
for i in a:
    c=a.count(i)
    if c>1:
        print(i)
        break """
#unique elements
"""n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if(a[i] not in a[i+1:n] and a[i] not in a[:i]):
        print(a[i])"""
"""n=int(input())
a=list(map(int,input().split()))
for i in a:
    if a.count(i)==1:
        print(i,end=" ")"""
#tuples
"""t=int(input())           #chef team
for _ in range(t):           #app-1
    n=int(input())
    c=0
    d=0
    for i in range(1,n+1):
        if(n%i==0):
            if(i%2==0):
                c=c+1
            else:
                d=d+1
    if(c==d):
        print("1")
    else:
        print("0")"""
"""t=int(input())
for _ in range(t):
    n=int(input())                       app-2
    c=[]
    d=[]
    for i in range(1,n+1):
        if(n%i==0):
            if(i%2==0):
                c.append(i)
            else:
                d.append(i)
    if(len(c)==len(d)):
        print("1")
    else:
        print("0") """
"""for _ in range(int(input())):
    n=int(input())
    f=[]                     app-3
    for i in range(1,n+1):
        if(n%i==0):
            f.append(i)
    a=[]
    b=[]
    for j in f:
        if(j%2==0):
            a.append(j)
        else:
            b.append(j)
    if(len(a)==len(b)):
        print(1)
    else:
        print(0)   """
"""t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))        #groceries cost
    b=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(a[i]>=x):
            c=c+b[i]
print(c) """
#prime number
"""n=int(input())
for i in range(2,n+1):
    if(n%i==0):
        print("not prime")
        break
    else:
        print("prime")
        break   """
"""n=int(input())
l=[]
for i in range(1,n+1):       #bruteforce app
    if n%i == 0:
        l.append(i)
if len(l)==2:
    print("prime")
else:
    print("not prime")  """
#Running comparision
"""n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=0
for i,j in zip(a,b):
    if i<=j*2 and i*2>=j:
        e=e+1
print(e)  """
"""n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
happy=0
for i in range(n):
    if a[i]<=b[i]*2 and a[i]*2>=b[i]:
        happy=happy+1
print(happy)    """
"""n=int(input())
for i in range(1,n+1):
    l=[]
    if(i%2==0):
        for j in range(1,i):
            if(i%j==0):
                l.append(j)
    if(sum(l)==i):
        print(i)"""
     
n=int(input())    
s=0                     #even perfect number in the range
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
    s=0


        
