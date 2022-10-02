#importamos los módulos que necesitarémos random para barajear las imágenes
import tkinter
import random
import time


#creamos la ventana y la configuramos    
ventana = tkinter.Tk()
ventana.geometry("1200x950")
ventana.configure(bg="spring green")
#ventana.resizable(0,0)
ventana.title("MEMORAMA")
#ventana.iconbitmap("imagenes_memorama/recordar.ico")


#cargamos las imágenes del memorama
imagen0=tkinter.PhotoImage(file="imagenes_memorama/rana.png")
imagen1=tkinter.PhotoImage(file="imagenes_memorama/elefante.png")
imagen2=tkinter.PhotoImage(file="imagenes_memorama/delfin.png")
imagen3=tkinter.PhotoImage(file="imagenes_memorama/aguila.png")
imagen4=tkinter.PhotoImage(file="imagenes_memorama/tortuga.png")
imagen5=tkinter.PhotoImage(file="imagenes_memorama/tigre.png")

#imagen de las tapas de las cartas
imapreg=tkinter.PhotoImage(file="imagenes_memorama/interrogante.png")

#ponemos las imagenes en un arreglo
imagenes=[imagen0,imagen1,imagen2,imagen3,imagen4,imagen5,imagen0,imagen1,imagen2,imagen3,imagen4,imagen5]


#barajeamos las imágenes del memorama con fisher-yates
def shuffle(arr):
    last_index = len(arr)-1
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        temp = arr[last_index]
        arr[last_index] = arr[rand_index]
        arr[rand_index] = temp
        last_index -= 1

    return arr

#mandamos a llamar la función de barajeo y obtenemos nuestras imagenes barajeadas
barajeado=shuffle(imagenes)




#intentos para que tome los intentos que le está tomando al usuario
intentos=0

#etiqueta que muestra los intentos hechos por el usuario
etiqueta_intentos=tkinter.Label(ventana,text=" Intentos : "+str(intentos),font=("Impact",30),bg="RoyalBlue4",fg="white")
etiqueta_intentos.place(x=965,y=350)


#creamos los 12 botones configurados, lo más importante es el argumento que le pasamos a eleccion que es la posicion que va a ser comparada en nuestro array barajeado


botones=[]
for i in range (12):
    boton=tkinter.Button(ventana,image=imapreg,width="180",height="180",command=lambda numelec=i:eleccion(numelec))
    botones.append(boton)


#variable para recorrer los botones y colocarlos
c=0

for x in range(3):
    for y in range(4):
        
        botones[c].grid(row=x,column=y,padx=25,pady=25)
        c+=1






miFrame=tkinter.Frame(ventana,background="gold")






#contadr_elec para que cuente los dos clickeo por turno
contador_elec=0
#contador_gana si empareja 6 pares
contador_gana=0
#posiciones va a tomar las posiciones de las cartas que se mandan desde lambda y así poder comparar las cartas de las posiciones de las cartas en el array barajeado
posiciones=[None,None]
#guarda las posiciones de las cartas emparejadas, para así no provocar un error con los contadores
emparejados=[]
def eleccion(n):
    #declaramos las variables globales para que funcionen fuera de la función
    global contador_gana,posiciones,emparejados,intentos,ventana,miFrame
    
    #si se seleccionó una imagen de las que ya está acertada (emparejada) no hace nada
    if n in emparejados:
        pass
    else:
        #si no se ha seleccionado ninguna carta en estos 2 clickeo por turno del usuario lo que hacemos es...
        if posiciones[0]==None:
            #cambiamos la imagen que tenía como tapa en el botón
            botones[n].config(image=barajeado[n])
            #agregamos la posición del primer botón seleccionado de los 2 clickeo por turno para después comparar esa posicion con la posicion del siguiente botón
            #en el arreglo barajeado
            posiciones[0]=n

        #si ya ha seleccionado 1 botón    
        elif(posiciones[0]!=None):
            #si n es decir la posicion pasada desde el botón como argumento es igual a la de este segundo intento no hace nada
            if posiciones[0]==n:
                pass
            #si la segunda posición del clickeo por turno es distinta al primero 
            elif(posiciones[0]!=n):
                #guardamos la posición del botón de este segundo clickeo por turno
                posiciones[1]=n

                #cambiamos la imágen del botón este segundo clickeo por turno
                botones[n].config(image=barajeado[n])
                #refrescamos para que se vean los cambios en la interfaz
                ventana.update()

                #comparamos las dos posiciones de los dos clickeo por turno
                #si coinciden las imagenes en las dos posiciones de los dos clickeos por turno en el arreglo barajeado
                if barajeado[posiciones[0]]==barajeado[posiciones[1]]:
                    #acerto un par, aumenta contador_gana
                    contador_gana+=1
                    #guardamos las posiciones que emparejamos
                    emparejados.append(posiciones[0])
                    emparejados.append(posiciones[1])
                    #limpiamos las posiciones para el siguiente turno
                    posiciones=[None,None]
                    #aumentamos los intentos
                    intentos+=1
                    #cambiamos la etiqueta_intentos con el texto de la variable intentos
                    etiqueta_intentos.config(text=" Intentos : "+str(intentos))
                else:
                    #si no coincidieron las imagenes espera para cambiar las imagenes en los botones en las posiciones que no eran iguales las imagenes
                    time.sleep(0.25)
                    #cambiamos las imagenes a la imagen incógnita imapreg
                    botones[posiciones[0]].config(image=imapreg)
                    botones[posiciones[1]].config(image=imapreg)
                    #borramos las posiciones para el siguiente turno
                    posiciones=[None,None]
                    #aumentamos los intentos
                    intentos+=1
                    #cambiamos la etiqueta_intentos con el texto de la variable intentos
                    etiqueta_intentos.config(text="Intentos : "+str(intentos))

    #si acierta los 6 pares el usuario ganó      
    if contador_gana==6:
        #espera para destruir los widgets
        time.sleep(1)
        
        
        
        #destruye los botones
        for i in range(12):
            botones[i].destroy()

        #muestra un mensaje en una etiqueta
        tkinter.Label(ventana,text=" ¡¡Bien hecho!! ",font=("Impact",50),fg="gold",bg="white").place(x=350,y=300)
        
        

ventana.mainloop()
