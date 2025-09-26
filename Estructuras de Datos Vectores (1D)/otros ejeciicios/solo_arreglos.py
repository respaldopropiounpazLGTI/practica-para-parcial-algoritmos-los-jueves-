import array as arr
mi_arreglo=arr.array('i',[0]*6)
print(mi_arreglo)
for i in range(len(mi_arreglo)):
    mi_arreglo[i]=int(input(f"ingrese numero {i+1} : "))
print(mi_arreglo)    