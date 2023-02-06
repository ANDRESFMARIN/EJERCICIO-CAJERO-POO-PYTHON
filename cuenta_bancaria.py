class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print('Se ha depositado $',cantidad ,'de la cuenta. Nuevo saldo: $',self.saldo)

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            print('Se ha retirado $',cantidad ,'de la cuenta. Nuevo saldo: $',self.saldo)
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print('El saldo actual es de $', self.saldo)

cuenta = CuentaBancaria()

while True:
    accion = input("¿Qué desea hacer? (depositar, retirar, consultar saldo, salir): ")
    if accion == "depositar":
        cantidad = int(input("¿Cuánto desea depositar? "))
        cuenta.depositar(cantidad)
    elif accion == "retirar":
        cantidad = int(input("¿Cuánto desea retirar? "))
        cuenta.retirar(cantidad)
    elif accion == "consultar saldo":
        cuenta.consultar_saldo()
    elif accion == "salir":
        break
    else:
        print("Acción no válida.")



