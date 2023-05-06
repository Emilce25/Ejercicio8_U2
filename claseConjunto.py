class Conjunto:
    __elementos=""
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def __add__(self, otro_conjunto):
        elementos_union = self.elementos.union(otro_conjunto.elementos)
        return Conjunto(elementos_union)

    def __sub__(self, otro_conjunto):
        elementos_diferencia = self.elementos.difference(otro_conjunto.elementos)
        return Conjunto(elementos_diferencia)

    def __eq__(self, otro_conjunto):
        return self.elementos == otro_conjunto.elementos

    def __str__(self):
        return "{" + ", ".join(str(e) for e in sorted(self.elementos)) + "}"
