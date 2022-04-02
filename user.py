class User:
    def __init__(self, email, username):
        self.email = email
        self.__password = "password"
        self.permissions = ['edit', 'create', 'update']
        self.username = username
        self.pago= True
    
    def set_name(self):
        self.username = input("introducir su nombre: ")
        print("Nombre colocado!!")
    
    def change_email(self):
        self.email = input("introducir su nuevo email: ")
        print("Email cambiado!!")
    

class UserPro(User):
   def __init__(self, email, username ):
        super().__init__(email, username)
        self.permissions +=['delete', 'download']
    

class UserManager(User):
    def __init__(self, email,username ):
        super().__init__(email, username)

    def pay_suscription(self):
        if self.pago:
            self.set_permissions(self.pago)
            print("Pagado con exito")
        else:
            print("pago no es con exitoso")

    def set_permissions(self, pago):
        if pago:
            user = UserPro(self.email, self.username)
            print("Usted si pago, sus permisos son {}".format(user.permissions))
        else:
            print("usted no a pagado")


user = UserManager('adxell', 'adxell')

user.pay_suscription()



