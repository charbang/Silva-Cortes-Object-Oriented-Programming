
from products import Producto
from exceptions import ProductoNoEncontrado

class Inventario:
    def __init__(self):
       
        self.productos = {
            "P001": Producto("P001", "Laptop", 10),
            "P002": Producto("P002", "Mouse", 25),
            "P003": Producto("P003", "Teclado", 15)
        }

    def retirar(self, codigo: str, cantidad: int) -> int:
        """
        Verifica que el producto exista y delega el retiro al objeto Producto.
        Permite que las excepciones de Producto se propaguen.
        """
        
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Error: El código de producto '{codigo}' no existe en el inventario.")
        
        
        return self.productos[codigo].retirar(cantidad)