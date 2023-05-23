max=[]
min=[]
temp_min = int
temp_max = int
pos_min = int
pos_max = int
prom=0


for i in range(28):
    max.append(int(input('Ingrese la temperatura maxima de hoy   ')))

    min.append(int(input('Ingrese la temperatura minima de hoy   ')))

    prom= prom + (min[i]+max[i])/2
    print('La temperatura promedio del dia fue  ', prom)
    prom = 0

temp_max=1
temp_min=99

for i in range(28):
    if(min[i]<temp_min):
    
        temp_min=min[i]
        pos_min=i

    if(max[i]>temp_max):
        temp_max=max[i]
        pos_max=i

print('La temperatura minima del mes fue:',pos_min)
print('La temperatura maxima del mes fue:',pos_max)

    



#for i in range(len(max)):
#    prom = prom + max[i]
#print('El promedio es = ',str(prom/len(max)))




#for i in range(len(a)):
#    c.append(int(input('ingrese un valor   ')))
#print(c)

#for i in range(len(a)):
#    prom=prom + c[i]
#print('el promedio es =  ',str(prom/len(c)))