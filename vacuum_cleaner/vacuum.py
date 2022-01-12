import random
import numpy as np
def display(room):
    print(np.matrix(room))

room = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
]
rows=len(room)
col=len(room[0])
tiles=rows*col
cost=0
print("1 : Dirty Tile  0 : Clean Tile")
display(room)

print("Enter initial position of the vacuum cleaner : ")
x=int(input())
y=int(input())


while y>1:
    if room[x-1][y-1] == 1 :
        print("Cleaning location ",(x,y))
        room[x-1][y-1]=0
    else :
        print("Location ",(x,y)," is already clean")
    y-=1
    cost+=1

while x>1 :
    if room[x-1][y-1] == 1 :
        print("Cleaning location ",(x,y))
        room[x-1][y-1]=0
    else :
        print("Location ",(x,y)," is already clean")
    x-=1
    cost+=1


vis_tiles=0
d=0
while vis_tiles != tiles :
    if room[x-1][y-1] == 1 :
        print("Cleaning location ",(x,y))
        room[x-1][y-1]=0
    else :
        print("Location ",(x,y)," is already clean")
    vis_tiles+=1
    if d == 0 :
        if y == col :
            if x<rows :
                x+=1
                d=1
        else :
            y+=1
    
    else :
        if y == 1 :
            if x<rows :
                x+=1
                d=0
            
        else :
            y-=1
    cost+=1
print("Total Cost(Distance travelled : )",cost)
