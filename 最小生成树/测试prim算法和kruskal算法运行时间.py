#自己写堆实现prim
import random
import time
#产生随机无向连通图
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
    while i<=3*len(G):
           #随机选取两个节点
           ui=random.choice(ul)
           vi=random.choice(ul)
           weight=random.randint(1,10)#产生1,10的权值
           if ui!=vi and (ui,vi) not in nodelist:#ui和vi不相等并且没有加过边
               G[ui][vi]=weight
               G[vi][ui]=weight
               nodelist.append((ui,vi))
           i+=1
           print(i)
    return G,nodelist


def heappop2(Q,lenq):#出堆函数
   #print(Q)
   end=Q[0]
   Q[0],Q[-1]=Q[-1],Q[0]#交换Q出堆的值和最大值
   #Q.remove(Q[-1])#Q的最小值出堆
   Q.pop()
   minheap(Q,0,lenq-1)#从头开始维持最小堆性质
   return end

def heappush2(Q,uvw,lenq):#入堆函数
    Q.append(uvw)#消耗时间

    i=lenq#当前i的位置
    while i>0 and Q[int((i-1)/2)][0]>Q[i][0]:
        Q[int((i-1)/2)],Q[i]=Q[i],Q[int((i-1)/2)]#交换该节点与母节点位置
        i=int((i-1)/2)
#维持堆的性质
def minheap(Q,i,lenq):
    # 找出i的左右子树
    l = 2 * i + 1
    r = 2 * i + 2
    # 找出左右子树中的最小值并判断是否与i交换
    # 判断左子树与i节点的大小
    lenQ=lenq
    if l < lenQ and Q[l][0] < Q[i][0]:#如果左子树存在并小于i的值
        minest = l#最小节点记为左子树
    else:
        minest = i#否则最小节点记为i
    if r < lenQ and Q[r][0] < Q[minest][0]:  # 如果右子树最小
        minest = r
    if minest == i:#如果已经最小，则直接返回Q
        return Q
    else:
        # 将i与最小值交换位置
        Q[i], Q[minest] = Q[minest], Q[i]
    # 递归的维持
    minheap(Q, minest,lenq)
    return Q

def prim(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    n=len(G)
    lenp=0
    lenq=1
    while lenp<n:#当节点并未全部上树
        _, p, u = heappop2(Q,lenq)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        lenq-=1
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        lenp+=1
        for v, w in G[u].items():#对每一个u的邻接节点
            heappush2(Q, (w, u, v),lenq)  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
            lenq+=1
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
            T.append((u,v))
            union(C,S,u,v)#将两个点合并到一个集合
    return  T


from heapq import heappop, heappush#导入优先级队列

def prim2(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    lenp=0
    n=len(G)
    while lenp<n:#当
        _, p, u = heappop(Q)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        lenp+=1
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


#last记录运行时间
def compare():
    last1=0

    last2=0
    G = {u: {} for u in range(2000)}  # 图的节点数
    nodelist = []
    Randomaddnode(G,nodelist)

    while judge(G):
        Randomaddnode(G,nodelist)

    for i in range(100):#同一个图求解次数
        print(i)
        stime1=time.clock()
        prim3(G, 0)
        endtime1=time.clock()
        last1=last1+endtime1-stime1

        stime2=time.clock()
        kruskal(G)
        endtime2=time.clock()
        last2=last2+endtime2-stime2
    #print(time.clock()-stime2)
    print(last1)

    print(last2)


compare()
