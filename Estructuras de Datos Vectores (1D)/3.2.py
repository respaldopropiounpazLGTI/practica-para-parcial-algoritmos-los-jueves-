"""Desarrollar un algoritmo que permita la carga de un vector de 10 posiciones.
Generar una rutina que transcriba el contenido del vector a otro vector en orden
inverso."""
import array as arr
mi_arreglo=arr.array('i',[0]*10)
mi_segundo_arreglo=arr.array('i',[0]*10)
for i in range(len(mi_arreglo)):
    mi_arreglo[i]=int(input(f"ingrese valor {i+1} : " ))
    
mi_segundo_arreglo=mi_arreglo[::-1]
     
print(mi_arreglo) 
print(mi_segundo_arreglo)      