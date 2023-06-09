class Usuario:

    def __init__(self , name,apellido, email_address,signo,edad,balance_cuenta):
    	# los asignamos en consecuencia
        self.name = name
        self.apellido=apellido
        self.email = email_address
        self.signo = signo
        self.edad=edad
        self.balance_cuenta=balance_cuenta
    def hacer_depósito(self, amount):	
        self.balance_cuenta += amount 

carla = Usuario("Carla","Torres","Carla@gmail.com","Acuario",57,0 )

carla.hacer_depósito(1000000)  
carla.hacer_depósito(2000) 
print(f"El saldo de {carla.name} es {carla.balance_cuenta} ")


# carla2 = Usuario("felipe","Torres","Carla@gmail.com","Acuario",17)
# carla3 = Usuario("isabel","Torres","Carla@gmail.com","Acuario",60)
# carla4 = Usuario("elita","Torres","Carla@gmail.com","Acuario",36)
# carla5 = Usuario("alioska","Torres","Carla@gmail.com","Acuario",24)

carla.hacer_depósito(100)





# print(f"my nombre es {carla.name} y mi edad es de {carla.edad}" )
# print(f"my nombre es {carla2.name} y mi edad es de {carla2.edad}")
# print(f"my nombre es {carla3.name} y mi edad es de {carla3.edad}")
# print(f"my nombre es {carla4.name} y mi edad es de {carla4.edad}")
# print(f"my nombre es {carla5.name} y mi edad es de {carla5.edad}")
'''
class fabian:

    def __init__(self , name,apellido, email_address,signo,edad):
    	# los asignamos en consecuencia
        self.name = name
        self.apellido=apellido
        self.email = email_address
        self.edad=edad
fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
 fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
fabian = Usuario("fabi","Torres","fabian1970@gmail.com",53)
print(f"my nombre es {fabian.name} y mi edad es de {fabian.edad}")

class ely:

    def __init__(self , name,apellido, email_address,signo,edad):
    	# los asignamos en consecuencia
        self.name = name
        self.apellido=apellido
        self.email = email_address
        self.edad=edad
ely= Usuario("fabi","Torres","fabian1970@gmail.com",53)
fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
 fabian= Usuario("fabi","Torres","fabian1970@gmail.com",53)
fabian = Usuario("fabi","Torres","fabian1970@gmail.com",53)
print(f"my nombre es {fabian.name} y mi edad es de {fabian.edad}")

'''

'''class Alumno:
    def __init__(self,curso,hora,fecha):
        self.curso=curso
        self.hora=hora
        self.fecha=fecha

Carla = Alumno("4°C",420,2023)


class fabian:
    def __init__(self,nombre,edad,profesion):


informacion=fabian()'''



