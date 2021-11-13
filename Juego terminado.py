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
        print("Intenta adivinar el numero: ")
        intento = int(input())
        numero_intentos += 1

        if intento < numero :
            print("Su numero es menor que el numero generado")
        if intento > numero :
            print("Su numero es mayor que el numero generado")
        if intento == numero:
            break
    if time == number:
        print("\n¡Enhorabuena! Has adivinado el número aleatorio en" ,str(times), "oportunidades.")
        score = maxtime - times
    
    if time != number:
         print("Otra vez será, no ha logrado adivinar el número aleatorio en los" + str(maxtime) + "intentos posibles.")
         
         if chossen_mode == 2:
            times = 0
            minIA = min
            maxIA = max 
            time = (minIA + maxIA)//2
            while time != number and times < maxtime:
                time = (minIA + maxIA)//2
                times += 1
                print("La IA ha comprobado el número introducido " + str(time) + " y ")
                if time > number:
                    print("este se encuentra por encima del número proporcionado.\n")
                    maxIA = time
                elif time < number:
                        print("este se encuentra por debajo del número proporcionado.\n")
                        minIA = time + 1
                        print("es el número a adivinar.\n")
                        print("Ha tardado " + str(times) + (" intentos."))
choose_level()

    