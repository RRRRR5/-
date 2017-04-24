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

def Randomaddnode(G):#随机加边
    ul=[u for u in G]
    nodelist=[]
    while judge(G):
           #随机选取两个节点
           ui=random.choice(ul)
           vi=random.choice(ul)
           if ui==vi:continue
           weight=random.randint(1,10)#产生1,10的权值
           if ui!=vi and (ui,vi) not in nodelist:#ui和vi不相等并且没有加过边
               G[ui][vi]=weight
               G[vi][ui]=weight
               nodelist.append((ui,vi))
    return G

def heappop2(Q):#出堆函数
   #print(Q)
   end=Q[0]
   #print(Q)
   Q[0],Q[-1]=Q[-1],Q[0]#交换Q出堆的值和最大值
   Q.pop()#Q的最小值出堆
   #print(Q)
   minheap(Q,0)#从头开始维持最小堆性质
   return end

def heappush2(Q,uvw):#入堆函数
    Q.append(uvw)
    i=len(Q)-1#当前i的位置
    while i>0 and Q[int((i-1)/2)][0]>Q[i][0]:
        Q[int((i-1)/2)],Q[i]=Q[i],Q[int((i-1)/2)]#交换该节点与母节点位置
        i=int((i-1)/2)
#维持堆的性质
def minheap(Q,i):
    # 找出i的左右子树
    l = 2 * i + 1
    r = 2 * i + 2
    # 找出左右子树中的最小值并判断是否与i交换
    # 判断左子树与i节点的大小
    lenq=len(Q)
    if l < lenq and Q[l][0] < Q[i][0]:#如果左子树存在并小于i的值
        minest = l#最小节点记为左子树
    else:
        minest = i#否则最小节点记为i
    if r < lenq and Q[r][0] < Q[minest][0]:  # 如果右子树最小
        minest = r
    if minest == i:#如果已经最小，则直接返回Q
        return Q
    else:
        # 将i与最小值交换位置
        Q[i], Q[minest] = Q[minest], Q[i]
    # 递归的维持
    minheap(Q, minest)
    return Q

def prim(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    n=len(G)
    lenp=0
    #lenq=1
    while lenp<n:
        _, p, u = heappop2(Q)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        #lenq-=1
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        lenp+=1
        for v, w in G[u].items():#对每一个u的邻接节点
            heappush2(Q, (w, u, v))  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
            #lenq+=1
    return P#返回最小生成树


from heapq import heappop, heappush#导入优先级队列

def prim2(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    while Q:#当Q不为空
        _, p, u = heappop(Q)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        for v, w in G[u].items():#对每一个u的邻接节点
            heappush(Q, (w, u, v))  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
    return P#返回最小生成树

#出桶函数
def bucketpop(Q):#i为当前指针位置
    i=0
    while Q[i]==[]:
           i=i+1
    top=Q[i][-1]    #Q[i]=(-1,None,None)
    #Q[i].remove(Q[i][0])
    Q[i].pop()
    return top

 #入桶函数
def bucketpush(Q,vuw):
    #print(vuw)
    i=vuw[0]%(len(Q))
    Q[i].append(vuw)
    return Q


def prim3(G, s):
    P= {}
    C = max([G[u][v] for u in G for v in G[u]])  # C为最大边长度
    Q={i:[] for i in range(C+1)}#P记录最小生成树，Q记录优先队列
    Q[0].append((0,None,s))
    n=len(G)
    lenp=0

    while lenp<n:
        _, p, u = bucketpop(Q)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        #print(Q)
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        lenp+=1
        for v, w in G[u].items():#对每一个u的邻接节点
            bucketpush(Q, (w, u, v))  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
            #print(Q)

    return P#返回最小生成树

def find(C,u):#查找u节点所在集合的头节点
    if C[u]!=u:
       u=find(C,C[u])
    return u

def union(C,S,u,v):#将u,v划入一个集合，即将两个集合的头节点合并为一个头节点
    u=find(C,u)#u的头节点
    v=find(C,v)#v的头节点
    if S[u]>S[v]:
        C[v]=u#将u设为v的头节点
    else:
        C[u]=v#将v设为u的头节点
    if S[u]==S[v]:#如果两个集合的大小相同
        S[v]+=1#集合大小加一

def kruskal(G):
    E=[(G[u][v],u,v) for u in G for v in G[u] if u>v]#找出所有权值
    T=[]#空集合用于存树
    C={u:u for u in G}#每个点一个集合
    S={u:1 for u in G}#每个集合的大小
    for _,u,v in sorted(E):#每次选取权值最小的边
        #print(u,v)
        if  find(C,u)!=find(C,v):#如果u和v不在一个集合
            T.append((_,u,v))
            union(C,S,u,v)#将两个点合并到一个集合
    return  T

#print(dijkstra(G,0))
n=10#需要产生n个节点的连通图
G = {u:{} for u in range(n)}
print(Randomaddnode(G))
#基于堆实现
print(prim(G,0))
#基于heap中的堆实现
print(prim2(G,0))
#基于桶实现
print(prim3(G,0))
#基于uion-find实现
print(kruskal(G))