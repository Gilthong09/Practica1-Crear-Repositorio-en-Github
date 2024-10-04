import msvcrt
import os


continuar = True
diccionario_est = {}
lista_est = [{"nombre": "Juan", "matricula": "1", "edad": 20, "sexo": "1", "altura": 160.0, "peso": 130.0},
             {"nombre": "María", "matricula": "2", "edad": 22,
                 "sexo": "1", "altura": 150.0, "peso": 120.0},
             {"nombre": "Carlos", "matricula": "3", "edad": 21,
                 "sexo": "1", "altura": 170.0, "peso": 130.0}
             ]
while (continuar):
    os.system('cls')
    opción = input("""
                   Bienvenidos al programa para gestionar estudiantes. Ingrese la opcion que desee
                   

                   1. Agregar
                   2. Buscar  
                   3. Modificar
                   4. Eliminar
                   x. Salir
                   
                   
                   """)

    match opción:
        case "1":
            os.system('cls')
            num = int(input(
                "Bienvenido a la sección de agregar estudiantes. Cuantos estudiantes desea agregar?"))

            for i in range(num):
                diccionario_est["nombre"] = input(
                    "Ingrese el nombre del estudiante: ")
                diccionario_est["matricula"] = input(
                    "Ingrese la matricula del estudiante: ")
                diccionario_est["edad"] = int(
                    input("Ingrese la edad del estudiante: "))
                diccionario_est["sexo"] = input(
                    "Ingrese el sexo del estudiante. 1 si es varon y 0 si es hembra: ")
                diccionario_est["altura"] = float(
                    input("Ingrese la altura del estudiante: "))
                diccionario_est["peso"] = float(
                    input("Ingrese el peso del estudiante: "))

                lista_est.append(diccionario_est)

            print(lista_est)

        case "2":
            os.system('cls')
            bus = input(
                "Ingrese la matricula del estudiante que quiere buscar")

            for e in lista_est:

                if bus == e["matricula"]:
                    print(f"""
                    Matricula: {e["matricula"]}
                    Nombre: {e["nombre"]}
                    Edad: {e["edad"]}
                    Sexo: {e["sexo"]}
                    Altura: {e["altura"]}
                    Peso: {e["peso"]}



                    """)
            else:
                print("El estudiante que esta buscando no existe aquí")
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
            print("Continuando...")
        case "3":
            os.system('cls')
            modi = input(
                "Ingrese la matricula del estudiante que quiere modificar")

            for m in lista_est:

                if modi == m["matricula"]:

                    posible = ""

                    print(f"""El nombre actual es {
                          m["nombre"]} escriba el nuevo o precione enter para continuar""")
                    posible = input("Digite el nombre: ")
                    if len(posible) > 0:
                        m["nombre"] = posible

                    print(f"""La matricula actual es {
                          m["matricula"]} escriba la nueva o precione enter para continuar""")
                    posible = input("Digite la matricula: ")
                    if len(posible) > 0:
                        m["matricula"] = posible

                    print(f"""La edad actual es {
                          m["edad"]} escriba la nueva o precione enter para continuar""")
                    posible = input("Digite la edad: ")
                    if len(posible) > 0:
                        m["edad"] = int(posible)

                    print(f"""La altura actual es {
                          m["altura"]} escriba la nueva o precione enter para continuar""")
                    posible = input("Digite la altura: ")
                    if len(posible) > 0:
                        m["altura"] = float(posible)

                    print(f"""El peso actual es {
                          m["peso"]} escriba el nuevo o precione enter para continuar""")
                    posible = input("Digite el peso: ")
                    if len(posible) > 0:
                        m["edad"] = float(posible)

                    print(f"""El sexo actual es {
                          m["sexo"]} escriba el nuevo o precione enter para continuar""")
                    posible = input("Digite el sexo: ")
                    if len(posible) > 0:
                        m["nombre"] = posible

                    print("El estudiante fue modificado con exito...")
                    print("Presione cualquier tecla para continuar...")
                    msvcrt.getch()
                    print("Continuando...")
        case"4":

            modi = input(
                "Ingrese la matricula del estudiante que quiere eliminar")
            for r in lista_est:

                if modi == r["matricula"]:
                    lista_est.remove(r)

                    print("El estudiante fue eliminado con exito...")
                    print("Presione cualquier tecla para continuar...")
                    msvcrt.getch()
                    print("Continuando...")

        case"x":
            break
