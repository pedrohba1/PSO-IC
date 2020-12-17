import networkx as nx

graphname = 'C250-9.mtx'
file1 = open('grafos/{}'.format(graphname), 'r') 
Lines = file1.readlines()


G = nx.Graph()

for line in Lines:
    node = line.split()
    G.add_edge(node[0], node[1])


#subG = nx.subgraph(G)
# verificando se estamos no dataset correto (C1000.9)
print(nx.number_of_nodes(G))
print(nx.density(G))