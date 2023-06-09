
class tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.list=[]

    def agregar_producto(self,nuevo_producto):
        self.list.append(nuevo_producto)
        return self

    def vender_producto(self,id):
        for x in self.list:
            if x.nombre==id:
                x.remove
            else:
                print("producto no existe")
        return self  
    def listar_producto(self,id):
        for x in self.list:
            x.imprimir()
        return self  