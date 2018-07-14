from Graph2 import Graph2, dijkstra, shortest

g = Graph2()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)  
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

print('Graph data:')
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

        
dijkstra(g, g.get_vertex('a')) 

target = g.get_vertex('e')
path = [target.get_id()]
shortest(target, path)
print('The shortest path : %s' %(path[::-1]))