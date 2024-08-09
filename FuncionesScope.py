#Scope (o alcance) de variables
# 1. Scope Global

valor_numerico = 50

#Funcion con alcance global
def PresentaValorNumerico():
    print(valor_numerico)

#Funcion con alcance global    
def PresentaValorNumericoConMensajeAdicional():
    print("El valor es:", valor_numerico)

#Funcion con alcance global
def PresenteUnNuevoValor():
    print(100)
    
    #variable con scope (alcance) local
    mensajeHolaMundo = "Hola Mundo"
    
    #funcion con scope(alcance) local
    def MuestraHolaMundo():
        print("Esta es una ejecucion desde la funcion interna")
        print(mensajeHolaMundo)
        
    MuestraHolaMundo()
    print(mensajeHolaMundo)
    
PresentaValorNumerico()
PresentaValorNumericoConMensajeAdicional()
