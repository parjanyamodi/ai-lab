import random as rn
import time

arr =[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
p=['','']
ch=-1
x=-1
y=-1
occ=[]
def disp():
    for i in range(3) :
        print(arr[i][0]+' | '+arr[i][1]+' | '+arr[i][2])
        if(i!=2):
            print("--+---+--")
            
def insttt():
    p[0] =input("Enter name of player 1:")
    p[1] =input("Enter name of player 2:")
    print("Tossing a coin.....")
    time.sleep(2)
    if(rn.randint(0,2)==0):
        print(p[0]+" will start the game with 'X'\n"+p[1]+" gets 'O'")
        return 0
    else:
        print(p[1]+" will start the game with 'X'\n"+p[0]+" gets 'O'")
        return 1

def check():
	
    if(arr[0][1]==arr[0][0] and arr[0][0]==arr[0][2]):
        if(arr[0][1] !=' '): 
            return True
    if(arr[1][1]==arr[1][0] and arr[1][0]==arr[1][2]):
        if(arr[1][1] !=' '):
            return True
    if(arr[2][1]==arr[2][0] and arr[2][0]==arr[2][2]):
        if(arr[2][1] !=' '):
            return True
    if(arr[1][0]==arr[2][0] and arr[2][0]==arr[1][0]):
        if(arr[1][0] !=' '):
            return True
    if(arr[1][1]==arr[2][1] and arr[2][1]==arr[1][0]):
        if(arr[1][1] !=' '):
            return True
    if(arr[1][2]==arr[2][2] and arr[2][2]==arr[1][2]):
        if(arr[1][2] !=' '):
            return True
    if(arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2]):
        if(arr[0][0] !=' '):
            return True
    if(arr[2][0]==arr[1][1] and arr[1][1]==arr[0][2]):
        if(arr[2][0] !=' '):
            return True
    return False


ch=insttt()
fl=True
print(ch)
for i in range(9):
    
    heeh=input(p[ch]+"choose your coordinates:\n")    
    temp=heeh.split()
    print(temp)
    x=int(temp[0])
    y=int(temp[1])
    while ([x,y] in occ):
        print("Already filled try again")
        heeh=input(p[ch]+"choose your coordinates:\n")    
        temp=heeh.split()        
        x=int(temp[0])
        y=int(temp[1])
    
    occ.append([x,y])
    if(fl):
        arr[x][y]='X'
    else:
        arr[x][y]='O'
    fl= not fl
    ch=(ch+1)%2
    disp()
    if(check()):
        print(p[ch]+" wins the game!!!")
        break
