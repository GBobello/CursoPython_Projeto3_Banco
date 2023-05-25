from models.cliente import Cliente
from models.conta import Conta

gabriel: Cliente = Cliente('Gabriel Bobello', 'bobello.gabriel@gmail.com', '071.683.699-89', '01/05/2003')
gbobello: Cliente = Cliente('Gabriel Luiz', 'bobello.sci@gmail.com', '071.683.699-89', '01/05/2003')

# print(gabriel)
# print(gbobello)

contag: Conta = Conta(gabriel)
contagb: Conta = Conta(gbobello)

# print(contag)
# print(contagb)

