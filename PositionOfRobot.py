move="UDDLLRUUUDUURUDDUULLDRRRR" #(0,0) ->-1,-1
x,y=0,0
for i in range(len(move)):
    if move[i]=='D':
        x,y=x,y-1
        print(x,",",y)
    elif move[i]=='U':
        x,y=x,y+1
        print(x,",",y)
    elif move[i]=='L':
        x,y=x-1,y
        print(x,",",y)
    elif move[i]=='R':
        x,y=x+1,y
        print(x,",",y) 
                    
