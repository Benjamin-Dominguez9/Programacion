# Definición de la clase base Fabrica
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

# Definición de la clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def __init__(self, llantas, color, precio, tipo_motor):
        super().__init__(llantas, color, precio)
        self.tipo_motor = tipo_motor

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Tipo de Motor: {self.tipo_motor}")

# Definición de la clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def __init__(self, llantas, color, precio, numero_puertas):
        super().__init__(llantas, color, precio)
        self.numero_puertas = numero_puertas

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Número de Puertas: {self.numero_puertas}")

# Creación de objetos de las clases Moto y Carro
moto1 = Moto(llantas=2, color="Rojo", precio=1500000, tipo_motor="4T")
carro1 = Carro(llantas=4, color="Azul", precio=2500000, numero_puertas=4)

# Mostrar atributos de cada objeto
print("Atributos de la Moto:")
moto1.mostrar_atributos()
print("\nAtributos del Carro:")
carro1.mostrar_atributos()
# Definición de la clase base Fabrica
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.90  # Aplicar un descuento del 10%
    
    def mostrar_atributos(self):
        self.aplicar_descuento()  # Aplicar descuento antes de mostrar los atributos
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio:.2f}")  # Mostrar el precio con 2 decimales

# Definición de la clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def __init__(self, llantas, color, precio, tipo_motor):
        super().__init__(llantas, color, precio)
        self.tipo_motor = tipo_motor

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Tipo de Motor: {self.tipo_motor}")

# Definición de la clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def __init__(self, llantas, color, precio, numero_puertas):
        super().__init__(llantas, color, precio)
        self.numero_puertas = numero_puertas

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Número de Puertas: {self.numero_puertas}")

# Creación de objetos de las clases Moto y Carro
moto1 = Moto(llantas=2, color="Rojo", precio=150000, tipo_motor="4T")
carro1 = Carro(llantas=4, color="Azul", precio=250000, numero_puertas=4)

# Mostrar atributos de cada objeto
print("Atributos de la Moto:")
moto1.mostrar_atributos()
print("\nAtributos del Carro:")
carro1.mostrar_atributos()

