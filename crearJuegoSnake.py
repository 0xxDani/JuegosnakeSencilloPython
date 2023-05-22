import turtle                        #IMPORTAR LIBRERIA turtle
import time                          #ESTA LIBRERÍA NOS SIRVE PARA CUADRARLE LOS TIEMPOS A LAS EJECUCIONES.
import random

posponer = 0.1
#MARCADOR

score = 0
high_score = 0

#CREAR VENTANA

wn = turtle.Screen()                 #CREAR VENTANA
wn.title("JUEGO DE SNAKE.")          #TÍTULO DEL JUEGO
wn.bgcolor("#00CED1")                #COLOR DE LA VENTANA
wn.setup(width = 600, height = 600)  #TAMAÑO DE LA VENTANA
wn.tracer(0)                         #FUNCIÓN PARA MEJORAR LA VISTA


#CREAR CABEZA

cabeza = turtle.Turtle()             #CABEZA DE LA SERPIENTE
cabeza.speed(0)                      #CON ESTA FUNCIÓN HACEMOS QUE EL ELEMENTO APAREZCA EN PANTALLA QUIETO
cabeza.shape("square")               #ASÍ PODEMOS DARLE UNA FORMA DE CUADRADO.
cabeza.color("black")                #DARLE COLOR A LA CABEZA DE LA SERPIENTE. (EN ESTE CASO EL CUADRADO)
cabeza.penup()                       #QUITAR EL RASTRO DEL MOVIMIENTO
cabeza.goto(0,0)                     #DARLE UNA POSICIÓN EN PANTALLA
cabeza.direction = "stop"            #CON ESTA FUNCIÓN PODEMOS DARLE UNA DIRECCIÓN A LA CABEZA

#COMIDA DE LA SERPIENTE

comida = turtle.Turtle()             #COMIDA DE LA SERPIENTE
comida.speed(0)                      #CON ESTA FUNCIÓN HACEMOS QUE EL ELEMENTO APAREZCA EN PANTALLA QUIETO
comida.shape("circle")               #ASÍ PODEMOS DARLE UNA FORMA DE CÍRCULO A LA COMIDA.
comida.color("#00008B")              #DARLE COLOR A LA COMIDA DE LA SERPIENTE. (EN ESTE CASO EL CIRCULO)
comida.penup()                       #QUITAR EL RASTRO DEL MOVIMIENTO
comida.goto(0,100)                   #DARLE UNA POSICIÓN EN PANTALLA AL CÍRCULO


segmentos = []

#TEXTO
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0       High Score: 0", align = "center", font =("Courier", 22, "normal"))


#CUERPO DE LA SERPIENTE/SEGMENTOS
segmentos = []


#CON ESTA FUNCIÓN PODEMOS DARLE UNA DIRECCIÓN A LA CABEZA

#FUNCIONES PARA CAMBIAR LA DIRECCION.

def arriba():
    cabeza.direction = "up"          #EN ESTA PARTE DECLARAMOS LAS FUNCIONES PARA PODER CONECTARLAS Y MANEJARLAS   
                                     #DESDE TECLADO
def abajo():
    cabeza.direction = "down"        #POSTERIORMENTE VA A IR AL SIGUIENTE BLOQUE DE FUNCIONES DONDE YA LES TENEMOS
                                     #ASIGNADAS SUS DEMÁS FUNCIONES
def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

#FUNCIONES QUE DEFINEN LOS MOVIMIENTOS DE LAS FLECHAS DEL TECLADO
    
#AQUÍ DECLARAMOS LAS FUNCIONES PARA QUE LA CABEZA SE MUEVA                          
#ESTO FUNCIONA COMO UN PLANO CARTESIANO DONDE (Y) ES VERTICAL Y (X) ES HORIZONTAL.


def mov():
    if cabeza.direction == "up":     #CABEZA HACIA ARRIBA
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":   #CABEZA HACIA ABAJO
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":   #CABEZA HACIA LA IZQUIERDA
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":  #CABEZA HACIA LA DERECHA
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#CONECTAR AL TECLADO LAS FUNCIONES

wn.listen()                          #CON ESTA FUNCION LE DAMOS LA INSTRUCCIÓN AL PROGRAMA DE QUE SE CONECTE
                                     ##AL TECLADO
wn.onkeypress(arriba, "Up")          
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")     #AQUÍ LE DAMOS LA INSTRUCCIÓN A LAS FLECHAS CON ESA SINTÁXIS
wn.onkeypress(derecha, "Right")


while True:                          #AQUÍ SE INICIA EL BUCLE DEL JUEGO.
    wn.update()                      #ESTO ACTIVA EL CICLO CON LA VENTANA DESDE UN INICIO

    #COLISIONES PANTALLA.

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #ESCONDER LOS SEGMENTOS
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #LIMPIAR LISTA DE SEGMENTOS
        segmentos.clear()

        #RESETEAR MARCADOR
        score = 0
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score),
                    align = "center", font =("Courier", 22, "normal"))
            
    #COLISIONES CON LA COMIDA

    if cabeza.distance(comida) <20:        #AQUÍ INDICAMOS QUE SI LOS DOS ELEMENTOS DE JUNTAN LA COMIDA SE MUEVA
        x = random.randint(-280,280)       #A CUALQUIER POSISION (RANDOM) EN LA VENTANA
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()             #NUEVO SEGMENTO
        nuevo_segmento.speed(0)                      #CON ESTA FUNCIÓN HACEMOS QUE EL NUEVO SEGMENTO APAREZCA
                                                     # EN PANTALLA QUIETO
                                
        nuevo_segmento.shape("square")               #ASÍ PODEMOS DARLE UNA FORMA DE CUADRADO AL NUEVO SEGMENTO
        nuevo_segmento.color("yellow")               #DARLE COLOR AL NUEVO SEGMENTO. (EN ESTE CASO UN CUADRADO NUEVO
        nuevo_segmento.penup()                       #QUITAR EL RASTRO DEL MOVIMIENTO

        segmentos.append(nuevo_segmento)

        #AUMENTAR MARCADOR
        score += 10

        if score > high_score:
            high_score = score
            
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score),
                    align = "center", font =("Courier", 22, "normal"))
             

    #MOVER EL CUERPO DE LA SERPIENTE

    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()                            #AQUÍ LLAMAMOS LA FUNCIÓN mov DEFINIDA ANTERIORMENTE AL CICLO DEL JUEGO

    # COLISIONES CUERPO

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #ESCONDER LOS SEGMENTOS
            for segmento in segmentos:
                segmento.goto(1000,1000)

            #LIMPIAR LOS ELEMENTOS DE LA LISTA
            segmentos.clear()

            #RESETEAR MARCADOR
            score = 0
            texto.clear()
            texto.write("Score: {}       High Score: {}".format(score, high_score),
                        align = "center", font =("Courier", 22, "normal"))

    time.sleep(posponer)     #AQUÍ CON ESTA FUNCIÓN PODEMOS PONER A FUNCIONAR LA CONSTANTE
                             # QUE NOS DISMINUYE EL TIEMPO DE EJECUCIÓN DE LAS FUNCIONES DE TODO EL CÓDIGO
    





















    
