class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio 
        self.registro=registro
    def cambiarColor(self,colorn):
        if colorn in ["amarillo", "verde", "blanco", "negro", "rojo"]:
            self.color = colorn

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro (self,registro):
        self.registro=registro
    def asignarTipo(self,tipon):
        if tipon in ["gasolina", "electrico"]:
            self.tipo=tipon
class Auto:
    def __init__(self,modelo,precio,motor,marca,asientos=None,registro=None,cantidadCreados=0):
        self.modelo=modelo
        self.registro=registro
        self.precio=precio
        self.Motor=motor
        self.marca=marca
        self.asientos=asientos if asientos is not None else[]
        Auto.cantidadCreados=cantidadCreados
       
    def cantidadAsientos(self):
        num_asientos = 0
        for asiento in self.asientos:
            if asiento is not None:
                num_asientos += 1
        return num_asientos
    
    def verificarIntegridad(self):
        if self.registro == Motor.registro:
            for asiento in self.asientos:
                if asiento is not None and asiento.registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"
