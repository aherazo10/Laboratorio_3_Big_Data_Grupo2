def main():
    print("\n===== PROCESADOR DE LOGS =====")

    tipos_logs = ["INFO", "ERROR", "WARNING"]

    conteo = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    logs = []

    n = int(input("¿Cuántos logs desea ingresar? "))

    for i in range(n):
        log = input(f"Ingrese log {i+1}: ")
        logs.append(log)

    for log in logs:

        log = log.lower() 

        match True:
            case _ if log.startswith("info"):
                conteo["INFO"] += 1

            case _ if log.startswith("error"):
                conteo["ERROR"] += 1

            case _ if log.startswith("warning"):
                conteo["WARNING"] += 1

    print("\n===== RESULTADOS =====")
    for tipo in tipos_logs:
        print(tipo, ":", conteo[tipo])


main()