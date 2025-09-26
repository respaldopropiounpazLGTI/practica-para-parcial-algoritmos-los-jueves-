"""3.1.Realizar un programa que cargue un vector de 15 posiciones."""
import array as arr
mi_arreglo=arr.array('i',[0]*15)
print("mi arreglo sin cargar ",mi_arreglo)
for i in range(len(mi_arreglo)):
    mi_arreglo[i]=int(input(f"ingrese numero {i+1} : "))
print(f"mi arreglo cargado {mi_arreglo}")    
print(len(mi_arreglo))
