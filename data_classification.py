def data_clasification():

    print("\n******************************")
    print(" CLASIFICADOR DE SENSORES ")
    print("******************************")

    temperatures = []
    humidities = []
    pressures = []

    option = 0

    while option != 3:

        print("\n1. Registrar datos")
        print("2. Ver datos registrados")
        print("3. Salir")

        option = int(input("\nElige una opción: "))

        match option:

            case 1:

                temp = float(input("Temperatura: "))
                hum = float(input("Humedad: "))
                pres = float(input("Presión: "))

                temperatures.append(temp)
                humidities.append(hum)
                pressures.append(pres)

                print("datos registrada.")
                
            case 2: