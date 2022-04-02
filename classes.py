class Perro:
    def __init__(self,name, raza, color, size ):
        self.size= size
        self.age = 0
        self.color=color
        self.raza=raza
        self.name = name

    def ladrar(self):
        print("El perro esta ladrando")
    def check_hambre(self, hambre):
        if hambre:
            self.comer()
        else:
            print(f"{self.name} no tiene hambre")

    def comer(self):
        print("Esta comiendo")

    def jugar(self):
        print("El perro esta jugando")

    def change_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, age):
        self.age=age
        print("la de edad de {} es {}".format(self.name, self.age))
    def adittion_year(self):
        self.age += 1
my_perro= Perro("abran", "chiguaba", "ramon", "12")
print(my_perro.name)
my_perro.jugar()
my_perro.check_hambre(True)
my_perro.change_nombre("Lucas")
my_perro.set_edad(25)

print(my_perro.nombre)