# Diccionario = []

#----------------CARGA INICIAL------------
Diccionario = [
    ['Animal', 'Gato', 'cat', 'chat', 'katze'],
    ['Animal', 'Perro', 'dog', 'chien', 'hund'],
    ['Animal', 'Raton', 'mouse', 'souris', 'maus'],
    ['Animal', 'Pajaro', 'bird', 'oiseau', 'vogel'],
    ['Numeros','Dos', 'Two', 'Deux', 'Zwei'],
    ['Numeros','Tres', 'Three', 'Trois', 'Drei'],
    ['Numeros', 'Cuatro', 'Four', 'Quatre', 'Vier'],
    ['Numeros', 'Cinco', 'Five', 'Cinq', 'Fünf'],
    ['Numeros', 'Seis', 'Six', 'Six', 'Sechs'],
    ['Numeros', 'Siete', 'Seven', 'Sept', 'Sieben'],
    ['Colores', 'Rojo', 'Red', 'Rouge', 'Rot'],
    ['Colores', 'Azul', 'Blue', 'Bleu', 'Blau'],
    ['Colores', 'Verde', 'Green', 'Vert', 'Grün'],
    ['Colores', 'Amarillo', 'Yellow', 'Jaune', 'Gelb'],
    ['Colores', 'Naranja', 'Orange', 'Orange', 'Orange'],
    ['Colores', 'Negro', 'Black', 'Noir', 'Shwarz']

]

# Menu 
opcion = ""
while opcion != 5:
    print('=' * 50)
    print('          Bienvenidos a Traductor         ')
    print('                Traducction                 ')
    print('               Menu Pricipal               ')
    print('')
    print('1. Agregar palabra')
    print('2. Mostrar palabra')
    print('3. Buscar palabra')
    print('4. Eliminar palabra')
    print('5. Salir')
    print('=' * 50)

    opcion = input('Selecciona una opción (1-5): ') #validar de que sea entero
    #validamos que sea nro y entre 1 y 5
    while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
        print('Opción Ínválida!')
        opcion = input('Selecciona una opción (1-5): ')
        
    opcion = int(opcion)

    #opciones del menú
    match opcion:
        case 1: 
            # Registro de Diccionario agregar palabra
            print('======== Registro de palabra ============')

            
            categoria = input('Ingrese categoria de la palabra: ').strip()
            word = input('Ingrese una palabra: ').strip()
            english = input('Ingrese la pabra en ingles: ').strip()
            french = input ('ingrese la palabra en frances: ').strip()
            germany = input ('ingrese la plabra en aleman: ').strip()

            # palabra = [categoria, word, english, french, germany]
            # Diccionario.append(palabra)
            # print('Palabra Registrada')

             # validaciones con variable bandera, alternativa al while
            datos_ok = True  # bandera

            if not categoria or not word or not english or not french or not germany:
                print("Todos los campos son obligatorios.")
                datos_ok = False

            if datos_ok:
                palabra = [
                    categoria.title(),
                    word.title(),
                    english.title(),
                    french.title(),
                    germany.title()
                ]
                Diccionario.append(palabra)
                print("Palabra registrado exitosamente.")
            else:
                print("Algún dato es inválido.")
            
        case 2:
            
            # Visualización de palabras
            print('======== Visualización del Diccionario ============')
            # if not Diccionario:
            #     print('No hay palabras registradas.')
            # else:
            #     print('Inventario: ')
            #     for i, palabra in enumerate(Diccionario, 1):
            #         # nombre, categoria, precio, marca = palabra
            #         # print(f'{i}. {nombre} {categoria} - Precio: ${precio} - Marca {marca}')
            #         # otra forma:
            #         print(f'{i}. Categoria: {palabra[0]} - Palabra: {palabra[1]} - Ingles: {palabra[2]} - Frances: {palabra[3]} - Aleman: {palabra[4]}')
                    
            # print("======== Lista de clientes ============")
            if not Diccionario:
                print("No hay Palabras registradas.")
            else:
                print("\n {:^75}".format("LISTADO DE PALABRAS"))
                print("-" * 75)
                print("{:<3} {:<15} {:<15} {:<15} {:<15} {:<15}".format("N°", "Categoria", "Palabra", "Ingles", "Frances", "Aleman"))
                print("-" * 75)

                for i, palabra in enumerate(Diccionario, 1):
                    print("{:<3} {:<15} {:<15} {:<15} {:<15} {:<15}".format(i, palabra[0], palabra[1], palabra[2], palabra[3], palabra [4]))


        case 3: 
            # Busqueda de Palabra
            print('======== Búsqueda de Palabra ============')
            # if not Diccionario:
            #     print('No hay palabras registrados.')
            # else:
            #     busqueda = input('Ingrese un palabra a buscar: ').strip().title()
            #     encontrados = []
                
            #     for palabra in Diccionario:
            #         if palabra[1] == busqueda:
            #             encontrados.append(palabra)
                        
            #     if encontrados:
            #         print('Productos encontrados: ')
            #         for i, palabra in enumerate(encontrados, 1):
            #             categoria, word, english, french, germany = palabra
                       
            #             print(f'{i}. Categoria: {palabra[0]} - Palabra: {palabra[1]} - Ingles: {palabra[2]} - Frances: {palabra[3]} - Aleman: {palabra[4]}')
                              
            #     else:
            #         print(f'No se encontraron palabras con esa nombre: {busqueda}')

            #         print("======== Búsqueda de cliente ============")
            if not Diccionario:
                print("No hay Palabras registradas.")
            else:
                palabra_buscar = input("Ingrese una palabra a buscar: ").strip().title()
                encontradas = [p for p in Diccionario if p[1] == palabra_buscar]

                if encontradas:
                    print("Resultados encontrados:")
                    print("-" * 75)
                    print("{:<3} {:<15} {:<15} {:<15} {:<15} {:<15}".format("N°", "Categoria", "Palabra", "Ingles", "Frances", "Aleman"))
                    print("-" * 75)

                    for i, palabra in enumerate(encontradas, 1):
                        print("{:<3} {:<15} {:<15} {:<15} {:<15} {:<15}".format(i, palabra[0], palabra[1], palabra[2], palabra[3], palabra [4]))
                else:
                    print(f"No se encontraron Palabras como: {palabra_buscar}")

        case 4:           
            #eliminación 
            # if not Diccionario: 
            #     print('No hay palabras registrados.')
            # else:
            #     print('Inventario: ')
            #     for i, palabra in enumerate(Diccionario, 1):
            #        print(f'{i}. Categoria: {palabra[0]} - Palabra: {palabra[1]} - Ingles: {palabra[2]} - Frances: {palabra[3]} - Aleman: {palabra[4]}')
                
            #     posicion = input('Ingrese el número de palabra a eliminar: ').strip()
            #     while not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(Diccionario):
            #         print('Ingrese valor válido: ')
            #         posicion = input('Ingrese el número de palabra a eliminar: ').strip()
                    
            #     pos = int(posicion)
                
              
            #     palabra_eliminada = Diccionario.pop(pos - 1)
            #     print(f' Palabra {palabra_eliminada[1]} eliminada.')


            #     print("======== Eliminación de cliente ============")
            if not Diccionario:
                print("No hay Palabras registradas.")
            else:
                print("\n {:^75}".format("LISTADO DE PALABRAS"))
                print("-" * 75)
                print("{:<3} {:<15} {:<15} {:<15} {:<15} {:<15}".format("N°", "Categoria", "Palabra", "Ingles", "Frances", "Aleman"))
                print("-" * 75)

                for i, palabra in enumerate(Diccionario, 1):
                    print("{:<3} {:<15} {:<15} {:<15} {:<15} {:<15}".format(i, palabra[0], palabra[1], palabra[2], palabra[3], palabra [4]))

                pos = input("Ingrese el numero de la palabra a eliminar: ").strip()
                # while not (pos.isdigit() and 1 <= len(Diccionario)):
                #     print("Palabra inválida.")
                #     pos = input("Ingrese la palabra a eliminar: ").strip()

                eliminada = Diccionario.pop(int(pos) - 1)
                print(f"Palabra{eliminada[1]} eliminada.")

                # coincidencias = [palabra for palabra in palabra if palabra in palabra[1]]

                # # Si hay coincidencias, eliminar
                # if coincidencias:
                #    for pos in coincidencias:
                #        Diccionario.remove(pos)
                #        print(f"Palabra: {palabra[0]} {palabra[1]} eliminada.")
                # else:
                #        print("No se encontró ningúna palabra que coincida.")
        

    # print('=' * 50)
    # print('          Bienvenidos a Traduction        ')
    # print('                Diccionario                 ')
    # print('               Menu Pricipal               ')
    # print('')
    # print('1. Agregar palabra')
    # print('2. Mostrar palabra')
    # print('3. Buscar palabra')
    # print('4. Eliminar palabra')
    # print('5. Salir')
    # print('=' * 50)

    # opcion = input('Selecciona una opción (1-5): ') #validar de que sea entero
    # #validamos que sea nro y entre 1 y 5
    # while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
    #     print('Opción Ínválida!')
    #     opcion = input('Selecciona una opción (1-5): ')
        
    # opcion = int(opcion)
    

print('Saliendo del Sistema...')           



