"""EJERCICIO REPASO CONCEPTOS
Se desea desarrollar un programa en Python que permita repasar los principales conceptos de funciones, ámbito de variables, 
parámetros por valor y por referencia, validaciones, uso de break y continue, y manejo de estructuras de datos como listas y arreglos.
El programa debe mostrar un menú con las siguientes opciones:

************************
Suma: Llamar a una función que reciba tres valores y muestre su suma.
Promedio: Calcular y devolver el promedio de tres valores recibidos como parámetros.
Multiplicación y División: Crear una función que reciba dos valores, calcule su producto y su cociente, controlando la división por cero 
mediante validaciones.
Carga de Arreglo: Permitir al usuario ingresar valores numéricos para completar un arreglo de 4 elementos.
Carga de Lista: Permitir al usuario ingresar valores numéricos para completar una lista de 4 elementos.
Mostrar Elementos: Visualizar en pantalla los elementos cargados en el arreglo y en la lista, separados por un delimitador (por ejemplo, |).
Salir: Finalizar la ejecución del programa.
*******************

🔹 El menú debe validar que la opción ingresada esté dentro del rango (1 a 7), utilizando las sentencias continue y break para manejar errores
y repetir las solicitudes en caso de datos inválidos. 
🔹 El programa debe trabajar tanto con variables locales y globales como con parámetros pasados por valor y por referencia,
para mostrar claramente la diferencia entre estos conceptos """

import array as arr

def suma (n1,n2,n3):
    suma=n1+n2+n3
    return suma

def promedio(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    return promedio

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2


def cargar_numeros():
    n1=int(input("ingrese numero "))
    n2=int(input("ingrese numero "))
    n3=int(input("ingrese numero "))
    return n1,n2,n3

def carga_lista():
    pass

def mi_menu():
    while True:
        print("bienvenido al menu ")
        print("1 para hacer sumas ")
        print("2 para hacer promedio ")
        print("3 para hacer multiplicacion")
        print("4 para hacer division")
        print("5 para cargar arreglo ")
        print("6 para salir ")
        opcion=int(input("que desea hacer ingrese opcion menu "))
        if opcion==6:
            print("gracias por utilizar el programa ")
            break
        return opcion
      
        
    
        
            
def mi_main():
    opcion_recibida=mi_menu()
    if opcion_recibida==1:
        n1,n2,n3=cargar_numeros()
        sumando=suma(n1,n2,n3)
        print(f"la suma es {sumando}")
    elif opcion_recibida==2:
        n1,n2,n3=cargar_numeros()
        saco_promedio=promedio(n1,n2,n3)
        print(f"el promedio es {saco_promedio}")
    elif opcion_recibida==3:
        n1=int(input("ingrese numero "))
        n2=int(input("ingrese numero "))
        multiplo=multiplicacion(n1,n2)
        print(f"la multiplicacion es {multiplo}")
    elif opcion_recibida==4:
        n1=int(input("ingrese numero "))
        n2=int(input("ingrese numero "))
        if n2==0:
            print("no se puede dividir por 0 ")
            n2=int(input("ingrese numero el 0 no esta permitido"))
        else:
            dividor=division(n1,n2)
            print(f"la division es {dividor} ")
    elif opcion_recibida==5:
        mi_arreglo=arr.array('i',[0]*4)
        for i in range(len(mi_arreglo)):
            mi_arreglo[i]=int(input(f"ingrese numero {i+1}"))
        print(f"el arreglo cargado es : {mi_arreglo}")
        


mi_main()        

        


    