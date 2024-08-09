from random import randint

opciones = ["piedra", "papel", "tijera"]
valor_aleatorio = randint(0,2)
juego_computador = opciones[valor_aleatorio]

juego_usuario = input("¿qué elije? piedra, papel, tijera")

if juego_usuario ==juego_computador:
    print("¡es un empate!")
elif juego_usuario == "piedra":
    if juego_computador ==papel:
        print("¡perdiste!", juego_computador, "cubre", juego_usuario)
    else:
        print("¡ganaste!", juego_usuario, "aplasta", juego_computador)
elif juego_usuario == "papel":
    if juego_computador == "tijera":
        print("¡perdiste!", juego_computador, "corta", juego_usuario)
    else:
        print("¡ganaste!", juego_usuario, "cubre", juego_computador)
elif juego_usuario =="tijera":
    if juego_computador == "piedra":
        print("¡perdiste!", juego_computador, "aplasta", juego_usuario)
    else:
        print("¡ganaste!", juego_usuario, "corta", juego_computador)
else:
    print("palabra no valida")