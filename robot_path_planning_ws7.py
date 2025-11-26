import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import heapq

def neighbors(node,rows,cols):
    x,y=node
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<rows and 0<=ny<cols:
            yield (nx,ny)

def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def a_star(grid,start,goal):
    rows,cols=grid.shape
    open_set=[]
    heapq.heappush(open_set,(0,start))
    came_from={}
    g_score={start:0}
    f_score={start:heuristic(start,goal)}
    while open_set:
        _,current = heapq.heappop(open_set)
        if current==goal:
            path=[]
            while current in came_from:
                path.append(current)
                current=came_from[current]
            path.append(start)
            return path[::-1]
        for nb in neighbors(current,rows,cols):
            if grid[nb]==1: continue
            tentative = g_score[current]+1
            if tentative < g_score.get(nb,1e9):
                came_from[nb]=current
                g_score[nb]=tentative
                f=tentative+heuristic(nb,goal)
                f_score[nb]=f
                heapq.heappush(open_set,(f,nb))
    return None

def main():
    r=int(input('rows: ')); c=int(input('cols: '))
    grid=np.zeros((r,c),dtype=int)
    k=int(input('num obstacles: '))
    for _ in range(k):
        x,y=map(int,input('obs x y: ').split())
        if 0<=x<r and 0<=y<c: grid[x,y]=1
    sx,sy=map(int,input('start x y: ').split())
    gx,gy=map(int,input('goal x y: ').split())
    start=(sx,sy); goal=(gx,gy)
    df = pd.DataFrame(grid)
    print(df)
    path = a_star(grid,start,goal)
    if path is None:
        print('No path')
        return
    print('path',path)
    fig,ax=plt.subplots()
    ax.imshow(grid,cmap='gray_r')
    px=[p[1] for p in path]; py=[p[0] for p in path]
    ax.plot(px,py,'ro-')
    ax.scatter([start[1]],[start[0]],c='green')
    ax.scatter([goal[1]],[goal[0]],c='blue')
    plt.show()

if __name__=='__main__':
    main()
