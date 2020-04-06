k=[]
r=[]
c=[]
t=int(input())
if(1<=t and t<=100):
    for i in range(t):
        x=[]
        trace=0
        coloumn=0
        row=0
        n=int(input())
        if(n>=2 and n<=100):
            for j in range(n):
                y=input().split(" ")
                a=[]
                for w in range(0,n):
                    a.append(int(y[w]))
                b=set(a)
                if len(b)!=n:
                    row+=1
                b.clear()
                x.append(a)
                
            for m in range(n):
                for n in range(n):
                    if(m==n):
                        trace=trace+x[m][n]
                        
            for m in range(n):
                hi=set()
                for i in range(n):
                    hi.add(x[i][m])
                if(len(hi)!=n):
                    coloumn+=1
                hi.clear()
                
        k.append(trace)
        r.append(row)
        c.append(coloumn)
        
        
for i in range(t):
    print("Case #{0}: {1} {2} {3}".format(i+1,k[i],r[i],c[i]))