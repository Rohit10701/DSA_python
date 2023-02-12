from cmath import inf


def dijsktra(graph,src,dst):
    visited=set()
    dist={}
    for ele in graph:
        dist[ele]=inf

    dist[src]=0
    
    for ele in graph:
        d=dist[ele]
        for n in graph[ele]:
            if n not in visited:
                dist[n]=min(dist[n],d+graph[ele][n])
        visited.add(ele)
    print(dist)
    return dist[dst]         
    


if __name__ == "__main__":

    graph={
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}

    }

    src='A'
    des='F'
    print(dijsktra(graph,src,des))