list = [['T','X','A','A','X','X'], ['X','X','X','A','A','X'], ['A','X','X','X','X','X'], ['A','X','X','X','A','A'], ['A','A','A','X','T','A'], ['A','X','A','A','A','X'], ['X','X','X','X','X','X']]

class node():
    def __init__(self, id, line, pos, index) -> None:
        self.id = id
        self.line = line
        self.pos = pos
        self.index = index
        self.adjacentes = []
        pass

    def add_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    

class adjacente():
    def __init__(self, pos):
        self.pos = pos
        

# Identificar por que caralhos n ta ciclando #
def contamina(nd):
    for i in nd.adjacentes:
        if nd.id == "T" and nodes[i].id == "A":
            nodes[i].id = "T"
            contamina(nodes[i])
        elif nd.id == "A" and nodes[i].id == "T":
            nodes[i].id = "T"
            contamina(nd)
        elif nd.id == "X":
            contamina(nodes[nd.index+1])
    
nodes = []

for l in range(len(list)):
    act_line = list[l]
    for p in range(len(act_line)):
        nd = node(id=act_line[p], line=l, pos=p, index=len(nodes)-1)
        nodes.append(nd)

## Só adicionar quando existe.
for i in nodes:
    try:
        i.add_adjacente(i.index+1)
    except:pass
    try:
        i.add_adjacente(i.index-1)
    except:pass
    try:
        i.add_adjacente(i.index+6)
    except:pass
    try:
        i.add_adjacente(i.index-6)
    except:pass

contamina(nodes[0])


# Fazer print certinho #
for i in nodes:
    print(i.id, end=": ")
    for i in i.adjacentes:
        print(nodes[i].id, end=", ")
    print("")
        
        
