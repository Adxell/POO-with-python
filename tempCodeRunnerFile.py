class User:
    def __init__(self):
        self.email = input("introducir email: ")
        self.__password = input("Introducir password: ")
        self.permissions = ['edit', 'create', 'update']
        self.username = None
        self.pago= False
    
    def set_name(self):
        self.username = input("introducir su nombre: ")
        print("Nombre colocado!!")
    
    def change_email(self):
        self.email = input("introducir su nuevo email: ")
        print("Email cambiado!!")
    
    def pay_suscription(self):
        self.pago = True
        print("pago es exitoso")
    
class UserPro(User):
    def __init__(self):
        super().__init__()
        self.permissions +=['delete', 'download']
    

class UserManager(User):
    def __init__(self):
        super().__init__()
    
    def set_permissions(self):
        if self.pago:
            UserPro()
            print("Usted si pago, sus permisos son {}".format(self.permissions))
        else:
            print("usted no a pagado")

user = User().pay_suscription()
print(user)