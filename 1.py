def suma(n1,n2,n3):
    return n1+n2+n3

def resta(n1,n2,n3):
    return (n1-n2)-n3

def promedio(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    return promedio
    



def menu():
    print("****** menu *********")
    print("1 para suma ")
    print("2 para restar")
    print("3 para multiplicar  ")
    print("4 para dividir")
    print("5 para promedio ")
    print("6 para salir ")
    opcion=int(input("que desea hacer  "))
    return opcion

def cargar_numeros():
    n1=int(input("ingrese numero "))
    n2=int(input("ingrese numero "))
    n3=int(input("ingrese numero "))
    return n1,n2,n3

def multiplico(n1,n2,n3):
    return n1*n2*n2

    
def main():
    while True:
        opcion_recibida=menu()
        print(opcion_recibida)
        if opcion_recibida==1:
         n1,n2,n3=cargar_numeros()
         sumando=suma(n1,n2,n3)
         print(f"el resultado de suma es : {sumando} ")
        elif  opcion_recibida==2:
         n1,n2,n3=cargar_numeros()
         restando=resta(n1,n2,n3)
         print(f"la resta es {restando}")
        elif opcion_recibida==5:
         n1,n2,n3=cargar_numeros()
         promediando=promedio(n1,n2,n3)
         print(f"el promedio es {promediando}")
        elif opcion_recibida==3:
            n1,n2,n3=cargar_numeros()
            multiplicando=multiplico(n1,n2,n3)
            print(f"la multiplicacion es {multiplicando}")
        elif opcion_recibida==4:
            numero1=int(input("ingrese primer valor "))
            numero2=int(input("ingrese segundo valor "))
            while numero2==0:
                print("no se puede dividir por 0")
                numero2=int(input("ingrese numero 0 no admitido!!"))
            division=numero1/numero2
            print(f"la division es {division}")
        elif opcion_recibida==6:
            print("gracias por utilizar el programa ")
            break    
      
   
        
    
        

        
    
        
       
       
        

main()