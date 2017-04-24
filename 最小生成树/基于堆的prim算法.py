def heappop(Q,lenq):#出堆函数
   #print(Q)
   end=Q[0]
   Q[0],Q[-1]=Q[-1],Q[0]#交换Q出堆的值和最大值
   Q.pop()#Q的最小值出堆
   minheap(Q,0,lenq-1)#从头开始维持最小堆性质
   return end

def heappush(Q,uvw,lenq):#入堆函数
    Q.append(uvw)
    i=lenq-1#当前i的位置
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
    #lenq=lenq
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
    minheap(Q, minest,lenq)
    return Q

def prim(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    n=len(G)
    lenp=0
    lenq=1
    while lenp<n:
        _, p, u = heappop(Q,lenq)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        lenq-=1
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        lenp+=1
        for v, w in G[u].items():#对每一个u的邻接节点
            heappush(Q, (w, u, v),lenq)  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
            lenq+=1
    return P#返回最小生成树

#测试
G = {
    0: {1: 1, 2: 3, 3: 4},
    1: {0: 1, 2: 5},
    2: {0: 3, 1: 5, 3: 2},
    3: {2: 2, 0: 4}
}

print(prim(G, 0))  # {0: None, 1: 0, 2: 0, 3: 2}
