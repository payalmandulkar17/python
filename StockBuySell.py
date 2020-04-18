T=int(input())
def profit(c,days):
    profit=0
    y=0
    buyday=0
    sellday=0
    for i in range(days):
        profit=c[i]-c[buyday]
        if profit<0:
            y=y+1
        if y==1:
            buyday=i-1
        if y==2:        
            sellday=i-1
            print(buyday,",",sellday)
            buyday=i    
    print("i is",i)           
    if i==(days-1):
        sellday=i
        print(buyday,',',sellday)     
              
            

    

for i in range(T): 
    days=int(input())
    c=list(map(int,input().rstrip().split()))
    profit(c,days)
    

