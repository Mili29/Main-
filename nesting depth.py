t=int(input())
temp=1
for i in range(1,t+1):
    str=input()
    n=len(str)
    out=" "
    l=0
    val=0
    for i in range(0,n):
        if(i==0):
            for j in range(0,int(str[i])):
                out=out+"("
                l=l+1
            out=out+str[i]
        else:
            val=int(str[i-1])-int(str[i])
            if(val==0):
                out=out+str[i]
            elif(val>0):
                for j in range(0,val):
                    out=out+')'
                    l=l-1
                out=out+str[i]
            else:
                for j in range(0,abs(val)):
                    out=out+'('
                    l=l+1
                out=out+str[i]
    if(l>0):
        for m in range(0,1):
            out=out+')'
            
    print("Case #{0}:{1}".format(temp,out))
    temp=temp+1