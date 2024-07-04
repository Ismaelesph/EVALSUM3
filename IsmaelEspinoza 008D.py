import os
import time
import random 
import csv

pedidos = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_numero_pedido():
    return random.randint(1, 1000)

def registrar_pedido():
    limpiar_pantalla()
    print("--registro de pedido--")
    num_pedido = generar_numero_pedido()
    nombre = input("nombre del cliente")
    apellido = input("apellido del cliente")
    comuna = input("comuna: ")
    detalle = input("detalle del pedido")
    if nombre and apellido and comuna and detalle:
        pedido = {
            'Numero': num_pedido,
            'Nombre': nombre,
            'apellido': apellido,
            'comuna': comuna,
            'Detalle': detalle
        }
        pedidos.append(pedido)
        print("\nPedido registrado correctamente.")
    else:
        print("\nError: Todos los campos son requeridos.")
    input("\nPresiona enter para continuar...")
    limpiar_pantalla()
    def listar_pedidos():
        limpiar_pantalla()
        print("--listado de pedidos--")
        if pedidos:
            for pedido in pedidos:
                print(f"numero: {pedido ['numero1']}")
                print(f"cliente: {pedido ['nombre']} ¨{pedido ['apellido']}")
                print(f"comuna: {pedido ['comuna']}")
                print(f"detalle: {pedido ['detalle']}")
            else:
                print("No hay pedidos registrados.")
            input("\nPresiona Enter para continuar...")
            limpiar_pantalla()
            def imprimir_hoja_ruta():
                limpiar_pantalla()
                print("-- selecciona de sector para hoja de ruta --")
                sectores = 'sectore A', 'sector B', 'sector C'
                print("sectores disponibles")
                for idx, sector in enumerate(sectores):
                    print(f"{idx + 1}, {sector}")
                seleccion = input("\nSelecciona el numero del sector para generar la hoja de ruta (1-3):")

                try:
                    seleccion = int(seleccion)
                    if seleccion >= 1 and seleccion <=3:
                        print(f"\nGenerando hoja de ruta para {sectores[seleccion - 1]}...")
                        time.sleep(2)
                        print("hoja de ruta generada correctamente.")
                    else:
                        print("seleccion invalida.")
                except ValueError:
                    print("Error: debes ingresar un numero valido,")
                input("\nPresiona Enter para continuar...")
                limpiar_pantalla()
        def main():
            while True:
                print("--- bienvenido a catpremium - sistema de gestion de pedidos ---")
                print("1. registrar pedido")
                print("2. listar pedidos")
                print("3. imprimir hoja de ruta")
                print("4. salir del programa")
                opcion = input ("\nIngrese el numero de la opcion que desea realizar")

                if opcion == '1':
                    registrar_pedido()
                elif opcion == '2':
                    listar_pedidos()
                elif opcion == '3':
                    imprimir_hoja_ruta()
                elif opcion == '4':

                    with open('pedidos.csv' , 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=['numero', 'nombre', 'apellido', 'comuna', 'detalle'])
                    writer.writeheader()
                    writer.writerows(pedidos)
                print("\nGracias por utilizar catpremium hasta luego")
                break
            else:
                print("opcion invalida. por favor, ingrese un numero del 1 al 4.")
                
            time.sleep(1)
            limpiar_pantalla()