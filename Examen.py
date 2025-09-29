from abc import abstractmethod
from abc import ABC

class Empleado(ABC):
    def __init__(self, rfc:str, apellidos:str, nombres:str):
        self.__rfc=rfc
        self.__apellidos=apellidos
        self.__nombres=nombres 
    
    @abstractmethod
    def mostrar_informacion(self):
        pass
        
    

class EmpleadoVendedorJ3(Empleado):
    def __init__(self, rfc:str, apellidos:str, nombres:str, monto_vendido:float, tasa_comision:float):
        super.__init__(self, rfc, apellidos, nombres)
        self.monto_vendido=monto_vendido
        self.tasa_comision=tasa_comision
        
    def calcular_ingresos(self):
        ingresos=self.monto_vendido * self.tasa_comision
        return f"Tus ingresos son de ${ingresos} "
    
    def calcular_bonificacion(self, ingresos):
        if self.monto_vendido >= 1000:
            return "No tendra bonificacion"
        elif self.monto_vendido <= 1000 and self.monto_vendido >=5000:
            return ingresos * 0.05 
        else:
            pass
    
    def calcular_descuento(self):
        pass
    
    def calcular_sueldo():
        pass
    
class EmpleadoPermanenteJ3(Empleado):
    def __init__(self, rfc:str, apellidos:str, nombres:str, sueldo_base:float, seguro_social:str):
        super.__init__(self, rfc, apellidos, nombres)
        self.sueldo_base=sueldo_base
        self.seguro_social=seguro_social 
        
    def retornar_sueldo_base(self):
        return self.sueldo_base 
    
    def calcular_descuento():
        pass
    
    def sueldo_neto():
        pass
    
    
def main():
    
        mi_perro = EmpleadoPermanenteJ3('mamífero', 'j', 'e', 100, 200)
        mi_perro.retornar_sueldo_base()
        
        
        
if __name__==("__main__"):
    main()