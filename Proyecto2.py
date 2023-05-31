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
        si = input('¿Cuantas respondio por si?         ')
        no = input('¿Cuantas respondio por no?      ')

        if((si + no)== 4):
            cant = si + no  
        si = 0
        no = 0
        sigue = input('Sigue encuestando?  Si = 1      ') 
    print('Total de encuestados',i,':',cant)
    total = total + cant
print('Total de encuestados:', total)

