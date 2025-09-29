"""Escribir un algoritmo que permita cargar un vector de 10 numeros enteros (positivos o negativos) entre -100 y 100.
No debe aceptar valores fuera de este intervalo. 

Luego de la carga se debe proporcionar un menú (debe estar en un ciclo) con las siguientes opciones:
1Mostrar números cargados (todos).*
2Realizar la sumatoria de los valores positivos impares.*
3Realizar el conteo de los valores negativos.*
4Calcular el promedio de todos los valores positivos ingresados.*
5Obtener el número negativo que más veces se repite en el vector. Mostrar aviso en caso de que no se hayan ingresado números negativos.
6Generar un vector destino y copiar (en las mismas posiciones del arreglo original)
7Salir del programa  menos mal!!! jajaim"""

import array as arr
mi_arreglo=arr.array('i',[0]*2)
i=0
while i<len(mi_arreglo):
    carga=int(input(f"ingrese valores entre -100 y 100  valor ingresado {i+1} :"))
    if carga>=-100 and carga<=100:
        mi_arreglo[i]=carga
        i+=1
    else:
        print("valor incorrecto ")


opcion=0  
while opcion!=7:
    print("*************MENU*****************")
    print("1 para mostrar números cargados (todos)")#listo
    print("2 para realizar la sumatoria de los valores positivos impares.")#listo
    print("3 para realizar el conteo de los valores negativos")#listo 
    print("4 para calcular el promedio de todos los valores positivos ingresados ")#listo
    print("5 para obtener el número negativo que más veces se repite en el vector. Mostrar aviso en caso de que no se hayan ingresado números negativos")
    print("6 para generar un vector destino y copiar (en las mismas posiciones del arreglo original")
    print("7 para salir del programa  menos mal!!! jaja que hdp!!! ")
    opcion=int(input("que desea hacer "))
    if opcion==1:
        print(mi_arreglo)
    elif opcion==2:
        valores_positivos_inpares=[numero for numero in mi_arreglo if numero >0 and numero%2!=0]
        print(f"punto 2 sumatoria valores + inpares : {valores_positivos_inpares} ")
        print(sum(valores_positivos_inpares))
    elif opcion==3:
        valores_negativos=[numero for numero in mi_arreglo if numero <0 ] 
        contador_negativos=0
        for numero in mi_arreglo:
            if numero<0:
                contador_negativos+=1
        print(f" numero de elemento negativos en el arreglo {contador_negativos}")
        if contador_negativos==0:
            print(" no hay numeros negativos no hay nada que contar ")
    elif opcion==4:
        saco_primero_los_valores_positivos=[numero for numero in mi_arreglo if numero>0]
        suma_de_promedio_positivos=sum(saco_primero_los_valores_positivos)
        
        cuento_los_elementos_valores_positivos=len(saco_primero_los_valores_positivos)
        if cuento_los_elementos_valores_positivos>0:
            promedio=suma_de_promedio_positivos/cuento_los_elementos_valores_positivos
            print(f"el promedio es {promedio}")
        else:
            print("no existe elemento para sacar promedio ")
    elif opcion==5:
        print("punto de la muerte ")
        print("ESTE PUNTO NO SE VIO EN CLASE POR DIFERENTES PAROS ")       
    elif opcion==6:
        vector_destino=arr.array('i',[0]*len(mi_arreglo))
        for i in range (len(mi_arreglo)):
            vector_destino[i]=mi_arreglo[i]
        print(f"arreglo mi arreglo original {mi_arreglo}")
        print(f"mi arreglo destino {vector_destino}") 
    elif opcion==7:
        print(" fin del programa que lo pario !!!! ")
        break
          

   
       
        
        

        



     