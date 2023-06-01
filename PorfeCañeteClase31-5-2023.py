alumnos = []
cant_alu = int(input('Cuantos alumnos va a cargar en la lista?: '))
for n in range(cant_alu):
    print('Ingrese el nombre del alumno nro: ', n+1)
    nombre = input()
    alumnos.append(nombre)
print(alumnos)