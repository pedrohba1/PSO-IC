import math
from makeGraph import *
from aidfunctions import *


def sigmoid(x):
  return 1 / (1 + math.exp(-x))


def calcFitness(x):
    return x**4

# 100 partículas
# 100 iterações
# c= número real aleatório
# c1 =[0,4]
# c2 4-c1


iterations = 100 # quantidade de iterações 
v = []

# preencher a primeira vez o vetor v com as parículas 


# iterações:
totaliter = 10


v.append(generateParticle(G))
v.append([])

# calcular as velocidades iniciais:
for particle in v[0]:
    velocity = 0.1 * particle['cliqueLen']
    particle['velocity'] = velocity
    particle['position'] = particle['cliqueLen'] + velocity

gBest = 0
lBest = 0 
maxCliqueSize = 0

i=0 
while (i< totaliter):
    
    # encontrar os melhores valores nas iterações
    for particle in list(v[i]):
        if particle['position'] > lBest:
            lBest = particle['position']
        if particle['position'] > gBest:
            gBest = particle['position'] 
            maxCliqueSize = particle['cliqueLen']

    # atualizar as velocidades de cada partícula e suas respectivas posições, Além de calcular o fitness de cada uma
    for particle in list(v[i]):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        c1 = 2
        c2 = 4 -c1
        particle['velocity'] = r1*c1*(lBest - particle['velocity']) + r2*c2*(gBest - particle['velocity'])
        particle['position'] = particle['position'] + particle['velocity']
        particle['fitness'] = calcFitness(particle['position'])
    


    
    sortByfit = sorted(v[i], key=lambda k: k['fitness'])

    # vou gerar cliques aleatórios a partir dos que possuírem mais nós
    rnodes = []
    rsize = random.randint(0,15)
    for particle in sortByfit[:rsize]:
        if particle['nodes']:
            for node in list(particle['nodes']):
                rnodes.append(node)    

    v.append(generateParticleFromNodes(G,rnodes))
    # a ideia é pegar os nós que tiverem cliques, pois eles provavelmente terão cliques maiores
    for particle in v[i+1]:
        velocity = 0.1 * particle['cliqueLen']
        particle['velocity'] = velocity
        particle['position'] = particle['cliqueLen'] + velocity
    print(gBest)
    print(maxCliqueSize)

    i+=1


    # aplicar a função de fitness nas minhas partículas
    # a função de fitness tem que ser maior quanto maior for o meu clique
    # 
    # máximo global




    # atualizar velocidade e posição das partículas



