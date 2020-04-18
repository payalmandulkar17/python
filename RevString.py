#s= "payal.a.good.girl"
n=(int)(input())
list=[]
for i in range(n):
    print("enter string")
    list.append(input())
    s=list[i]
    s=s.split(".")
    print(s)
    str=""
    dot="."
    for i in s:
       str=i+"."+str
    print(str[0:len(str)-1])
    
