from heapq import heappop, heappush#导入优先级队列
import networkx as nx
import matplotlib.pyplot as plt
def prim(G, s):
    P, Q = {}, [(0, None, s)]#P记录最小生成树，Q记录优先队列
    while Q:#当
        _, p, u = heappop(Q)#将Q优先队列中选出最小值及节点信息p为母节点，u为子节点
        if u in P: continue#如果u已经上树则不进行下面的操作
        P[u] = {p:_}#将u:p存入P字典
        for v, w in G[u].items():#对每一个u的邻接节点
            heappush(Q, (w, u, v))  # 将u的邻接节点以（权重，母节点,子节点）存入优先队列
    return P#返回最小生成树

#画图函数
def drawG(G):
    edgeslist1=list([(u,v) for u in G for v in G[u] if u>v])#所有边
    np=prim(G,0)#prim算法返回的字典
    nplist=[(u,v) for u in np for v in np[u] if v!=None]#最小生成树边
    edgeslist2=nplist
    #print(edgeslist2)
    edgeslist1=list(set(edgeslist1)-set(edgeslist2))+edgeslist2#将最小生成树边和其他边在所有边列表中分开
    G1=nx.Graph()#图
    ulist=[u for u in range(len(G))]#所有节点
    pos=nx.spring_layout(G1)#布局格式
    G1.add_nodes_from(ulist)#添加节点
    G1.add_edges_from(edgeslist1)#添加所有边
    colors=['k']*(len(edgeslist1)-len(edgeslist2))+['b']*(len(edgeslist2))#将最小生成树边和其他边标记不同颜色的列表
    #nx.draw_networkx_edges(G1,pos=nx.spring_layout(G1),edgelist=edgeslist1,edge_color=colors)
    nx.draw_networkx(G1,pos=nx.spring_layout(G1),nodelist=ulist,edgelist=edgeslist1,edge_color=colors,width=3,node_size=700)#画图
    plt.axis('off')#去掉坐标轴
    #plt.show()
    plt.savefig('prim.png')
    plt.show()#显示

#邻接图
G = {
    0: {1: 1, 2: 3, 3: 4},
    1: {0: 1, 2: 5},
    2: {0: 3, 1: 5, 3: 2},
    3: {2: 2, 0: 4}
}

drawG(G)