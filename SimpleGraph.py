"""
Graph impl
- add_vertex(vertex)
- remove_vertex(vertex)
- connect_vertex(a,b)
- disconnect_vertex(a,b)
"""
from Stack import Stack
from Queue import Queue
import time

class Vertex:
    def __init__(self,value):
        self.value = value
        self.hit = False
        self.parent = None
    
    def __eq__(self, other):
        return self.value == other
    
    def __repr__(self):
        return "%s"%self.value

class Graph():
    """
    Graph impl
    - add_vertex(vertex)
    - remove_vertex(vertex)
    - connect_vertex(a,b)
    - disconnect_vertex(a,b)
    """
    def __init__(self,size):
        self.max_vertex = size
        self.m_adjacency = [[0]*self.max_vertex]*self.max_vertex
        self.vertex = list()
        
    def connect(self, a, b):
        try:
            id1 = self.vertex.index(a)
            id2 = self.vertex.index(b)
            self.m_adjacency[id1][id2] = 1
            self.m_adjacency[id2][id1] = 1
        except:
            print("passing vertex not in list")
    
    def add_vertex(self, item):
        if len(self.vertex)<self.max_vertex:
            self.vertex.append(item)
            self.m_adjacency[self.vertex.index(item)] = [0]*self.max_vertex
            
    def remove_vertex(self,vert):
        try:
            id = self.vertex.index(vert)
            self.vertex.pop(id)
            for i in self.m_adjacency:
                i[id] = 0
        except:
            print("passing vertex not in list")
    
    def disconnect(self, a, b):
        try:
            id1 = self.vertex.index(a)
            id2 = self.vertex.index(b)
            self.m_adjacency[id1][id2] = 0
            self.m_adjacency[id2][id1] = 0
        except:
            print("passing vertex not in list")

    def find(self, a,b):
        def proc(v,path):
            if v != b and v not in path:
                resp = []
                id = self.vertex.index(v)
                for i in range(len(self.vertex)):
                    if self.m_adjacency[id][i] == 1:
                        res = proc(self.vertex[i],path+[v,])
                        if res != None:
                            if len(resp)>0 and len(resp)>len(res):
                                resp = res
                            elif len(resp) == 0:
                                resp = res
                if len(resp)>0:
                    return [v,]+resp
            elif v == b:
                return [v,]
            else:
                return None
            
        return proc(a,[])

    def find_with_Stack(self,a,b):
        self.clear_hits()
        stack = Stack()
        stack.push(a)
        x = self.vertex[self.vertex.index(a)]
        while stack.size()>0:
            temp_flag = False
            x.hit = True
            all = self.adj(x)
            if b in all:
                stack.push(b)
                return stack.stack
            for i in all:
                if i.hit == False and i not in stack.stack:
                    x = i
                    temp_flag = True
                    stack.push(x)
##                    print([x.value for x in stack.stack])
                    break
            if temp_flag == True:
                continue
            else:
                stack.pop()
                if stack.size()>0:
                    x = stack.peak()
        return []            
            
    def bfs_with_path(self,a,b):
        ################
        def get_path(x):
            result = [b,]
            while x != None:
                result.append(x)
                x = x.parent
            return result[::-1]
        ################
        if a == b:
            return True
        self.clear_hits()
        q = Queue()
        x = self.vertex[self.vertex.index(a)]
        x.hit = True
        while True:
            edges = [y for y in self.adj(x) if y.hit == False]
            if b in edges:
                return get_path(x)
            for i in edges:
              i.hit = True
              i.parent = x
              q.enqueue(i)                                
            if q.size()>0:
                x = q.dequeue()
            else:
                return False
                               
    def bfs(self,a,b):
        if a == b:
            return True
        self.clear_hits()
        q = Queue()
        x = self.vertex[self.vertex.index(a)]
        x.hit = True
        while True:
            edges = [y for y in self.adj(x) if y.hit == False]
            for i in edges:            
                i.hit = True
                q.enqueue(i)
            if q.size()>0:
                x = q.dequeue()
                if x == b:
                    return True
            else:
                return False
        
    def clear_hits(self):
        for i in self.vertex:
            i.hit = False
            i.parent = None
            
    def adj(self, v):
        try:
            id = self.vertex.index(v)
            all = []
            for i in range(len(self.vertex)):
                if self.m_adjacency[id][i] == 1:
                    all.append(self.vertex[i])
            return all
        except:
            return []
        
#######################################################
if __name__ == "__main__":            
    g = Graph(10)
    
##    10 станций
    g.add_vertex(Vertex("gor"))
    g.add_vertex(Vertex("nev"))
    g.add_vertex(Vertex("vas"))
    g.add_vertex(Vertex("vost"))
    g.add_vertex(Vertex("pnev"))
    g.add_vertex(Vertex("spas"))
    g.add_vertex(Vertex("dost"))
    g.add_vertex(Vertex("lig"))
    g.add_vertex(Vertex("tech"))
    g.add_vertex(Vertex("push"))
    
##    12 связей
    g.connect(Vertex("gor"),Vertex("nev"))
    g.connect(Vertex("nev"),Vertex("vas"))
    g.connect(Vertex("nev"),Vertex("vost"))
    g.connect(Vertex("nev"),Vertex("spas"))
    g.connect(Vertex("vost"),Vertex("dost"))
    g.connect(Vertex("vost"),Vertex("pnev"))
    g.connect(Vertex("pnev"),Vertex("lig"))
    g.connect(Vertex("lig"),Vertex("dost"))
    g.connect(Vertex("dost"),Vertex("spas"))
    g.connect(Vertex("dost"),Vertex("push"))
    g.connect(Vertex("spas"),Vertex("tech"))
    g.connect(Vertex("spas"),Vertex("push"))

    print("Два варианта: первый без, второй со стеком ")
##от горьковской к василеостровской
    print("\n##от горьковской к василеостровской")
    print(g.find(Vertex("gor"), Vertex("vas")))
    print(g.find_with_Stack(Vertex("gor"), Vertex("vas")))
    print(g.bfs_with_path(Vertex("gor"), Vertex("vas")))
    print(g.bfs(Vertex("gor"), Vertex("vas")))
  
##от горьковской к техноложке
    print("\n##от горьковской к техноложке")
    print(g.find(Vertex("gor"), Vertex("tech")))
    print(g.find_with_Stack(Vertex("gor"), Vertex("tech")))
    print(g.bfs_with_path(Vertex("gor"), Vertex("tech")))
    print(g.bfs(Vertex("gor"), Vertex("tech")))
##от восстания к пушкинской
    print("\n##от восстания к пушкинской")
    print(g.find(Vertex("vost"), Vertex("push")))
    print(g.find_with_Stack(Vertex("vost"), Vertex("push")))
    print(g.bfs_with_path(Vertex("vost"), Vertex("push")))
    print(g.bfs(Vertex("vost"), Vertex("push")))
##от восстания в другой город
    print("\n##от восстания в другой город")
    print(g.find(Vertex("vost"), Vertex("ньюйорк")))
    print(g.find_with_Stack(Vertex("vost"), Vertex("ньюйорк")))
    print(g.bfs_with_path(Vertex("vost"), Vertex("ньюйорк")))
    print(g.bfs(Vertex("vost"), Vertex("ньюйорк")))
  
    
def test():
    start = time.time()
    for i in range(10000):
        g.find(Vertex("gor"), Vertex("pnev"))
    end = time.time()
    print("test ended in {}".format(end-start))
    
    start = time.time()
    for i in range(10000):
        g.find_with_Stack(Vertex("gor"), Vertex("pnev"))
    end = time.time()
    print("test ended in {}".format(end-start))
    
    start = time.time()
    for i in range(10000):
        g.bfs(Vertex("gor"), Vertex("pnev"))
    end = time.time()
    print("test ended in {}".format(end-start))
    start = time.time()
    for i in range(10000):
        g.bfs_with_path(Vertex("gor"), Vertex("pnev"))
    end = time.time()
    print("test ended in {}".format(end-start))

test()
##test(g.find(Vertex("gor"), Vertex("pnev")))
