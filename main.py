import queue

que = queue.Queue()


class Vrchol:
    def __init__(self, id, sousedi):
        self.id = id
        self.sousedi = sousedi
        self.visited = False
        self.vzdalenost = 99999999
        self.cesta = []


prvni = Vrchol(1, [(2, 3)])
druhy = Vrchol(2, [(1, 3), (4, 1), (5, 3)])
ctvrty = Vrchol(4, [(2, 1), (5, 1)])
paty = Vrchol(5, [(4, 1), (2, 3)])
treti = Vrchol(3, [(1, 100), (2, 200), (4, 400), (5, 500)])

vrcholi = [prvni, druhy, treti, ctvrty, paty]
que.put(prvni)
prvni.vzdalenost = 0
prvni.cesta = [1]
while que.qsize() > 0:
    prvek = que.get()
    prvek.visited = True
    for dvojice in prvek.sousedi:
        soused = vrcholi[dvojice[0] - 1]
        if not soused.visited:
            que.put(soused)
        if prvek.vzdalenost + dvojice[1] < soused.vzdalenost:
            soused.vzdalenost = prvek.vzdalenost + dvojice[1]
            soused.cesta = prvek.cesta + [soused.id]
print(vrcholi[4].vzdalenost, vrcholi[4].cesta)
