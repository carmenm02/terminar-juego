import random

def elige_nivel():
    print("Selecciona un nivel de dificultad: ")
    print("Nivel 1: Simple")
    print("Nivel 2: Intermedio")
    print("Nivel 3: Avanzado")
    print("Nivel 4: Experto")
    nivel_elegido = int(input("Selecciona un nivel de dificultad: "))
    global eleccion
    eleccion = nivel_elegido
    if 0 < eleccion <= 4 :
        if eleccion == 1 :
            print("Nivel de dificultad simple")
        if eleccion == 2 :
            print("Nivel de dificultad intermedio")
        if eleccion == 3 :
            print("Nivel de dificultad avanzado")
        if eleccion == 4 :
            print("Nivel de dificultad experto")
    else:
        print("Selecciona un nivel de dificultad, porfavor")
def game ():
    print("Elija un modo de juego:")
    print("1 = Usuario \n ")
    print("2 = IA")
    elige_nivel = int(input("Selecciona el modo deseado de juego"))
    elige_modo = elige_nivel
    if 0 < elige_modo <= 4 :
        if elige_modo == 1:
            print("El modo elegido es Usuario")
        if elige_modo == 2:
            print("El modo seleccionado es IA")
    else:
        print("Selecciona un modo")
if elige_modo == 1:
    numero_intentos = 0
    while numero_intentos < maximo_intentos :
        print