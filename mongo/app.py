# importar bibliotecas
import pymongo

# uri de mongo atlas
uri = "mongodb+srv://JuanVidal:sena123@cluster0.xvgr1vn.mongodb.net/?retryWrites=true&w=majority"
# conexion con mongo atlas
conexion = pymongo.MongoClient(uri)
# conexion a la base de datos
db = conexion["sena-prueba"]
# seleccionar la coleccion
coleccion = db["aprendices"]

def todos_aprendices():
    try:
        # obtener todos los aprendices
        aprendices = coleccion.find()
        # verificando si hay aprendices
        if aprendices:
            for aprendiz in aprendices:
                print(aprendiz)
        else:
            print("No hay aprendices!")

    except Exception as error:
        print("Error: ", error)

todos_aprendices()

"""
# conexion mongoDB de manera local
conexion = pymongo.MongoClient("localhost", 27017)
"""
# conexion = pymongo.MongoClient("mongodb://localhost:27017")
# seleccionar DB
baseDatos = conexion["tienda"]
# acceder a la collecion
productos = baseDatos["productos"]

# agregar productos
def add_producto():
    try:
        # estructura producto
        producto = {
            "codigo": 10,
            "nombre": "Televisor",
            "precio": 1000000,
            "categoria": "Electrodomestico" 
        }
        # insertando el producto con estructura en mongo
        resultado = productos.insert_one(producto)
        print("Producto ingresado exitosamente!")
        
    except pymongo.errors as error:
        print("Error: ", error)

# obtener producto por id
def get_producto_por_id():
    try:
        # codigo a buscar
        codigo_buscar = {"codigo": 10}
        # obtener producto por id con estructura en mongo
        producto = productos.find_one(codigo_buscar)
        # verificando el id exista
        if producto:
            print(producto)
        else:
            print(f"El producto con codigo {codigo_buscar['codigo']} no existe!")
        
    except pymongo.errors as error:
        print("Error: ", error)

# obtener todos los productos
def get_productos():
    try:
        # obtener todos los productos con estructura en mongo
        all_productos = productos.find()
        # verificando si hay productos
        if all_productos:
            for producto in all_productos:
                print(producto)
        else:
            print("No hay productos!")

    except pymongo.errors as error:
        print("Error: ", error)

# eliminar producto por id
def delete_producto():
    try:
        # codigo a buscar
        codigo_buscar = {"codigo": 10}
        # eliminar producto por id con estructura en mongo
        resultado = productos.delete_one(codigo_buscar)
        # verificando si se elimino
        if resultado.deleted_count > 0:
            print("Producto eliminado exitosamente!")
        else:
            print(f"El producto con codigo {codigo_buscar['codigo']} no existe!")

    except pymongo.errors as error:
        print("Error: ", error)

# actualizar producto por id
def update_producto():
    try:
        # codigo a buscar
        codigo_buscar = {"codigo": 10}
        # actualizar producto por id con estructura en mongo
        resultado = productos.update_one(codigo_buscar, {"$set": {"precio": 1500000}})
        # verificando si se actualizo
        if resultado.modified_count > 0:
            print("Producto actualizado exitosamente!")
        else:
            print(f"El producto con codigo {codigo_buscar['codigo']} no existe!")

    except pymongo.errors as error:
        print("Error: ", error)

# llamado de funciones
#add_producto() # agregar producto
# get_producto_por_id() # obtener producto por id
# get_productos() # obtener todos los productos
# delete_producto() # eliminar producto por id