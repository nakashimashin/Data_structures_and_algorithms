'''
Created on 2023/07/04

@author: Suguru Ueda
'''

WHITE = 0
GRAY = 1
BLACK = 2

class MyStack:

    def __init__(self, n):
        """サイズ n でスタックを初期化する．"""
        self.stack = [None] * n
        self.size = n
        self.top = -1     # トップの要素のインデックス番号

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def push(self, x):
        if self.top == self.size - 1:
            raise RuntimeError('スタック・オーバーフロー')
        else:
            self.top += 1
            self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise RuntimeError('スタック・アンダーフロー')
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    def __str__(self):
        return str([str(x) for x in self.stack[:self.top + 1]])
    
class MyQueue:
    def __init__(self,size):
        self.Q = [None]*size
        self.len = size
        self.head = 1
        self.tail = 1
        
    def enqueue(self,x):
        self.Q[self.tail-1] = x #
        if self.tail == len(self.Q):
            self.tail = 1
        else:
            self.tail = self.tail + 1
            
    def dequeue(self):
        x = self.Q[self.head-1] #
        if self.head == len(self.Q):
            self.head = 1
        else:
            self.head = self.head + 1
        return x
    
    def __str__(self):
        return str([str(x) for x in self.Q[self.head-1:self.tail -1]])

    
class MyVertex:
    
    def __init__(self, name):
        self.name = name
        # self.color = WHITE #
        # self.d = float('inf')
        
    def __str__(self):
        return str(self.name)
        
    
class MyGraph:
    
    def __init__(self, E):
        
        self.V = dict()     # 頂点の集合
        self.Adj = dict()   # 隣接リスト
    
        # 追加する辺毎に隣接リストを大きくしていくループ
        for e in E:
            # 辺の端点uとv (と重みw) を変数に代入する
            u, v = e
        
            # 頂点uがVに含まれていないときにVをuに追加し，uの空の隣接リストを作成する    
            if u not in self.V.keys():
                self.V[u] = MyVertex(u)
                self.Adj[self.V[u]] = []
        
            
            if v not in self.V.keys():
                self.V[v] = MyVertex(v)
                self.Adj[self.V[v]] = []
            
            # 頂点uの隣接リストの末尾に頂点vを追加する
            self.Adj[self.V[u]].append(self.V[v])
            self.Adj[self.V[v]].append(self.V[u])
        
        self.V = {v for v in self.V.values()}
        

def BFS(G, s):
    for u in G.V:
        if u!="s":
            u.color = WHITE
            u.d = float('inf')
    s.color = GRAY
    s.d = 0
    myqueue = MyQueue(100)
    myqueue.enqueue(s)
    while myqueue.head != myqueue.tail :
        u = myqueue.dequeue()
        for v in G.Adj[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                myqueue.enqueue(v)
        u.color = BLACK
    print("幅優先探索")
    for i in G.V:
        print(str(i.name)+":距離"+str(i.d))

    
    

def DFS(G, s):
    for u in G.V:
        if u!="s":
            u.color = WHITE
    s.color = GRAY
    mystack = MyStack(100)
    mystack.push(s)
    while mystack.top != -1:
        u = mystack.pop()
        for v in G.Adj[u]:
            if v.color == WHITE:
                v.color = GRAY
                mystack.push(v)
        u.color = BLACK
    print("深さ優先探索 白:0 灰色:1 黒:2")
    for i in G.V:
        print(str(i.name)+" 色"+str(i.color))

    

        
E = {('r', 's'), ('r', 'v'), ('s', 'w'), ('t', 'u'), ('t', 'w'), ('t', 'x'), ('u', 'x'), ('u', 'y'), ('w', 'x'), ('x', 'y')}
G = MyGraph(E)

for v in G.V:
    if v.name == 's':
        s = v
#幅優先探索
BFS(G,s)

#深さ優先探索
DFS(G,s)