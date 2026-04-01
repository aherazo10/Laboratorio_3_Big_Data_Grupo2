# Clasificador de datos de sensores

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
                print("\ndatos registrados:\n")
                for i in range(len(temperatures)):
                    temp = temperatures[i]
                    hum = humidities[i]
                    pres = pressures[i]

                    # Lectura de temperatura
                    if temp < 15:
                        temp_reading = "Frío"
                    elif temp <= 25:
                        temp_reading = "Normal"
                    else:
                        temp_reading = "Caliente"

                    # Lectura de humedad
                    if hum < 30:
                        hum_reading = "Baja"
                    elif hum <= 60:
                        hum_reading = "Media"
                    else:
                        hum_reading = "Alta"

                    # Lectura de presión
                    if pres < 1000:
                        pres_reading = "Baja"
                    elif pres <= 1020:
                        pres_reading = "Media"
                    else:
                        pres_reading = "Alta"

                    print("\nLectura", i+1)
                    print("Temperatura:", temp, "→", temp_reading)
                    print("Humedad:", hum, "% →", hum_reading)
                    print("Presión:", pres, "→", pres_reading)
            case 3:
                print("Saliendo del sistema...")
            case _:
                print("Opción inválida")
data_clasification()