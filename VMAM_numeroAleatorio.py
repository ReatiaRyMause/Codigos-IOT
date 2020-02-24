import random
class sacarnumero:
    def comparar(nu):
        print ("INGRESE NÚMERO 1-10")
        nu=input("¿CUÁL ES SU NÚMERO?: ")
        nu = int(nu)
        numale=random.randrange(10)
        if(nu > numale):
            print("El número mayor es el ingresado por el usuario: " + str (nu))
            print("Numero RANDOM: " + str(numale))
        if(nu < numale):
            print("El número mayor es el RANDOM: " + str (numale))
            print("Numero usuario: " + str(nu))
        if(nu == numale):
            print("Los dos números son iguales: " + str (numale) +" " + str (nu))
        
obtener = sacarnumero()
obtener.comparar()
