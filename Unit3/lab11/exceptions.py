

class ErrorInventario(Exception):
    """Clase base para todas las excepciones relacionadas con el inventario."""
    pass

class ProductoNoEncontrado(ErrorInventario):
    """Se lanza cuando el código del producto no existe en el inventario."""
    pass

class CantidadInvalida(ErrorInventario):
    """Se lanza cuando la cantidad ingresada es cero, negativa o no válida."""
    pass

class StockInsuficiente(ErrorInventario):
    """Se lanza cuando la cantidad solicitada supera el stock disponible."""
    pass