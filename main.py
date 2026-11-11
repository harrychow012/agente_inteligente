
from memoria import cargar_memoria
from diagnostico import diagnosticar, mostrar_estadisticas


def main():
    memoria = cargar_memoria()

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Diagnosticar una falla")
        print("2. Consultar memoria y estadísticas")
        print("3. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            diagnosticar(memoria)
        elif opcion == "2":
            mostrar_estadisticas(memoria)
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma detenido.")
