import networkx as nx
import matplotlib.pyplot as plt

#查找函数
def find(C,u):#查找u节点所在集合的头节点
    if C[u]!=u:
       u=find(C,C[u])
    return u

#集合函数
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
    E=[(G[u][v],u,v) for u in G for v in G[u]]#找出所有权值
    T=set()#空集合用于存树
    C={u:u for u in G}#每个点一个集合
    S={u:1 for u in G}#每个集合的大小
    for _,u,v in sorted(E):#每次选取权值最小的边
        if  find(C,u)!=find(C,v):#如果u和v不在一个集合
            T.add((u,v,_))#将该边加入到生成树上（母节点，子节点，权值）
            union(C,S,u,v)#将两个点合并到一个集合
    return  T

#画图函数
def drawG(G):
    edgeslist1=list([(u,v,G[u][v]) for u in G for v in G[u] if u>v])
    edgeslist2=list(kruskal(G))
    edgeslist1=list(set(edgeslist1)-set(edgeslist2))+edgeslist2
    G1=nx.Graph()
    ulist=[u for u in range(len(G))]
    pos=nx.spring_layout(G1)
    G1.add_nodes_from(ulist)
    G1.add_weighted_edges_from(edgeslist1)
    colors=['k']*(len(edgeslist1)-len(edgeslist2))+['b']*(len(edgeslist2))
    #nx.draw_networkx_edges(G1,pos=nx.spring_layout(G1),edgelist=edgeslist1,edge_color=colors)
    nx.draw_networkx(G1,pos=nx.spring_layout(G1),nodelist=ulist,edgelist=edgeslist1,edge_color=colors,width=3,node_size=700)
    plt.axis('off')
    #plt.show()
    plt.savefig('kruskal.png')
    plt.show()

#连通图
G = {
    0: {1: 1, 2: 3, 3: 4},
    1: {0: 1, 2: 5},
    2: {0: 3, 1: 5, 3: 2},
    3: {2: 2, 0: 4}
}

drawG(G)


