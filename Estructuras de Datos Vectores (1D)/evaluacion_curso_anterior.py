"""Escribir un algoritmo que permita cargar un vector de 10 numeros enteros (positivos o negativos) entre -100 y 100.
No debe aceptar valores fuera de este intervalo. DIFICULTAD 1 - LISTO

Luego de la carga se debe proporcionar un menú (debe estar en un ciclo) con las siguientes opciones:
Mostrar números cargados (todos).*
Realizar la sumatoria de los valores positivos impares.*
Realizar el conteo de los valores negativos.*
Calcular el promedio de todos los valores positivos ingresados.*
Obtener el menor de los números primos ingresados. Mostrar aviso en caso de que no se hayan ingresado números primos.(no se como se hace ) perdon!!

Obtener el número negativo que más veces se repite en el vector. Mostrar aviso en caso de que no se hayan ingresado números negativos.

Generar un vector destino y copiar (en las mismas posiciones del arreglo original)
****los valores positivos que superen el promedio calculado en el punto 4, 
en el resto de posiciones copiar el valor 0. **** re loco !!! no se hace 

Salir del programa  menos mal!!! jajaj hdp"""

import array as arr
mi_arreglo=arr.array('i',[0]*3)
print(len(mi_arreglo))
for i in range(len(mi_arreglo)):
    carga_de_valores=int(input(f"ingrese valor entre -100 y 100  ingrese valor {i+1} : "))
    if carga_de_valores>=-100 and carga_de_valores<=100:
        mi_arreglo[i]=carga_de_valores
      
print("listo arreglo ")

     
opcion=0
while opcion !=7:
    print("**************mi menu *******************")
    print("1 para mostrar  numeros cargados (todos) ")#listo
    print("2 para realizar al sumatoria de todos los valores positivos inpares ")
    print("3 realizar el conteo de todos los valores negativos ")
    print("4 calcular el promedio de todos los valores positivos ingresados ")
    print("5 obtener el numero negativo que mas veces se repite en el vector ,mostrar aviso en caso de que no se hayan ingresado numeros negativos ")
    print("6 generar un vector destino y copiar  en las mismas posiciones ")
    print("7 salir del programa ")
    opcion=int(input("que desea hacer lcdtm?")) 
    if opcion==7:
        print("gracias por utlizar el programa ")
        break 
    elif opcion==1:
        print(mi_arreglo)
    elif opcion==2:
        arreglo_positivos_inpares=[numero for numero in mi_arreglo if  numero >0 and numero %2!= 0]#jajaja no me peque
        suma_arreglo_positivos_inpares=sum(arreglo_positivos_inpares)
        print(f"opcion 2 la suma es {suma_arreglo_positivos_inpares}")
    

        



     