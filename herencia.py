class Animal: 
    def __init__(self):
        self.edad = None
        self.especie = None
        self.pelaje = None
    
    def comer(self):
        print("El animal esta comiendo")
        
    def reproducirse(self):
        print("El animal se esta reproduciendo")

class Perro(Animal):
    def __init__(self):
        super().__init__()
        self.size=None
        self.raza=None
        self.nombre=None

    def ladrar(self):
        print("{} esta ladrando".format(self.nombre))
   
    def jugando(self):
        print("{} esta jugando".format(self.nombre))

tommy = Perro()
tommy.reproducirse()
print(tommy.edad)