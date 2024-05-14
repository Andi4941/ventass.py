def crear_informe_ventas(ventas):
    try:
        with open("informe_ventas.txt", "w") as archivo:
            for producto, cantidad in ventas.items():
                archivo.write(f"{producto}:{cantidad}\n")
    except IOError:
        print("Error al escribir en el archivo.")
    except Exception as e:
        print("Ocurrió un error:", e)
    finally:
        print("Informe de ventas guardado.")

def main():
    productos = {
        "pan ciabatta": 2000,
        "pie de limon": 3500,
        "cafe": 2200,
        "te": 1600,
        "alfajor": 1000
    }
    ventas = {}
    total_ventas = 0
    for producto, precio in productos.items():
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                ventas[producto] = cantidad
                total_ventas += cantidad * precio
                break
            except ValueError as ve:
                print(ve)
            except Exception as e:
                print("Ocurrió un error:", e)
    print("\nInforme de ventas:")
    for producto, cantidad in ventas.items():
        print(f"{producto}: {cantidad}")
    print(f"Total de ventas del día: ${total_ventas}")

    crear_informe_ventas(ventas)

if __name__ == "__main__":
    main()