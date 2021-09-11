#encabezado
#reto5
import os
import math
import csv

from math import asin, cos, radians, sin, sqrt

from os import read, system
from typing import Coroutine

#from numpy import double
# from typing import Sized
#import numpy as np
# Definicion de variables y/o constantes
opciones = ['1.Cambiar contraseña','2.Ingresar coordenadas actuales','3.Ubicar zona wifi más cercana','4.Guardar archivo con ubicación cercana','5.Actualizar registros de zonas wifi desde archivo','6.Elegir opción de menú favorita','7.Cerrar sesión']
password='90615' # Por ahora como variable global pa ir trabajando , pero creeria que lo ideal es renovarla!?
coordenada= []
coordenadas_predefinidas = [[-3.777,-70.302,91],[-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
R = 6372.795477598
# definicion de funciones


def inicio_sesion():
    
        # Solucion reto1
        # En este reto se creara un log in con usuario, contraseña y captcha.
        # Datos usuario y captcha

        # En las siguientes dos lineas se realiza la limpieza de la consola
        # codigo que funciona en windows
        
        system("cls")

        # A continuacion son los datos del usuario que realiza el ingreso
        user_name = '51609'  #codigo del grupo
        password = '90615'  # la contraseña es el usuario al revés
        captcha = 609-(5+6-9-1-1) # como el penúltimo numero es 0, entonces se busca una operación aritmetica
        # que de 0 en el segundo termino y el primer termino son los 3 ultimos digitos del codigo

        # Ingreso de datos y validacion
        print('Bienvenido al sistema de ubicacion para zonas públicas WIFI') # Bienvenida al sistema
        # system("cls")
        InputUserName = input(' Nombre de usuario: ')  #Ingreso de usuario
        if InputUserName == user_name:  # Se valida si el usuario ingresado es correcto o no
            InputPassword = input(' Contraseña: ') # SI el usuario es correcto, se procede a solicitar la contraseña
            if InputPassword == password: # Se valida la contraseña si es correcta o no
                CaptchaIngresada = input('Ingrese la suma de 609-(5+6-9-1-1): ') #En caso de haber ingresado la contraseña sea correcta, se imprime en pantalla la captcha
                CaptchaIngresada = int(CaptchaIngresada)# Se convierte la captcha ingresada a entero para poder comparar
                system("cls")
                if CaptchaIngresada == captcha: # Se compara el resultado real de la captcha con la ingresada por el usuario
                    return 'sesión iniciada'# Si es correcta la respuesta ingresadda, se imprime Sesion iniciada
                else: 
                   return 'Error'# Se imprime error si no se ingresa el usario bien
            else:
                return 'Error'# Se imprime error si no se ingresa la contraseña bien
        else:
           return 'Error'# Se imprime error si no se ingresa la respuesta de la catcha bien

# Confirmacion antes de hacer el cambio a la opcion favorita
def  confirmacion(array):
    casillero=[]
    original = ['1.Cambiar contraseña','2.Ingresar coordenadas actuales','3.Ubicar zona wifi más cercana','4.Guardar archivo con ubicación cercana','5.Actualizar registros de zonas wifi desde archivo','6.Elegir opción de menú favorita','7.Cerrar sesión']
    print('Adivina....')
    numero1=input('Si me giras sigo siendo el mismo: ')    
    if numero1 == '0':
        numero2 = input('Si me giras me restas 3 unidades: ')
        if numero2 == '9':
            system("cls")
            for i in array:
                casillero.append(i)
               # print(i)
            return casillero
        else:
            print('Error')
            menu(original)
    else:
        print('Error')
        menu(original)

# Validacion de la contraseña , para realizar cambio de contraseña
def validacion_contraseña(contraseña_actual):
    contraseña = input('Ingrese contraseña actual: ')
    if contraseña == contraseña_actual:
        nueva_contraseña = input('Ingrese nueva contraseña: ')
        if nueva_contraseña != contraseña_actual:
            return nueva_contraseña
        else:
            return'Error'
    else:
        return 'Error'


# realiza la transpuesta de cualquier matriz  
def transponer(matriz):
    t=[]
    for i in range(len(matriz[0])):
        t.append([])
        for j in range(len(matriz)):
            t[i].append(matriz[j][i])
    return t
#Busca el menor de la cordenada latitud para ver cual esta mas al sur    
def menor_sur(matriz):
                menor = matriz[0][0]
                cordenada_menor = 0
                for fila in range(len(matriz)):
                    aux =matriz[fila][0]
                    if menor > aux :
                        menor = matriz[fila][0]
                        cordenada_menor=fila
                return(cordenada_menor)
#Busca el mayor de la cordenada latitud para ver cual esta mas al norte            
def mayor_norte(matriz):
                mayor = matriz[0][0]
                cordenada_mayor = 0
                for fila in range(len(matriz)):
                    aux =matriz[fila][0]
                    if mayor < aux :
                        mayor = matriz[fila][0]
                        cordenada_mayor = fila
                    
                return(cordenada_mayor) 
#Busca el menor de la cordenada longitud para ver cual esta mas al occidente
def menor_occidente(matriz):
                menor = matriz[0][1]
                cordenada_menor = 0
                for fila in range(len(matriz)):
                    aux =matriz[fila][1]
                    if menor > aux :
                        menor = matriz[fila][1]
                        cordenada_menor=fila
                return(cordenada_menor)
#Se realiza el promedio de las latitudes y longitudes                 
def promedio_cordenadas(matriz):
    arr=transponer(matriz)# se hace la transpuesta para poder tomar las latitudes
    # y longitudes por filas
    latitudes = arr[0]
    longitudes = arr[1]
    promedio_latitud = sum(latitudes)/len(latitudes)
    promedio_longitud = sum(longitudes)/len(longitudes)
    return promedio_latitud, promedio_longitud
#Se le entrega la matriz vacia o llena para entregarle las nuevas cordenadas o 
# simplemente para ingresarlas por primera vez, en ambos casos se usa la funcion
def filling_cordinates(arr,size,indice_matriz):
    for i in range(0,size):
                arr.append(round(float(input('Ingrese en '+str(indice_matriz))),3))
                if (arr[0] < -4.227 or arr[0] > -3.002):
                    
                    return 'Error coordenada'
                    
                if i == 1:
                    if (arr[1] < -70.366 or arr[1] > -69.714):
                        
                        return 'Error coordenada'
    return arr
#esta funcion concatena los vectores a,b,c para entregarlos como nueva ubicacion
# teniendo en cuenta que previamente a su entrega se verifican los valores ingresados
def coordenadas(ubicacion,contraseña):
    
        a_size = 2#Size del arreglo a( contiene latitudes)
        b_size = 2#Size del arreglo a( contiene longitudes)      
        c_size =2
        #Declaring an empty 1D array.
        a = []
        #Declaring an empty 1D array.
        b = []
        c=[]
   
        if ubicacion == []:# verifica que la matriz ubicacion este vacia
            a = filling_cordinates(a,a_size,'a') # funcion filling que llena la matriz 
            if a == 'Error coordenada':
                return 'Error coordenada'


            b = filling_cordinates(b,b_size,'b')   
            if b == 'Error coordenada':
                return 'Error coordenada'
          
            c = filling_cordinates(c,c_size,'c') 
            if c == 'Error coordenada':
                return 'Error coordenada'
     
        
            ubicacion_nueva = [a,b,c]
            return ubicacion_nueva
        else:
            print('cordenada [latitud,longitud] 1: '+ str(ubicacion[0]))
            print('cordenada [latitud,longitud] 2: '+ str(ubicacion[1])) 
            print('cordenada [latitud,longitud] 3: '+ str(ubicacion[2]))
            cordenada_mas_occide=menor_occidente(ubicacion)
            [promedio_latitud,promedio_longitud] = promedio_cordenadas(ubicacion)
            print('La cordenada '+ str(cordenada_mas_occide+1)+ ' es la que esta mas al occidente')
            print('El promedio de la latitud es : '+ str(promedio_latitud))
            print('El promedio de la longitud es : '+ str(promedio_longitud))
            print('Presione 1,2 o 3 para actualizar la respectiva cordenada')
            print('Presione 0 para regresar al menu')
            opcion_cordenada = input('Ingrese cordenada a modificar')
            if opcion_cordenada == '0':
                return ubicacion
                

            elif opcion_cordenada == '1':
                a = filling_cordinates(a,a_size,'a')
                b = ubicacion[1]
                c = ubicacion[2]

                if a == 'Error coordenada':
                    return 'Error actualización'
       
                else:
                    ubicacion_nueva = [a,b,c]
                    return ubicacion_nueva
            elif opcion_cordenada == '2':
                a = ubicacion[0]
                b = filling_cordinates(b,b_size,'b')
                c = ubicacion[2]
                if b == 'Error coordenada':
                    return 'Error actualización'
       
                else:
                    ubicacion_nueva = [a,b,c]
                    return ubicacion_nueva

            elif opcion_cordenada == '3':
                a = ubicacion[0]
                b = ubicacion[1]
                c = filling_cordinates(c,c_size,'c')       
                if c == 'Error coordenada':
                    return 'Error actualización'
         
                else:
                    
                    ubicacion_nueva = [a,b,c]
                    return ubicacion_nueva
            else:
                return 'Error actualización'

            
        # ubicacion_nueva = ubicacion
        # return ubicacion_nueva          
def distancia(dist1,dist2):# dist1 es una matriz de coordenadas predefinidas y dist2 es el punto actual del usuario
    lat_predefinida = []
    lon_predefinida = []
    lat_actual = math.radians(dist2[0])
    lon_actual = math.radians(dist2[1])
    distance = []
    
    matriz_predefinida = transponer(dist1)    
    for i in matriz_predefinida[0]:       
        i = math.radians(i)
        #print("i = ",i)
        lat_predefinida.append(i)
    for j in matriz_predefinida[1]:        
        j = math.radians(j)
        #print("j = ",j)
        lon_predefinida.append(j)

    for k in range(4):
        delta_lat = lat_predefinida[k] - lat_actual
        delta_long = lon_predefinida[k] - lon_actual       
       
        l = 2*R*asin(sqrt((sin(delta_lat/2)**2)+(cos(lat_actual)*cos(lat_predefinida[k]))*sin(delta_long/2)**2))
        distance.append(l)
        
        
    return distance
# el_mas_cerca Saca los dos valores mas cercanos en distancia
def el_mas_cerca(distancia):
    aux_distancia = distancia.copy()
    primer_minimo = min(aux_distancia)
    primer_indice = distancia.index(primer_minimo)
    aux_distancia.pop(primer_indice)
    segundo_minimo = min(aux_distancia)
    segundo_indice = distancia.index(segundo_minimo)
    return primer_minimo, segundo_minimo, primer_indice,segundo_indice

def menor_usuarios(arr,indx1,indx2):#traigo M_aux completa para poder sacar los indices que tienen
    #menor catindad de usarios
    aux = arr.copy()#creo una copia para no afectar el original    
    aux = [[aux[0][indx1],aux[0][indx2]],[aux[1][indx1],aux[1][indx2]]]# Pone las dos distancias mas cortas en pareja con la cantidad de usarios correspondientes
    aux_minimos = aux[1]
    numero_menor_usuarios = min(aux_minimos)
    indice_chico_aux = aux_minimos.index(numero_menor_usuarios)# Se saca el indice del auxiliar para eliminarlo y luego encontrar el otro menor
    indice_menor = arr[1].index(numero_menor_usuarios)# se saca el indice menor de arr, que es el que tiene la coordenada verdadera del arreglo
    #aux_minimos.pop(indice_chico_aux)
    aux_minimos[indice_chico_aux] = 10000
    numero2_menor_usuarios = min(aux_minimos)
    indice2_menor = arr[1].index(numero2_menor_usuarios)
    casillero = [arr[0][indice_menor],arr[0][indice2_menor]]
    return casillero,indice_menor,indice2_menor # se retornan los indices de menores usuarios con la distancia
    # respectiva

def eleccion_zona_wifi(choose,distance1,distance2):
    if choose == '1':
        tiempo_auto,tiempo_bicicleta = tiempo_llegada(distance1)
        print("El tiempo en auto es: "+str(tiempo_auto)+" Y el tiempo en bicicleta es: "+str(tiempo_bicicleta))
        return tiempo_auto,tiempo_bicicleta, "En auto"
    elif choose == '2':                                            
        tiempo_auto,tiempo_bicicleta = tiempo_llegada(distance2)
        print("El tiempo en auto es: "+str(tiempo_auto)+" Y el tiempo en bicicleta es: "+str(tiempo_bicicleta))
        return tiempo_auto,tiempo_bicicleta,"En auto"
    else:
        return 'Error zona wifi'
                          

def tiempo_llegada(distance):
    velocidad_auto = 20.83
    velocidad_bicicleta = 3.33
    tiempo_auto = distance/velocidad_auto
    tiempo_bicicleta = distance/velocidad_bicicleta
    return tiempo_auto,tiempo_bicicleta

# esta funcion tiene la finalidad de decirle que direccion tomar para ir a la zona wifi elegida
# por el usuario.

###########################################################################################################
#verificar los direccionamientos, siempre oriente y luego sur???
def direccionamiento_a_zona(eleccion,coord1,coord2,localizacion,eleccion_localizacion):
    if eleccion == '1':
        arreglo_coordenadas = [coord1,localizacion[eleccion_localizacion]]
        cerca_norte = mayor_norte(arreglo_coordenadas)
        cerca_occidente = menor_occidente(arreglo_coordenadas)                         
        if cerca_occidente == 0:            
            if cerca_norte == 0:
                print('Dirijase al occidente primero y luego dirijase al norte')
            else:
                print('Dirijase al occidente primero y luego dirijase al sur')
        else:            
            if cerca_norte == 0:
                print('Dirijase al oriente primero y luego dirijase al norte')
            else:
                print('Dirijase al oriente primero y luego dirijase al sur') 
    elif eleccion == '2':
        arreglo_coordenadas = [coord2,localizacion[eleccion_localizacion]]
        cerca_norte = mayor_norte(arreglo_coordenadas)
        cerca_occidente = menor_occidente(arreglo_coordenadas)                         
        if cerca_occidente == 0:            
            if cerca_norte == 0:
                print('Dirijase al occidente primero y luego dirijase al norte')
            else:
                print('Dirijase al occidente primero y luego dirijase al sur')
        else:            
            if cerca_norte == 0:
                print('Dirijase al oriente primero y luego dirijase al norte')
            else:
                print('Dirijase al oriente primero y luego dirijase al sur')
    else:
        return 'Error zona wifi'

def opciones_coordenadas_punto3(coordenadas_predefinidas,location,punto_actual):
    
    distancia_a_punto = distancia(coordenadas_predefinidas ,location[punto_actual])# Entrega distancia 
    cord_transpuesta = transponer(coordenadas_predefinidas)# hace transpuesta de las cordenadas predefi...
    primero,segundo,primer_index,segundo_index = el_mas_cerca(distancia_a_punto)#Indeices de las distancias mas cortas(primer_index,segundo_index)
    M_aux = [distancia_a_punto,cord_transpuesta[2]]# acoplo la distancia con la cantidad de usarios                   
    M_menores,index_min1,index_min2= menor_usuarios(M_aux,primer_index,segundo_index)#m_menores es la matriz con las dos distancias mas corta, 
    #index_min1 e index_min2 son los indices de las zonas con menos personas conectadas a wifi
    coordenada_cercana_latitud = coordenadas_predefinidas[index_min1][0]# saco coordenadas cercanas del de menor usuarios
    coordenada_cercana_longitud = coordenadas_predefinidas[index_min1][1]# tanto latitud como longitud                     
    coordenadas_cercanas_menor_usuarios_1= [coordenada_cercana_latitud,coordenada_cercana_longitud]# acoplo lat y lon 
    distancia_coordenada_1 = M_menores[0]# distancia a la zona wifi 1 de menos usuarios
    coordenada_cercana_latitud_2 = coordenadas_predefinidas[index_min2][0]# lo mismo pero para la segunda
    coordenada_cercana_longitud_2 = coordenadas_predefinidas[index_min2][1]# coordenada cercana                     
    coordenadas_cercanas_menor_usuarios_2= [coordenada_cercana_latitud_2,coordenada_cercana_longitud_2]                    
    distancia_coordenada_2 = M_menores[1]# distancia a la zona wifi 2 de menos usuarios
    print("La zona wifi 1: Ubicada en "+"["+str(coordenadas_cercanas_menor_usuarios_1[0])+","+str(coordenadas_cercanas_menor_usuarios_1[1])+"]"+" a "+str(M_menores[0])+" metros ,con  un promedio de usarios: "+str(coordenadas_predefinidas[index_min1][2]))
    print("La zona wifi 2: Ubicada en "+"["+str(coordenadas_cercanas_menor_usuarios_2[0])+","+str(coordenadas_cercanas_menor_usuarios_2[1])+"]"+" a "+str(M_menores[1])+" metros ,con  un promedio de usarios: "+str(coordenadas_predefinidas[index_min2][2]))
    eleccion = input('Ingrese 1 o 2 segun la zona que desee ir: ')                          
    validacion_zona_wifi = direccionamiento_a_zona(eleccion,coordenadas_cercanas_menor_usuarios_1,coordenadas_cercanas_menor_usuarios_2,location,punto_actual)# mando la eleccion hecha por usuario    
    if validacion_zona_wifi == 'Error zona wifi':
        return 'Error zona wifi',eleccion,distancia_coordenada_1,distancia_coordenada_2
    else:
        return 'ok',eleccion,distancia_coordenada_1,distancia_coordenada_2
    
def alistamiento(localizacion,coordenadas_wifi,recorrido,punto_acutal,eleccion,dist1,dist2):
        actual = localizacion[punto_acutal]
        zona_wifi1 = coordenadas_wifi[int(eleccion)]
        recorrido = list(recorrido)
        recorrido_auto = recorrido.copy()
        recorrido_auto.pop(1)
        tiempo_carro = recorrido_auto[0]
        medio_transporte = recorrido_auto[1]
        
        if eleccion == '1':
            distancia = dist1
        elif eleccion == '2':
            distancia = dist2
        arr = [actual,zona_wifi1]
  
        with open('informacion.csv','w',newline='') as csvfile:

            filednames = ['actual','zonawifi1','recorrido']
    
            thewriter = csv.DictWriter(csvfile, fieldnames=filednames)

            thewriter.writeheader()
           
                                 
        with open('informacion.csv',newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            print('informacion = ',{'actual':actual,'zonawifi1': zona_wifi1,'recorrido':[distancia,medio_transporte,tiempo_carro]}) 
            acuerdo = input('¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal') 
            if acuerdo == '0':
                 return 'menu'
            elif acuerdo == '1':
                with open('informacion.csv','w',newline='') as csvfile:

                    filednames = ['actual','zonawifi1','recorrido']
            
                    thewriter = csv.DictWriter(csvfile, fieldnames=filednames)

                    thewriter.writeheader()
                    thewriter.writerow({'actual':actual,'zonawifi1': zona_wifi1,'recorrido':[distancia,medio_transporte,tiempo_carro]})
                    print('Exportando archivo')          

def actualizacion_coordenadas_predefinidas ():
        with open('actualizacion.csv',newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            casillero = []
            for row in reader:
                casillero.append(row)
                #print(row)
            return casillero


     
def menu(opciones, contraseña_actual,location,punto_actual=-1,eleccion=0,resultados_tiempos=0,distancia_coordenada_1=0,distancia_coordenada_2=0,coordenadas_predefinidas = coordenadas_predefinidas):# parametros que se renuevan dentro del codigo
    for contador in range(3):
        system("cls")    
        for i in opciones:
            print(i)
        opcion = input('Elija una opción')
        if opcion == '6' :# eleccion de opcion 'favorita'
            system("cls")
            favorito = int(input('Seleccione opción favorita')) - 1
            if favorito == 5 or favorito == 6:# Se coloca que el caso 6 y 7 no se modifiquen( recordar que empieza desde el 0, por lo que iguala a 5 y 6)
                print('Error')
                break
            elif favorito == 0 or (favorito >=1 and favorito <=4):
                if favorito == 0:
                    opciones = opciones                
                    confirmacion(opciones)
                    break
                
                elif favorito>= 1 and favorito <= 4:
                    opciones.insert(0,opciones[favorito])
                    opciones.pop(favorito+1)
                    nuevo_menu = confirmacion(opciones)
                    menu(nuevo_menu, contraseña_actual,location)
                    break
                            
            else:
                print('Error')
                break
        
        elif opcion == '1': # cambio de contraseña
            print('Usted ha elegido la opción 1')
            confirmacion_contraseña = validacion_contraseña(contraseña_actual)
            if confirmacion_contraseña == 'Error':
                print('Error')
                break
            else: 
                contraseña_actual = confirmacion_contraseña# Se le asigna la nueva contraseña a contraseña actual 
                menu(opciones, contraseña_actual,location)                       
                break
        elif opcion == '2':

            cordenada_actual = coordenadas(location, contraseña_actual)# cordenada actual variable global
            if cordenada_actual == 'Error coordenada' or cordenada_actual == 'Error actualización':
                
                print(cordenada_actual)
                break

            else:
                
                location = cordenada_actual
                print(location)              

                menu(opciones,contraseña_actual,location)
                break
            
        elif opcion == '3':
            if location==[]:
                print("Error sin registro de coordenadas")
                break
            else:
                print('cordenada [latitud,longitud] 1: '+ str(location[0]))
                print('cordenada [latitud,longitud] 2: '+ str(location[1])) 
                print('cordenada [latitud,longitud] 3: '+ str(location[2]))
                punto_actual = int(input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: '))
                if punto_actual == 1:
                    punto_actual -= 1 
                    # opciones_coordenadas_punto3 encapsula gran cantidad del codigo de cada opcion, se repite para la 1,2 y 3
                    validacion_zona_wifi ,eleccion,distancia_coordenada_1 ,distancia_coordenada_2 = opciones_coordenadas_punto3(coordenadas_predefinidas,location,punto_actual)
                    if validacion_zona_wifi == 'Error zona wifi':
                        print('Error zona wifi')
                        break
                    # junto con las coordenadas cercanas de menor usuarios, la numero uno y la que le sigue; y finalmente la localizacion actual del usuario
                    resultados_tiempos= eleccion_zona_wifi(eleccion,distancia_coordenada_1,distancia_coordenada_2)
                    opcion_final = input('Presione 0 para salir')
                    if opcion_final == '0':
                        menu(opciones,contraseña_actual,location,punto_actual,eleccion,resultados_tiempos,distancia_coordenada_1,distancia_coordenada_2)
                    if resultados_tiempos == 'Error zona wifi':
                        print(resultados_tiempos)
                        break
                    break
                elif punto_actual == 2:
                    punto_actual -= 1
                     # opciones_coordenadas_punto3 encapsula gran cantidad del codigo de cada opcion, se repite para la 1,2 y 3
                    validacion_zona_wifi ,eleccion,distancia_coordenada_1 ,distancia_coordenada_2 = opciones_coordenadas_punto3(coordenadas_predefinidas,location,punto_actual)
                    if validacion_zona_wifi == 'Error zona wifi':
                        print('Error zona wifi')
                        break
                    if validacion_zona_wifi == 'Error zona wifi':
                        print('Error zona wifi')
                        break                    
                    resultados_tiempos= eleccion_zona_wifi(eleccion,distancia_coordenada_1,distancia_coordenada_2)
                    opcion_final = input('Presione 0 para salir')
                    if opcion_final == '0':
                        menu(opciones,contraseña_actual,location,punto_actual,eleccion,resultados_tiempos,distancia_coordenada_1,distancia_coordenada_2)
                    if resultados_tiempos == 'Error zona wifi':
                        print(resultados_tiempos)
                        break
                    break                    
                    
                elif punto_actual == 3:
                    punto_actual -= 1
                     # opciones_coordenadas_punto3 encapsula gran cantidad del codigo de cada opcion, se repite para la 1,2 y 3
                    validacion_zona_wifi ,eleccion,distancia_coordenada_1 ,distancia_coordenada_2 = opciones_coordenadas_punto3(coordenadas_predefinidas,location,punto_actual)
                    if validacion_zona_wifi == 'Error zona wifi':
                        print('Error zona wifi')
                        break
                    if validacion_zona_wifi == 'Error zona wifi':
                        print('Error zona wifi')
                        break                   
                    resultados_tiempos= eleccion_zona_wifi(eleccion,distancia_coordenada_1,distancia_coordenada_2)
                    opcion_final = input('Presione 0 para salir')
                    if opcion_final == '0':
                        menu(opciones,contraseña_actual,location,punto_actual,eleccion,resultados_tiempos,distancia_coordenada_1,distancia_coordenada_2)                 
                    if resultados_tiempos == 'Error zona wifi':
                        print(resultados_tiempos)
                        break                    
                    break                
                else: 
                    print("Error ubicación")
                    break
        elif opcion == '4':
            if punto_actual == -1:
                print('Error de alistamiento')
            elif location ==[location]:
                print('Error de alistamiento')
            else:
                accion = alistamiento(location,coordenadas_predefinidas,resultados_tiempos,punto_actual,eleccion,distancia_coordenada_1,distancia_coordenada_2)
                if accion == 'menu':
                     menu(opciones,contraseña_actual,location,punto_actual,eleccion,resultados_tiempos,distancia_coordenada_1,distancia_coordenada_2)

            break
        elif opcion == '5':
            coordenadas_predefinidas = actualizacion_coordenadas_predefinidas()
            print(coordenadas_predefinidas)
            regresar_menu = input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal')
            if regresar_menu == '0':
                menu(opciones,contraseña_actual,location,punto_actual,eleccion,resultados_tiempos,distancia_coordenada_1,distancia_coordenada_2,coordenadas_predefinidas)
            break
        elif opcion == '7':
            print('Hasta pronto')
            break
            
        else:                       
             
            print('Error')
        
   
#codigo principal

ingreso =inicio_sesion()
print(ingreso)

system("cls")
if ingreso == 'sesión iniciada':
    menu(opciones,password,coordenada)# parametros iniciales

    
