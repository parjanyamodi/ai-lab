import math
import numpy as np
s = [['#','#','#','#'],
['#','S','#','.'],
['.','.','#','.'],
['#','.','#','D']]
rows = len(s)
col = len(s[0])
visited_states =[]
def isDest(cur,dest):
    return cur==dest

def getH(cur,dest) :
    return math.sqrt((dest[1]-cur[1])**2+(dest[0]-cur[0])**2)

def gen_states(cur):
    cur_x=cur[0]
    cur_y=cur[1]
    states=[]
    if cur_x>0 and s[cur_x-1][cur_y]!='.' : states.append((cur_x-1,cur_y))
    if cur_y>0  and s[cur_x][cur_y-1]!='.' : states.append((cur_x,cur_y-1))
    if cur_x<rows-1  and s[cur_x+1][cur_y]!='.' : states.append((cur_x+1,cur_y))
    if cur_y<col-1  and s[cur_x][cur_y+1]!='.' : states.append((cur_x,cur_y+1))
    return states

def calF(cur,dest) :
    cur_x = cur[0]
    cur_y = cur[1]
    states = gen_states(cur)
    Min = float('inf')
    next_state=states[0]
    for t in states :
        if t == dest :
            return t
        f = 1 + getH(t,dest)
        if f < Min :
            Min = f
            next_state = t
    return next_state
    
def A_star(src,dest) :
    visited_states.append(src)
    if src == dest :
        print(src)
        print("Destination reached!")
        return
    print(src)
    next_state = calF(src,dest)
    if next_state not in visited_states :
        A_star(next_state,dest)
    
def maze(src):
    print(np.matrix(s))
    for i in range(rows):
        for j in range(col):
            if s[i][j] == 'S' :
                cur = (i,j)
            if s[i][j] == 'D' :
                dest = (i,j)
    A_star(cur,dest)
    
maze(s)    
    
