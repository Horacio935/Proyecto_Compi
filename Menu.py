import subprocess
import webbrowser

def menu():
    while True:
        print("\nMenu Principal")
        print("1. Analizador Lexico")
        print("2. Analizador Sintactico")
        print("3. Arbol Sintactico")
        print("4. Tabla de simbolos")
        print("5. Bitacoras")
        print("6. Arbol Sintactico")
        print("7 Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ejecutar_archivo('lexico.py')
        elif opcion == '2':
            ejecutar_archivo('sintactico.py')
        elif opcion == '3':
            ejecutar_archivo('sintactico2.py')
        elif opcion == '4':
            submenu_tabla_simbolos()
        elif opcion == '5':
            submenu_bitacoras()
        elif opcion == '6':
            abrir_html('AST.html')
            break
        elif opcion == '7':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def ejecutar_archivo(nombre_archivo):
    try:
        subprocess.run(['python', nombre_archivo], check=True)
    except subprocess.CalledProcessError:
        print(f"Hubo un error al ejecutar {nombre_archivo}.")
    volver_al_menu()

def abrir_html(nombre_archivo):
    try:
        webbrowser.open(nombre_archivo)
    except Exception as e:
        print(f"Hubo un error al abrir {nombre_archivo}: {e}")
    volver_al_menu()

def submenu_tabla_simbolos():
    while True:
        print("\nSubmenú Tabla de Símbolos")
        print("1. Tabla de simbolos")
        print("2. Tabla de simbolos variables")
        print("3. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            abrir_html('tabla_simbolos.html')
        elif opcion == '2':
            abrir_html('tabla_simbolos_variables.html')
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def submenu_bitacoras():
    while True:
        print("\nSubmenú de Bitacoras")
        print("1. Bitácora de Errores Léxico")
        print("2. Bitácora de Errores Sintáctico")
        print("3. Bitácora de Tokens")
        print("4. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            abrir_html('bitacora_errores.html')
        elif opcion == '2':
            abrir_html('bitacora_errores_sin.html')
        elif opcion == '3':
            abrir_html('bitacora_tokens.html')
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def volver_al_menu():
    input("\nPresiona Enter para volver al menú principal...")

if __name__ == "__main__":
    menu()
