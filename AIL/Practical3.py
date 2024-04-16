# -------------------------#SeLectton Sort:----------------------
def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index], arr[i]
    return arr
a1=[20,10,5,7,9,13]
print(selection_sort(a1))

# -------------------#prims algorithm------------------
import heapq

def prim(graph, start):
    mst=[]
    visited=set([start])
    edges=[(cost,start,to) for to, cost in graph[start].items()] 
    heapq.heapify(edges)
    while edges :
        cost, frm, to =  heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm,to, cost))
            for to_next, cost2 in graph [to].items():
                if to_next not in visited:
                    heapq.heappush(edges,(cost2, to, to_next))
    return mst
graph={
    'A':{'B':2, 'C':3},
    'B':{'A':2, 'C':1, 'D':1},
    'C':{'A':3, 'B':1, 'D':4},
    'D':{'B':1, 'C':4}
}
print(prim(graph, 'A'))