# importar libreria para usar base de datos con sqLite
import sqlite3
# nombre de la base de datos
base_datos = "tienda.db"
# crear conexion con la base de datos, el parametro es la base de datos
conexion = sqlite3.connect(base_datos)

# funcion para agregar producto
def add_product():
    try:
        # columnas de la tabla en la db
        codigo_producto =11
        nombre_producto = "Pantalon Nike 32"
        precio_producto = 100000
        categoria_producto = "Pantalon"
        # orden del producto que se va a ingresar a la db
        producto = (codigo_producto, nombre_producto, precio_producto, categoria_producto)
        # consulta sql
        consulta = "insert into productos values (null, ?, ?, ?, ?)"
        # hace que la sentencia sql empiece
        cursor = conexion.cursor()
        # ejecucuion, recibe la consulta y la tupla con la informacion que se va a subir a la base de datos
        resultado = cursor.execute(consulta, producto)
        # verifica que la consulta sea correcta, se hace un commit cada vez que se actualice la base de datos
        conexion.commit()
        # mensaje que controla si se agrego un registro
        if resultado.rowcount == 1:
            print("Registro agregado con exito!")
        
        # en caso de haber un error en la conexion
    except conexion.Error as error:
        # no se hace la conexion
        conexion.rollback()
        print(f"Error al conectar la DB: {error}")
# todos los productos
def show_products():
    try:
        # consulta sql
        consulta = "SELECT * FROM productos"
        # iniciando cursor
        cursor = conexion.cursor()
        # ejecutando consulta
        cursor.execute(consulta)
        # obteniendo todos los productos
        productos = cursor.fetchall()
        # en caso de no haber productos
        if productos:
            # impriminedo los productos
            for producto in productos:
                print(producto)
        # en caso de no haber productos
        else:
            print("No hay productos agregados!")
        
    except conexion.Error as error:
        print(f"Error con la conexion: {error}")
# obteniendo producto por codigo
def show_product_by_id(codigo):
    try:
        # ibteniendo el codigo del producto
        codigo_producto = (codigo,)
        # consulta sql
        consulta = "select * from productos where proCodigo = ?"
        # iniciar el cursor
        cursor = conexion.cursor()
        # ejecutando la consulta, primer parametro para la consulta la segundo parametro es en c
        cursor.execute(consulta, codigo_producto)
        # obteniendo el producto buscado
        producto =  cursor.fetchone()
        
        # en caso de existir el producto va a retornar el producto
        if producto:
            print(producto)
            # en caso de no existir el productp
        else:
            print("No existe el producto")

    except conexion.Error as error:
        print(f"Error en la conexion: {error}")
# actualizar producto
def update_product(codigo):
    try:
        # nombre a actualizar
        nuevo_nombre = "Camiseta Nike M"
        # tupla que recibe 
        actualizacion = (nuevo_nombre, codigo)
        # consulta sql
        consulta = "update productos set proNombre = ? where proCodigo = ?"
        # inicializa la conexion
        cursor = conexion.cursor()
        # ejecuta la consutla, 1 parametro la consulta, 2 parametro tupla actualizada
        resultado = cursor.execute(consulta, actualizacion)
        # en caso tal de haber un error
        conexion.commit()
        # verificando que algun producto se haya actualizado
        if resultado.rowcount == 1:
            print("Producto actualizado con exito!")
            # en caso de no haber un producto con ese codigo
        else:
            print(f"No existe un producto con el codigo: {codigo}")
    # manejo de errores
    except conexion.Error as error:
        conexion.rollback()
        print(f"Error en la conexion: {error}")
# elimiar un producto por codigo
def delete_product(codigo):
    try:
        # consulta
        consulta = "delete from productos where proCodigo = ?"
        # iniciando cursor
        cursor = conexion.cursor()
        # ejecutando la consulta
        resultado = cursor.execute(consulta, (codigo,))
        # en caso de haber encontrado el producto
        if resultado.rowcount == 1:
            conexion.commit()
            print("Producto eliminado exitosamente!")
        else:
            print("El codigo ingresado no existe")
        
    except conexion.Error as error:
        conexion.rollback()
        print(f"Error en la conexion de la DB: {error}")
        
# llamado de la funciones
#add_product()
#show_product_by_id(10)
show_products()
#update_product(10)
#delete_product(10)