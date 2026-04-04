def main():
   
    numbers = []
 


    option = 0


    while option != 6:
   
        print("\n--- MENÚ ---")
        print("1. Ingresar número")
        print("2. Ver promedio de valores")
        print("3. Ver valor máximo")
        print("4. Ver valor mínimo")
        print("5. Ver cantidad de valores introducidos")
        print("6. Salir")


        option = int(input("Elige una opción: "))


        match option:


            case 1:
                num = float(input("Ingresa un número: "))
                numbers.append(num)
                print("Número agregado.")


            case 2:
                if len(numbers) > 0:
                    average = sum(numbers) / len(numbers)
                    print("Promedio:", average)
                else:
                    print("No hay datos.")


            case 3:
                if len(numbers) > 0:
                    print("Máximo:", max(numbers))
                else:
                    print("No hay datos.")


            case 4:
                if len(numbers) > 0:
                    print("Mínimo:", min(numbers))
                else:
                    print("No hay datos.")


            case 5:
                print("Cantidad de datos:", len(numbers))


            case 6:
                print("Saliendo del programa...")


            case _:
                print("Opción inválida")






main()
