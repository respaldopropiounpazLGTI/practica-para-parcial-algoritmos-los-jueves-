import array as arr
mi_arreglo=arr.array('i',[0]*5)
print(mi_arreglo)
print(len(mi_arreglo))
for i in range(len(mi_arreglo)):
    mi_arreglo[i]=int(input(f"ingrese valor {i+1} :"))
    
suma_arreglo=sum(mi_arreglo)
cantidad_de_arreglo=len(mi_arreglo)
promedio=suma_arreglo/cantidad_de_arreglo 
print(f"la suma es {suma_arreglo}")
print(f"la cantidad de elementos del arreglo es {cantidad_de_arreglo}")  
print(f"y el promedio es {promedio} ") #me jajaj que rata 

numero_pares=[numero for numero in mi_arreglo if numero %2==0]#jajajaja
numero_inpares=[numero for numero in mi_arreglo  if numero %2!=0]# jajaja
suma_de_numeros_pares=sum(numero_pares)
suma_de_numeros_inpares=sum(numero_inpares)
print(f"la suma de pares es :{suma_de_numeros_pares} ")
print(f" la suma de numeros inpares e : {suma_de_numeros_inpares}") 
#esto es experimental 
cantidad_pares=len(numero_pares)
cantidad_inpares=len(numero_inpares)
promedio_de_pares_a_inpares=cantidad_pares/cantidad_inpares
promedio_de_inpares_a_pares=cantidad_inpares/cantidad_pares
print(f"prmedio de solo numeros pares {promedio_de_inpares_a_pares} ")
print(f"promedio de solo numero inpares {promedio_de_pares_a_inpares}")