
from inventory import Inventario
from exceptions import ErrorInventario

def main():
    mi_inventario = Inventario()

    print("--- SISTEMA DE CONTROL DE INVENTARIO ---")
    print("Productos disponibles: P001 (Laptop), P002 (Mouse), P003 (Teclado)\n")

    codigo = input("Ingrese el código del producto: ").strip()
    
    try:
     
        cantidad_input = input("Ingrese la cantidad a retirar: ")
        cantidad = int(cantidad_input)
        
      
        stock_restante = mi_inventario.retirar(codigo, cantidad)

    except ValueError:
        print("\n[Excepción Capturada]: ValueError -> Debe ingresar un número entero válido.")
    except ErrorInventario as e:
        print(f"\n[Excepción Capturada]: {e.__class__.__name__} -> {e}")
    else:
      
        print("\n[Éxito]: Operación completada exitosamente.")
        print(f"Stock restante del producto: {stock_restante}")

if __name__ == "__main__":
    main()