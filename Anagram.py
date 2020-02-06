n=int(input())
for i in range(n):
    s1,s2=input().split(" ")
    s1=set(s1)
    s2=set(s2)
    if(s1==s2):
        print("YES")
    else:
        print("NO")
    
