from models.Product import Producto
from sqlite3 import Connection


class ManagerProductos:

    def __init__(self):
        pass

    def postProducto(self, producto: Producto, conexion: Connection):

        conexion.execute(
            "INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
            (producto.nombre, producto.stock, producto.precio)
        )

        conexion.commit()

        return f"Guardando producto: {producto.nombre}"