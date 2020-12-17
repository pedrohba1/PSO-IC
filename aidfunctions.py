from makeGraph import *
import itertools
nx.write_graphml(G, 'grafo.graphml')
from random import sample 
import random


def is_subclique(G,nodelist):
    H = G.subgraph(nodelist)
    n = len(nodelist)
    return H.size() == n*(n-1)/2



# gerando um subgrafo à partir de u conjunto de nós:
subS = G.subgraph(['1','2','3','4','5', '6','20','120']).copy()

def generate_random_node_from_graph(G):
    return sample(list(G.nodes), random.randint(1,G.number_of_nodes()))
    
def generate_random_clique(G,nodes):
    subGj = G.subgraph(nodes).copy()
    
    while(not is_subclique(G,list(subGj.nodes))):
        degrees = []
        for node in list(subGj.nodes):
            degree = nx.degree(subGj, node)
            degrees.append(degree)
        minIndex = degrees.index(min(degrees))
        minNode = list(subGj.nodes)[minIndex]
        subGj.remove_node(minNode)
    
    return subGj
    
def generateParticleFromNodes(G,nodes):
    Vj = []
    for node in G.nodes:
        rnodes = sample(nodes, random.randint(0,len(nodes)) )
        clique = generate_random_clique(G, nodes)
        if node in clique.nodes:
            Vj.append({ 'vid': node, 'inClique': 1, 'cliqueLen': len(clique.nodes), 'nodes': clique.nodes})
        else:  
            Vj.append({'vid': node,'inClique': 0,'cliqueLen': 0, 'nodes': [] })
    return Vj
  
# gera uma swarm onde as partículas são cliques:
def generateParticle(G):
    #gerar vertice aleatório
    # gero um clique à partir de um número aleatório de nós    
    #para cada um dos meus vértices, checo se ele está no clique,
    Vj = []
    for node in G.nodes:
        rnodes = generate_random_node_from_graph(G)
        clique = generate_random_clique(G, rnodes)
        if node in clique.nodes:
            Vj.append({ 'vid': node, 'inClique': 1, 'cliqueLen': len(clique.nodes), 'nodes': clique.nodes})
        else:  
            Vj.append({'vid': node,'inClique': 0,'cliqueLen': 0, 'nodes': [] })
    return Vj



