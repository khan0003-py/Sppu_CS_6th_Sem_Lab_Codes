# --------------------------------------------------Astar-----------------------------------------------------------------------
from collections import deque
class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list=adjacency_list
    def get_neighbors(self, v):
        return self.adjacency_list[v]
    def h(self, n):
        H={
            'A':3,
            'B':4,
            'C':2,
            'D':6,
            'G':0,
            'S':5
        }
        return H[n]
    def a_star_algorithm(self,start_node,stop_node):
        open_list=set([start_node])
        closed_list=set([])
        g={}
        g[start_node]=0
        parents={}
        parents[start_node]=start_node
        while len(open_list)>0:
            n=None
            for v in open_list:
                if n==None or g[v]+self.h(v)<g[n]+self.h(n):
                    n=v;
            if n==None:
                print('path does not exist!')
                return None
            if n==stop_node:
                reconst_path=[]
                while parents[n]!=n:
                    reconst_path.append(n)
                    n=parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('path found:{}'.format(reconst_path))
                return reconst_path
            for(m,weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        print('path does not exist!')
        return None
adjacency_list={
    
    'A':[('B',2),('C',1)],
    'B':[('D',5)],
    'C':[('D',3),('G',4)],
    'D':[('G',2)],
    'S':[('A',1),('G',10)]
}
graph1=Graph(adjacency_list)
graph1.a_star_algorithm('S','G')

# --------------------------------------------------------------------8 puzzle ------------------------------------------------------------------

from copy import deepcopy
import numpy as np
import time
 
def bestsolution(state):
    bestsol = np.array([], int).reshape(-1, 9)
    count = len(state) - 1
    while count != -1:
        bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
        count = (state[count]['parent'])
    return bestsol.reshape(-1, 3, 3)
 
        
# checks for the uniqueness of the iteration(it).
def all(checkarray):
    set=[]
    for it in set:
        for checkarray in it:
            return 1
        else:
            return 0
 
 
# number of misplaced tiles
def misplaced_tiles(puzzle,goal):
    mscost = np.sum(puzzle != goal) - 1
    return mscost if mscost > 0 else 0
 
 
def coordinates(puzzle):
    pos = np.array(range(9))
    for p, q in enumerate(puzzle):
        pos[q] = p
    return pos
 
 
# start of 8 puzzle evaluvation, using Misplaced tiles heuristics
def evaluvate_misplaced(puzzle, goal):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])
 
    dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
 
    costg = coordinates(goal)
    # initializing the parent, gn and hn, where hn is misplaced_tiles  function call  
    parent = -1
    gn = 0
    hn = misplaced_tiles(coordinates(puzzle), costg)
    state = np.array([(puzzle, parent, gn, hn)], dtstate)
 
   #priority queues with position as keys and fn as value.
    dtpriority = [('position', int),('fn', int)]
 
    priority = np.array([(0, hn)], dtpriority)
     
    while 1:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])      
        position, fn = priority[0]       
        # sort priority queue using merge sort,the first element is picked for exploring.                                          
        priority = np.delete(priority, 0, 0)                         
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
          
        blank = int(np.where(puzzle == 0)[0])   
       
        gn = gn + 1                            
        c = 1
        start_time = time.time()
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                openstates = deepcopy(puzzle)         
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]
                
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():          
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" The 8 puzzle is unsolvable \n")
                        break
                     
                    hn = misplaced_tiles(coordinates(openstates), costg)
                    # generate and add new state in the list                    
                    q = np.array([(openstates, position, gn, hn)], dtstate)         
                    state = np.append(state, q, 0)
                    # f(n) is the sum of cost to reach node
                    fn = gn + hn                                        
                     
                    q = np.array([(len(state) - 1, fn)], dtpriority)
                    priority = np.append(priority, q, 0)
                     
                    if np.array_equal(openstates, goal):                      
                        print(' The 8 puzzle is solvable \n')
                        return state, len(priority)
                         
    return state, len(priority)
 
 
# initial state
puzzle = []
 
puzzle.append(2)
puzzle.append(8)
puzzle.append(3)
puzzle.append(1)
puzzle.append(6)
puzzle.append(4)
puzzle.append(7)
puzzle.append(0)
puzzle.append(5)
 
#goal state       
goal = []
 
goal.append(1)
goal.append(2)
goal.append(3)
goal.append(8)
goal.append(0)
goal.append(4)
goal.append(7)
goal.append(6)
goal.append(5)
 
 
state, visited = evaluvate_misplaced(puzzle, goal)
bestpath = bestsolution(state)
print(str(bestpath).replace('[', ' ').replace(']', ''))
totalmoves = len(bestpath) - 1
print('\nSteps to reach goal:',totalmoves)
visit = len(state) - visited
print('Total nodes visited: ',visit, "\n")