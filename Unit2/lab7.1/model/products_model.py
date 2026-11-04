from controller.connection_db import Database_connection


class Product:
    def __init__(self):
        self.db = Database_connection()

    def _conectar(self):
        return self.db.get_connection()

    def obtener_todos(self):
        conn = self._conectar()
        if not conn:
            return []

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id_product, nombre, precio, stock FROM products")
            filas = cursor.fetchall()
            return filas
        finally:
            cursor.close()
            conn.close()

    def agregar(self, nombre, precio, stock):
        conn = self._conectar()
        if not conn:
            return False

        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO products (nombre, precio, stock) VALUES (%s, %s, %s)",
                (nombre, precio, stock)
            )
            conn.commit()
            return True
        finally:
            cursor.close()
            conn.close()