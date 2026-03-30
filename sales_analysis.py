# File 1 Analizador de ventas masivas

def main():
    # Aquí empieza todo el programa, lo que se ejecuta primero

    print("\n\t******************************")
    print("\t ANALIZADOR DE VENTAS")
    print("\t******************************")

    products = []
    # Aquí guardamos los nombres de los productos (ejemplo: arroz, pan, etc)

    prices = []
    # Aquí guardamos los precios de esos productos

    stock = []
    # Aquí guardamos cuántos productos se vendieron de cada uno

    option = 0
    # Esto es solo para controlar el menú (qué opción elegirá el usuario)

    while option != 5:
        # Este while hace que el menú se repita hasta que elijan salir (opción 5)

        print("\n1. Registrar venta")
        print("2. Ver total vendido")
        print("3. Ver promedio de ventas")
        print("4. Ver venta más grande")
        print("5. Salir")

        option = int(input("\nElige una opción: "))
        # Le pedimos al usuario una opción y la convertimos a número

        match option:
        # El match es como un if gigante pero más limpio, revisa qué opción eligieron

            case 1:
                # Aquí registramos una venta nueva

                product = input("Producto: ")
                # Nombre del producto

                price = float(input("Precio: "))
                # Precio del producto (decimal)

                quantity = int(input("Cantidad: "))
                # Cuántos se vendieron

                products.append(product)
                # Guardamos el producto en su lista

                prices.append(price)
                # Guardamos el precio

                stock.append(quantity)
                # Guardamos la cantidad

                print("Venta registrada.")

            case 2:
                # Aquí calculamos todo lo que se ha vendido en total

                total = 0
                # Empezamos en 0 porque vamos a ir sumando

                for i in range(len(products)):
                # "i" es la posición (índice) de las listas
                # range(len(products)) crea números desde 0 hasta el tamaño de la lista -1
                # Ejemplo: si hay 3 productos → i será 0, 1, 2

                    total = total + (prices[i] * stock[i])
                    # Aquí pasa lo importante:
                    # prices[i] = precio del producto en la posición i
                    # stock[i] = cantidad vendida de ese mismo producto
                    #
                    # OJO: usamos la misma "i" en todas las listas porque están alineadas
                    # Es decir:
                    # products[0] → arroz
                    # prices[0] → 2.0
                    # stock[0] → 3
                    #
                    # Entonces:
                    # prices[0] * stock[0] = 2.0 * 3 = 6 (venta de arroz)
                    #
                    # Luego eso se suma al total acumulado:
                    # total = total + 6

                print("Total vendido:", total)

            case 3:
                # Aquí sacamos el promedio de ventas

                total = 0
                # Igual que antes, acumulamos todo

                for i in range(len(products)):
                # Recorremos todas las ventas

                    total = total + (prices[i] * stock[i])
                    # Sumamos cada venta

                if len(products) > 0:
                # Verificamos que sí haya ventas (para no dividir entre 0)

                    average = total / len(products)
                    # Total dividido entre cantidad de ventas (promedio)

                    print("Promedio de ventas:", average)
                else:
                    print("No hay ventas registradas.")

            case 4:
                # Aquí buscamos cuál fue la venta más grande

                max = 0
                # Aquí guardamos la venta más alta encontrada

                max_product = ""
                # Aquí guardamos el nombre del producto con mayor venta

                for i in range(len(products)):
                # Recorremos todas las ventas

                    sale = prices[i] * stock[i]
                    # Calculamos cuánto se vendió de ese producto

                    if sale > max:
                    # Si esta venta es más grande que la anterior

                        max = sale
                        # Guardamos el nuevo valor máximo

                        max_product = products[i]
                        # Guardamos el nombre del producto

                print("Venta más grande:")
                print(max_product, "=", max)

            case 5:
                # Aquí simplemente salimos del programa
                print("Saliendo del sistema...")

            case _:
                # Si ponen algo raro o inválido
                print("Opción inválida sea serio y eliga entre 1 al 51")


main()
# Esto ejecuta todo el programa