
from exceptions import CantidadInvalida, StockInsuficiente

class Producto:
    def __init__(self, codigo: str, nombre: str, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def retirar(self, cantidad: int) -> int:
        """
        Valida que la cantidad a retirar sea un entero positivo y que 
        no supere el stock disponible. Actualiza y retorna el stock restante.
        """
        
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise CantidadInvalida(f"Error: La cantidad '{cantidad}' no es válida. Debe ser un número entero mayor a cero.")
        
        
        if cantidad > self.stock:
            raise StockInsuficiente(f"Error: Stock insuficiente. Stock actual: {self.stock}, cantidad solicitada: {cantidad}.")
        
       
        self.stock -= cantidad
        return self.stock