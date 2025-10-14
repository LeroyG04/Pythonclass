# #Definir un diccionario llamado persona
# persona = {
#     "nombre": "Ana",
#     "edad": 22,
#     "ciudad": "Guadalajara"
# }
# print(type(persona))#Nos indica el tipo de dato de una variable

# print(persona["nombre"])  # Ana
# print(persona["edad"])    # 22
# print(persona["ciudad"])  # Guadalajara

# #Añadir dos nuevos pares clave-valor
# persona["profesion"] = "Ingeniera"
# persona["pais"] = "Mexico"
# print(persona)

# #Modificar el valor de una clave existente
# persona["edad"] = 23
# print(persona)

# #Eliminar un par clave-valor
# del persona["ciudad"]
# print(persona)

# #crear otro diccionario y agregar ambos a una lista
# persona2 = {
#     "nombre": "Luis",
#     "edad": 30,
#     "ciudad": "Monterrey",
#     "profesion": "Doctor",
#     "pais": "Mexico"
# }
# #Lista de diccionarios
# personas=[persona, persona2]
# print(personas)
alumnos=[]
def agregar_alumno():

    nombre = input("Inserte el nombre del alumno: ")
    edad= int(input("Inserte la edad del alumno: "))
    carrera= input("Inserte carrera del alumno: ")

    alumno = {
        "Nombre": nombre,
        "Edad": edad,
        "Carrera": carrera
    }
    alumnos.append(alumno)
    print(f"Alumno {nombre} agregado")

    
for _ in range (3):
        agregar_alumno()


print("Lista de alumnos agregados")
print(alumnos)