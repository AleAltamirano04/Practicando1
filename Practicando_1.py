i = int
temp_min = int
temp_max = int
min = []
max = []
pos_min = int
pos_max = int
prom = []

for i in range(1,29):
    print('Ingrese la temperatura maxima del dia de hoy')
    max = input()
    print('Ingrese la temperatura mininma del dia de hoy')
    min = input()

    prom=(min+max)/2
    print('El promedio de temperatura maxima es:')
    print(prom)
    

