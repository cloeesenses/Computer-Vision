from funciones import registrar_nuevo_perfil, acceder_hogar


# Muestra el menú principal del sistema
def mostrar_menu():
    print("\nSistema de reconocimiento facial para hogares inteligentes")
    print("=" * 60)
    print("1. Registrar nuevo perfil")
    print("2. Acceder al hogar")
    print("3. Salir")


# Ejecuta el programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_nuevo_perfil()

        elif opcion == "2":
            acceder_hogar()

        elif opcion == "3":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()