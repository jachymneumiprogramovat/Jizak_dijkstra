import queue
import json

que = queue.Queue()


class Vrchol:
    def __init__(self, id, sousedi):
        self.id = id
        self.sousedi = sousedi
        self.visited = False
        self.vzdalenost = 99999999
        self.cesta = []

configFile=open("config.json","r")
config = json.load(configFile)
nodes=[]

for key in config:
  nodes.append(Vrchol(key,[(int(klic),config[key][klic]) for klic in config[key]]))

que.put(prvni)
prvni.vzdalenost = 0
prvni.cesta = [1]
while que.qsize() > 0:
    prvek = que.get()
    prvek.visited = True
    for dvojice in prvek.sousedi:
        soused = nodes[dvojice[0] - 1]
        if not soused.visited:
            que.put(soused)
        if prvek.vzdalenost + dvojice[1] < soused.vzdalenost:
            soused.vzdalenost = prvek.vzdalenost + dvojice[1]
            soused.cesta = prvek.cesta + [soused.id]

