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
i=0
while i<len(mi_arreglo):
    carga=int(input(f"ingrese numeros entre -100 y 100 {i+1} : "))
    if carga>=-100 and carga<=100:
        mi_arreglo[i]=carga
        i+=1
    else:
        print("valor no admitido ")

    


print(f"el arreglo cargado es : {mi_arreglo }")








        



     