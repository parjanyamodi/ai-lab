from heapq import heappush,heappop
import copy

class node:
    def __init__(self,parent,mat,empty_tile_pos):
        self.parent=parent
        self.mat=mat
        self.empty_tile_pos=empty_tile_pos
        # self.level=level
        # self.cost=cost
        
        # def __lt__(self,nxt):
        #     return self.cost<nxt.cost
def printB(mat):
    for i in range(3):
        print(mat[i][0]+" "+mat[i][1]+" "mat[i][2])
        
        
mat=[[0,0,0],[0,0,0],[0,0,0]]
empsp=[-1,-1]
print("Enter the initial state")
for i in range(3):
    x=input()
    mat[i][0],mat[i][1],mat[i][2]=x.split()
    if(mat[i][0]==0):
        empsp[0]=i 
        empsp[1]=0
    if(mat[i][1]==0):
        empsp[0]=i 
        empsp[1]=1
    if(mat[i][2]==0):
        empsp[0]=i 
        empsp[1]=2
        
    
printB(mat)

root = node(None,mat,empsp)
final=[[1,2,3],[4,5,6],[7,8,0]]

newMat=copy.deepcopy(mat)

while(check)

# class priorityQueue:
#     def __init__(self):
#         self.heap=[]
        
#     def push(self,x):
#         heappush(self.heap,x)
    
#     def pop(self):
#         return heappop(self.heap)
#     def isEmpty(self):
#         if not self.heap:
#             return True
#         return False
        
        
