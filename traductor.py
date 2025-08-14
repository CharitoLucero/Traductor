#----------------------------------------------------------
# Intalamos con pip instal mysql-conector-python

import mysql.connector
import mysql.connector.errorcode

# Instalar con pip install flask
from flask import Flask, request, jsonify, render_template
from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Si es necesario, pip install werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#----------------------------------------------------------

#Crear una instancia de aplicacion flask
app = Flask(__name__)
CORS(app) #Se habilita CORS para la apicacion Flask. CORS es una caracteristica de seguridad en los navegadores que restringe como los recursos wn unapagina web pueden ser solicitadas desde otro dominio distinto del que sirvio lapagina original. Al habilitar CORS, se permite que lo recursos de la aplicacion web sean accesibles desde otros dominios, lo cual es necesario en muchos casos, como cuando se desarrolla una API que necesita ser consumido dde diferentes dominios.


#----------------------------------------------------------
# Definimos clase Catalogo
#----------------------------------------------------------

class Traductor:
    '''
    Esta Clase proporciona metodos para administrar un catalago de language almacenados en una base de datos MySQL
    '''
    
    #Constructor
    def __init__(self, host, user, database):
        '''
        Inicializa una instancia de caalogo y crea una conexion a la base de datos

        Args:
        host (str): La direccion del servidor de l base de datos
        user: (str): El nomre del usuario para acceder a la base de datos
        password (str): La contrasea del usuario
        database (str): El nombre de la base de datos
        '''

        #PRIMER PASO: establecer una conexin sin especificar la base de datos. self.conn es un atributo de la clase que representa una conexion activa a una base de datos.

        self.conn = mysql.connector.connect(
            host = host,
            user = user
        )

        #Un cursor permite interactuar con la base de datos de forma más directa. A través de este cursor, se pueden ejecutar comandos SQL.

        self.cursor = self.conn.cursor()

        #Conectar a la base de datos

        try:
            self.cursor.execute(f'USE {database}')
        except mysql.connector.Error as err:

            #Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database}')
                self.conn.database = database
            else:
                raise err    

        #Una vez que la base de datos esta establecida, crearmos la tabla si no existe


        self.cursor.execute('''CREATE TABLE IF NOT EXISTS language(
                    codigo INT AUTO_INCREMENT PRIMARY KEY,
                    categoria VARCHAR (255) NOT NULL,
                    español VARCHAR (255) NOT NULL,
                    ingles VARCHAR (255) NOT NULL,
                    frances VARCHAR (255) NOT NULL,
                    aleman VARCHAR (255) NOT NULL,
                    imagen_url VARCHAR (255)
                    )''')
        
        #Guardar cambios en la base de datos
        self.conn.commit()

        #Cerrar el cursor inicial y abrir una nueva con el parametro dictionary=True

        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        #self.conn.cursor(dictionary=True) devuelve cada fila como un diccionario. Cada FILA se representa como un diccionario, donde las CLAVES son los nombres de las COLUMNAS y los valores son los datos correspondientes. Esto facilita el acceso a los datos que recordar el orden de las columnas.


    def agregar_palabra(self, categoria, español, ingles, frances, aleman, imagen_url):

      sql = 'INSERT INTO language (categoria, español, ingles, frances, aleman, imagen_url) VALUES (%s, %s, %s, %s,%s, %s)'
      #Los valores se pasan como parametros separados a la consulta, la que asegura que sean tratados como datos y no como parte del codigo SQL. Los marcadores de posicion %s son reemplazados por los valores reales de los parametros cuando se ejecuta la consulta.

    
      valores = (categoria, español, ingles, frances, aleman, imagen_url)
     
      self.cursor.execute(sql, valores) #Ejecuta
      self.conn.commit() #Guarda
      return self.cursor.lastrowid #proporciona eel valor de la clave primaria automaticamente por la base de datos para la fila recien insertada.


    #----------------------------------------------------------
    # Metodo para consultar un palabra a partir de su codigo
    #----------------------------------------------------------


    def consultar_palabra(self, codigo):
        #Consultamos un palabra a partir de su codigo
        self.cursor.execute(f'SELECT * FROM language WHERE codigo = {codigo}')
        return self.cursor.fetchone() #fetchone devuelve un solo registro 



    #----------------------------------------------------------
    # Metodo para modificar un palabra a partir de su codigo
    #----------------------------------------------------------

    def modificar_palabra(self, codigo, nueva_categoria, nuevo_español, nuevo_ingles, nuevo_frances, nuevo_aleman, nueva_imagen):

        # Modificamos los datos de un palabra a partir de su codigo 
        # Los %s se utilizan para indicar que alli se debe insertar un valor especificos mas adelante, luego, los valores se pasan como un argumento separado al metodo execute

        sql = 'UPDATE language SET categoria=%s, español=%s, ingles=%s, frances=%s, aleman=%s, imagen_url=%s WHERE codigo = %s'


        valores = (nueva_categoria, nuevo_español, nuevo_ingles, nuevo_frances, nuevo_aleman, nueva_imagen, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
        #rowcount() se utiliza para comprobar si una operacion SQL ha afectado a alguna fila en la base de datos. Es una comparacion que verifica si este numero es mayor que cero, indica que al menos una fila fue afectada
            
        
    #----------------------------------------------------------
    # Metodo para listar un palabra a partir de su codigo
    #----------------------------------------------------------

    def listar_palabra(self):
       # Mostramos un listado de todos los language en la tabla
       self.cursor.execute('SELECT * FROM language')
       language = self.cursor.fetchall() #devuelve tods las filas en una consulta SQL
       return language


    #----------------------------------------------------------
    # Metodo para eliminar un palabra a partir de su codigo
    #----------------------------------------------------------

    def eliminar_palabra(self, codigo):
        self.cursor.execute(f'DELETE FROM language WHERE codigo = {codigo}')
        self.conn.commit()
        return self.cursor.rowcount > 0
        #rowCount() se utiliza para comprobar si una operación SQL ha afectado a alguna fila en la base de datos. Es una comparación que verifica si este número es mayor que cero, indica que al menos una fila fue afectada.


#--------------------------------------------------------
# Programa Principal - Ejemplo de uso de funciones
#--------------------------------------------------------

traductor = Traductor(host='localhost',user='root', database='traductor')

#traductor = Catalogo(host='USUARIO.mysql.pythonanywhere-services.com', user='USUARIO', password='CLAVE', database='USUARIO$miapp')

#Agregar Productos

# traductor.agregar_producto('Teclado USB 101 Teclas', 10, 12000, "imagenjpg", 100)
# traductor.agregar_producto('Mousse USB 3 botones', 5, 2500, "mouse.jpg", 102)
# traductor.agregar_producto('Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
# traductor.agregar_producto('Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg',104)
# traductor.agregar_producto('Pad mouse', 5, 500, 'padmouse.jpg', 105)


#Carpeta para guardar las imagenes
RUTA_DESTINO = './static/imagenes/'

#Al subir al servidor, debera utilizar la siguiente ruta, USUARIO debe ser reemplazado por el nombre de USUARIO de Pythonanywhere

#RUTA_DESTINO = '/home/USUARIO/mysite/static/imagenes'


#---------------------------------------------------------
#    Listado de Productos
#---------------------------------------------------------


@app.route('/language', methods=['GET']) #GET: metodo para obtener resuestas a uestras peticiones
def listar_palabra():
      palabra = traductor.listar_palabra()
      return jsonify (palabra)


#---------------------------------------------------------
#   Mostrar solo un palabra segun su codigo
#---------------------------------------------------------

@app.route('/language/<int:codigo>', methods=['GET'])
def mostrar_palabra(codigo):
    palabra = traductor.consultar_palabra(codigo)
    if palabra:
        return jsonify(palabra), 201
    else:
        return 'Palabra no encontrada', 404


#---------------------------------------------------------
#    Agregar Productos
#---------------------------------------------------------

@app.route('/language', methods=['POST'])
#La ruta Flask '/language' con el metodo HTTP POST esta diseada para permitir la adicion de un nuevo palabra a la base de datos.

#La funcion agregar_producto se asocia con esta URL y es llamada cuando se hace una solicitud POST a /language
def agregar_palabra():
    #Se toman los datos del form

    categoria = request.form['categoria']
    español = request.form['español']
    ingles = request.form ['ingles']
    frances = request.form ['frances']
    aleman = request.form ['aleman']
    imagen = request.files['imagen'] 
    nombre_imagen = ''

    #Se genera el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del articulo de la imagen, asegurandose de que sea seguro para guardar en el sistema de archivos
    nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extension 
    nombre_imagen = f'{nombre_base}_{int(time.time())}{extension}' #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

    nuevo_codigo = traductor.agregar_palabra(categoria, español, ingles, frances, aleman, nombre_imagen)
    if nuevo_codigo:
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        
        #Si el palabra se agrega con exito, se devuelve una respuesta JSON con un mensaje de xito y un codigo de estado HTTP 201 ()
        return jsonify({'mensaje': 'Palabra agregada correctamente.', 'codigo': nuevo_codigo, 'imagen': nombre_imagen}), 201
    else:
        #Si el palabra no se puede agregar, se devuelve una respuesta JSON con un mensaje de error y un codigo de estado HTTP 500 (Interner Server Error)
        return jsonify({'mensaje': 'Error al agregar la palabra.'}), 500
    

#---------------------------------------------------------
#    Modificar Productos
#---------------------------------------------------------

@app.route('/language/<int:codigo>', methods=['PUT'])
#La ruta  Flask /language/<int:codigo con el metodo HTTP PUT esta diseñada para actualizar la informacion de un palabra existente en la base de datos, identificado por su codigo
#La funcion modifcar_producto se ascia con esta URL y es invocada cuando se realiza una solicitud PUT a /language/ seguido de un numero (el codigo del palabra)
def modificar_palabra(codigo):
    nueva_categoria = request.form.get('categoria')
    nuevo_español = request.form.get('español')
    nuevo_ingles = request.form.get('ingles')
    nuevo_frances = request.form.get('frances')
    nuevo_aleman = request.form.get('aleman')

    # Verifica si se proporciono una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        #Procesamiento de la imagen
        nombre_imagen = secure_filename (imagen.filename)#Chequeo el nombre del archivo de la imagen asegurandose de que sea seguro para guardar en el sistema de archivos
        nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archvo de su extension
        nombre_imagen = f'{nombre_base}_{int(time.time())}{extension}' #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescribir y conflictos de nombres

        #Guardar imagen en e servidor
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))

        #Busco el palabra guardado
        palabra = traductor.consultar_palabra(codigo)
        if palabra: # Si existe el palabra...
            imagen_vieja = palabra['imagen_url']
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)
       
        # Y si existe la borro.
        if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    
    else:
        # Si no se proporciona una nueva imagen, simplemente usa la imagen existente del palabra
        palabra = traductor.consultar_palabra(codigo)
        if palabra:
            nombre_imagen = palabra["imagen_url"]


    # Se llama al método modificar_producto pasando el codigo del palabra y los nuevos datos.
    if traductor.modificar_palabra(codigo, nueva_categoria, nuevo_español, nuevo_ingles, nuevo_frances, nuevo_aleman, nombre_imagen):
        
        #Si la actualización es exitosa, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
        return jsonify({"mensaje": "Palabra modificado"}), 200
    else:
        #Si el palabra no se encuentra (por ejemplo, si no hay ningún palabra con el código dado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Palabra no encontrado"}), 403


#---------------------------------------------------------
#    Eliminar un palabra segun su codigo
#---------------------------------------------------------
@app.route('/language/<int:codigo>', methods={'DELETE'})
#La ruta Flask /palabra/<int:codigo> con el metodo HTTP DELETE esta diseñada para eliminar un palabra especifico de la base de datos, utilizando su codigo como identificador
#La funcion eliminar_producto se asocia con esta URL y es llamada cuando se realiza una solictud DELETE a /language/ seguido de un numero (el codigo de palabra)
def eliminar_palabra(codigo):
    #Busco el palabra en la base de datos
    palabra = traductor.consultar_palabra(codigo)
    if palabra: # si el palabra existe, verifica si hay imagen asociada en el servidor
        imagen_vieja = palabra['imagen_url']
        # Armo la ruta a la imagen
        ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

        # Y si existe, lo elimina del sistema de archivos
        if os.pat.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimna el palabra del traductor
        if traductor.eliminar_palabra(codigo):
            #Si el palabra se elimina correctamente, se devuelve una respuesta JSON con un mensaje de exito y un codigo de estado HTTP 200 (OK)
            return jsonify({'mensaje': 'Palabra eliminada'}), 200
        else:
            #Si ocurre un error durante la eliminacion (por ejemplo, i e produto no se puede eliminar de la base de datos por alguna razon), se devuelve un mensaje de error con un codigo de estado http 500 (Error Interno del Servidor)
            return jsonify({'mensaje': 'Error al eliminar la palabra'}), 500
    else:
        # Si el palabra n se encuentra (por ejemplo, si no existe un palabra con el codigo proporcionado), se devuelve un mensaje de error con un codigo de estado HTTP 404 (No Encontrado)
        return jsonify({"mensaje": "Palabra no encontrada"}), 404



#-------------------------------FLASK-----------------------
if __name__ == '__main__':
    app.run(debug=True)