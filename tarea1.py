# Método para ingresar puntuación y comentarios
def ingresar_puntuacion_y_comentarios():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5.')
        punto = input()

        if punto.isdecimal():
            punto = int(punto)
        
            if punto <= 0 or punto > 5:
                print('Indíquelo en una escala de 1 a 5.')
            else:
                print('Por favor, introduzca un comentario')
                comentario = input()
                post = f'punto: {punto} comentario: {comentario}'
                with open('data.txt', 'a') as archivo:
                    archivo.write(f'{post} \n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

# Método para comprobar resultados guardados
def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open('data.txt', 'r') as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print(contenido)
            else:
                print('No hay resultados guardados aún')
    except FileNotFoundError:
        print('No se ha encontrado el archivo de datos. Aún no se han guardado puntuaciones.')

# Método para ejecutar el programa principal
def ejecutar_programa():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            if num == '1':
                ingresar_puntuacion_y_comentarios()
            if num == '2':
                comprobar_resultados()
            if num == '3':
                print('Finalizando...')
                break
            else:
                print('Introduzca un número del 1 al 3.')
        else:
            print('Introduzca un número del 1 al 3.')

# Ejecutar el programa
ejecutar_programa()