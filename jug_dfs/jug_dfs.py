src = (0,0)
visited_states =[]
def gen(cur) :
    states = []
    if cur[0]<3 :
        states.append((3,cur[1]))
        if cur[1]>0 :
            states.append((cur[0],0))
            rem=0
            if cur[1]>(3-cur[0]) :
                rem=3-cur[0]
            else :
                rem = cur[1]
            states.append((cur[0]+rem,cur[1]-rem))
    if cur[1]<4 :
        states.append((cur[0],4))
        if cur[0]>0 :
            states.append((0,cur[1]))
            rem=0
            if cur[0] >(4-cur[1]) :
                rem = 4-cur[1]
            else :
                rem = cur[0]
            states.append((cur[0]-rem,cur[1]+rem))
    return states        
def dfs(cur) :
    visited_states.append(cur)
    if cur[1] == 2 :
        print("Solution Found : ",cur)
        return
    print(cur)
    states = gen(cur)
    for state in states : 
        if state not in visited_states :
            dfs(state)
dfs(src)
