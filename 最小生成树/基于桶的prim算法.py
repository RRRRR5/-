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


def prim(G, s):
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


#测试
G = {
    0: {1: 1, 2: 3, 3: 4},
    1: {0: 1, 2: 5},
    2: {0: 3, 1: 5, 3: 2},
    3: {2: 2, 0: 4}
}

print(prim(G, 0))  # {0: None, 1: 0, 2: 0, 3: 2}

