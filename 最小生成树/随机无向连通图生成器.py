import random
def judge(G):#判断图是否连通,连通返回0，不连通返回1
    unlist=[0]#队列
    uselist=[0]
    while unlist:
        top,*unlist=unlist#每次取队列首元素
        for v in G[top]:
            if v not in uselist:
                unlist.append(v)
                uselist.append(v)
    #print(uselist)
    if len(uselist)==len(G):
        return 0
    else:
        return 1

def Randomaddnode(G,nodelist):#随机加边
    ul=[u for u in G]
    i=0
    while i<3*len(G):
           #随机选取两个节点
           ui=random.choice(ul)
           vi=random.choice(ul)
           if ui==vi or (ui,vi) in nodelist:continue
           weight=random.randint(1,10)#产生1,10的权值
           G[ui][vi]=weight
           G[vi][ui]=weight
           nodelist.append((ui,vi))
           i+=1
           print(i)
    return G




#print(dijkstra(G,0))
n=2000#需要产生n个节点的连通图
G = {u:{} for u in range(n)}
nodelist=[]
Randomaddnode(G,nodelist)
while judge(G):
    Randomaddnode(G,nodelist)
print(G)