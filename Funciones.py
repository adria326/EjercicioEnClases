#Funcion sin parametros
def MostarMensaje():
    "Muestra un mensaje de prueba"
    
    print("Hola Mundo")
    return

#Funcion con Parametros (argumentos)
def MostrarMensajeConParametros(nombre):
    "Muestra un mensaje de prueba"
    
    print("Hola", nombre)
    return
    
#Funcion sin paremetros(argumentos) que retornan un valor
def MostrarMensajeNueva():
    print("Hola Clase")
    return True

    
#Funcion con paremetros(argumentos) que retornan un valor
def MostrarMensajeNuevaConParametros(nombre):
    mensaje ="Hola " + nombre
    print(mensaje)
    return mensaje

mensaje_devuelto = MostrarMensajeNuevaConParametros("Adriana")

print(mensaje_devuelto, "segunda ejecucion")