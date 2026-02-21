estudiantes = []
print("#-------------------------------#")
print("#--| registro de estudiantes |--#")
print("#-------------------------------#")
while True:
    nombre = input("ingresa el nombre del estudiante (o escribe 'salir' para finalizar): ")
    if nombre.lower() == "salir":
        break
    estudiantes.append(nombre)
    print("estudiante registrado correctamente.\n")
print("\n=== lista de estudiantes registrados ===")
if len(estudiantes) == 0:
    print("no se registraron estudiantes.")
else:
    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"{i}. {estudiante}")