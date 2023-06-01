#int total=0, si,no,i,cant,sigue
total = 0
si = int
no = int
i = int
cant = int             
sigue = 1

for i in range(5):
    si = 0
    no = 0
    cant = 0
    sigue = 1
    while sigue == 1:
        si = int(input('¿Cuantas respondio por si?         '))
        no = int(input('¿Cuantas respondio por no?      '))

        if((si + no)):
            cant = si + no
            print(cant)  
        si = 0
        no = 0
        sigue = int(input('Sigue encuestando?  Si = 1      ')) 
    print('Total de encuestados en la ciudad Numero:',i+1,':',cant)
    total = total + cant
print('Total de encuestados entre todas las ciudades:', total)

