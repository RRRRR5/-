#coding='utf-8'
#利用优先级队列heapq实现prim算法
from heapq import heappop, heappush#导入优先级队列

def prim(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    while Q:#当Q不为空
        _, p, u = heappop(Q)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] =p#将u:p存入P字典
        for v, w in G[u].items():#对每一个u的邻接节点
            heappush(Q, (w, u, v))  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
    return P#返回最小生成树
#测试
#邻接图
G = {
    0: {1: 1, 2: 3, 3: 4},
    1: {0: 1, 2: 5},
    2: {0: 3, 1: 5, 3: 2},
    3: {2: 2, 0: 4}
}
print(prim(G, 0))  # {0: None, 1: 0, 2: 0, 3: 2}
