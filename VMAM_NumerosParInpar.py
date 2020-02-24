class numparinpar:
    def calcular(self):
        print ("CALCULAR NUMERO PAR - INPAR")
        num=input("¿CUÁL ES SU NÚMERO?: ")
        num = int(num)
        if((num%2) == 0):
            print("El numero " + str(num) + " es par.")
        else:
            print("El numero " + str(num) + " es inpar.")

obtener = numparinpar()
obtener.calcular()
