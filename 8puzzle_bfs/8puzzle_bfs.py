src=[1,2,3,-1,4,5,6,7,8]
dest=[-1, 1, 3, 6, 2, 5, 7, 4, 8]
vis=[]

def gen(moves,cur,idx) :
    states=[]
    for move in moves :
        state=cur[:]
        if move == 'U' : state[idx],state[idx-3] = state[idx-3],state[idx]
        if move == 'D' : state[idx],state[idx+3] = state[idx+3],state[idx]
        if move == 'L' : state[idx],state[idx-1] = state[idx-1],state[idx]
        if move == 'R' : state[idx],state[idx+1] = state[idx+1],state[idx]
        states.append(state)
    return states
def gen_next(cur) :
    states=[]
    moves=[]
    idx=cur.index(-1)
    if idx>2:moves.append('U')
    if idx<5:moves.append('D')
    if idx%3>0:moves.append('L')
    if idx%3<2:moves.append('R')
    return gen(moves,cur,idx)

def bfs(src,dest) :
    vis.append(src)
    queue=[]
    queue.append(src)
    while len(queue) > 0 :
        cur=queue.pop(0)
        print(cur)
        if cur == dest :
            print("Destination Found!")
            return
        next_states = gen_next(cur)
        for state in next_states :
            if state not in vis :
                queue.append(state)
                
    
bfs(src,dest)
