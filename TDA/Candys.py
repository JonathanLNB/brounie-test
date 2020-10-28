class Candys:
    def __init__(self, ninos, dulces):
        self.ninos = ninos
        self.dulces = dulces
    
    def obtenerResultado(self):
        residuo = self.dulces % self.ninos
        if(residuo == 0):
            return self.dulces / self.ninos
        else:
            sobrantes = self.dulces - residuo
            totalxNino = sobrantes / self.ninos
            return totalxNino * self.ninos
