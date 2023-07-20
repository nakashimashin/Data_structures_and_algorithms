'''
Created on 2023/07/06

@author: Suguru Ueda
'''

class MyVertex:
    '''
    グラフの頂点を保持するクラス
    
    Attributes
    ----------
    name : str
        頂点の名前
    '''
    
    def __init__(self, name):
        '''
        Parameters
        ----------
        name : str or int
            頂点の名前
        '''
        
        self.name = name
        
    def __str__(self):
        return str(self.name)

class MyWeightedDigraph:
    '''
    グラフを保持するクラス
    
    Attributes
    ----------
    V : set
        頂点の集合
    Adj : dict
        隣接リスト
    '''
    
    def __init__(self, E):
        '''
        Parameters
        ----------
        E : set of tuple
            辺の集合
        '''
        
        self.V = dict()     # 頂点の集合
        self.Adj = dict()   # 隣接リスト
    
        # 追加する辺毎に隣接リストを大きくしていくループ
        for e in E:
            # 辺の端点 u と v と重み w を変数に代入する (アンパック代入)
            u, v, w = e
        
            # 頂点 u が V に登録されていないとき，頂点 u を作成し，u の空の隣接リストを作成する    
            if u not in self.V.keys():
                self.V[u] = MyVertex(u)
                self.Adj[self.V[u]] = []
        
            # v についても同様
            if v not in self.V.keys():
                self.V[v] = MyVertex(v)
                self.Adj[self.V[v]] = []
            
            # 頂点 u の隣接リストの末尾に頂点 v と重み w を追加する
            self.Adj[self.V[u]].append({'vertex': self.V[v], 'weight': w})
        
        # V をdict型からset型に変換する (集合内包表記)
        self.V = {v for v in self.V.values()}
        
    def __str__(self):
        
        lines = ''
        
        for u in self.V:
            line = 'Adj[' + str(u.name) + ']: ['
            for v in self.Adj[u]:
                line += "{'vertex': " + str(v['vertex']) + ", 'weight': " + str(v['weight']) + "}, "
            
            line = line[:len(lines) - 2]
            line += ']'
            
            lines += line + '\n'
            
        lines = lines[:len(lines) - 1]
        
        return lines
        
def initialize_single_source(G, s):
    for v in G.V:
        v.d = float('inf')
        v.π = None
    s.d = 0
    
    '''
    最短路推定値と先行点の初期化
    
    Parameters
    ----------
    G : MyWeightedDigraph
        グラフ
    s : MyVertex
        始点
    '''
    
    
def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.π = u
    '''
    緩和
    
    Parameters
    ----------
    u : MyVertex
        有向辺(u,v)の始点
    v : MyVertex
        有向辺(u,v)の終点
    w : int
        有向辺(u,v)の重み
    '''
    

def dijkstra(G, s):
    initialize_single_source(G,s)
    S = [None]
    while len(G.V) != len(S):
        min = float('inf')
        for i in G.V:
            if min > i.d and (i.name not in S): #リストSにiの情報がはいっていなければ
                min = i.d
                u = i
        S.append(u.name) #先行・を格納
        for v in G.Adj[u]:
            relax(u,v['vertex'],v['weight'])
            
    for v in G.V:
        print(v.name,v.d,v.π)
    
    '''
    ダイクストラのアルゴリズムを用いて最短路を求める
    
    Parameters
    ----------
    G : MyWeightedDigraph
        グラフ
    s : MyVertex
        始点
    '''

E = {('s', 't', 10), ('s', 'y', 5), ('t', 'x', 1), ('t', 'y', 2), ('x', 'z', 4), ('y', 't', 3), ('y', 'x', 9), ('y', 'z', 2), ('z', 's', 7), ('z', 'x', 6)}

G = MyWeightedDigraph(E)

print(G)

for v in G.V:
    if v.name == 's':
        s = v
        
dijkstra(G, s)

