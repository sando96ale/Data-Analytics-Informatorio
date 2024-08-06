import os 
import platform
from sistema_gestion_ventas import Venta, GestionVentas, VentaOnline, VentaLocal

def limpiar_consola():
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def agregar_venta(gestion_ventas):
    while True:
        try:
            id_venta = input("ID de la venta: ")
            id_venta = int(id_venta)
            break
        except ValueError:
            print("Error: El ID de la venta debe ser un número entero. Por favor, ingrese de nuevo.")

    while True:
        fecha_venta = input("Fecha de la venta (DD-MM-AAAA): ")
        if Venta.validar_fecha_venta(None, fecha_venta):
            break
        else:
            print("Por favor, ingrese de nuevo en formato (DD-MM-AAAA).")

    cliente = input("Cliente: ")
    producto_vendido = input("Producto vendido: ")
    descripcion = input("Descripción: ")

    while True:
        try:
            monto = input("Monto: ")
            monto = float(monto)
            break
        except ValueError:
            print("Error: El monto debe ser un número. Por favor, ingrese de nuevo.")

    metodo_pago = input("Método de pago: ")
    vendedor = input("Vendedor: ")

    es_venta_online = input("¿Venta online o Venta local? (1/2): ") == '1'
    if es_venta_online:
        direccion_envio = input("Dirección de envío: ")
        while True:
            fecha_envio = input("Fecha de envío (DD-MM-AAAA): ")
            if Venta.validar_fecha_venta(None, fecha_envio):
                break
            else:
                print("Error: El formato de la fecha debe ser DD-MM-AAAA. Por favor, ingrese de nuevo.")

        venta = VentaOnline(id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, direccion_envio, fecha_envio)
    else:
        direccion_local = input("Dirección del local: ")
        localidad = input("Localidad: ")

        venta = VentaLocal(id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, direccion_local, localidad)

    gestion_ventas.agregar_venta(venta)
    print("Venta agregada correctamente.")


def buscar_venta(gestion_ventas):
    id_venta = input("ID de la venta a buscar: ")
    venta = gestion_ventas.buscar_venta(id_venta)
    if venta:
        print(venta)
    else:
        print("Venta no encontrada.")

def actualizar_venta(gestion_ventas):
    id_venta = input("ID de la venta a actualizar: ")
    nuevo_cliente = input("Nuevo cliente (presiona Enter para omitir): ")
    nuevo_producto_vendido = input("Nuevo producto vendido (presiona Enter para omitir): ")
    nueva_descripcion = input("Nueva descripción (presiona Enter para omitir): ")
    nuevo_monto = input("Nuevo monto (presiona Enter para omitir): ")
    nuevo_metodo_pago = input("Nuevo método de pago (presiona Enter para omitir): ")
    nuevo_vendedor = input("Nuevo vendedor (presiona Enter para omitir): ")

    es_venta_online = input("¿Venta online o Venta local? (1/2): ") == '1'
    if es_venta_online:
        nueva_direccion_envio = input("Nueva dirección de envío (presiona Enter para omitir): ")
        nueva_fecha_envio = input("Nueva fecha de envío (presiona Enter para omitir): ")
        gestion_ventas.actualizar_venta(id_venta, nuevo_cliente, nuevo_producto_vendido, nueva_descripcion, nuevo_monto, nuevo_metodo_pago, nuevo_vendedor, nueva_direccion_envio, nueva_fecha_envio)
    else:
        nueva_direccion_local = input("Nueva dirección del local (presiona Enter para omitir): ")
        nueva_localidad = input("Nueva localidad (presiona Enter para omitir): ")
        gestion_ventas.actualizar_venta(id_venta, nuevo_cliente, nuevo_producto_vendido, nueva_descripcion, nuevo_monto, nuevo_metodo_pago, nuevo_vendedor, nueva_direccion_local, nueva_localidad)

def eliminar_venta(gestion_ventas):
    id_venta = input("ID de la venta a eliminar: ")
    gestion_ventas.eliminar_venta(id_venta)

def mostrar_todas_las_ventas(gestion_ventas):
    gestion_ventas.mostrar_todas_las_ventas()

def main():
    archivo = "ventas.json"
    gestion_ventas = GestionVentas(archivo)

    while True:
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║                     SISTEMA DE GESTIÓN DE VENTAS                     ║")
        print("╠══════════════════════════════════════════════════════════════════════╣")
        print("║   1. Agregar una nueva venta                                         ║")
        print("║   2. Buscar venta por ID                                             ║")
        print("║   3. Actualizar información de una venta                             ║")
        print("║   4. Eliminar una venta                                              ║")
        print("║   5. Mostrar todas las ventas                                        ║")
        print("║   6. Salir del sistema                                               ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_venta(gestion_ventas)

        elif opcion == "2":
            buscar_venta(gestion_ventas)

        elif opcion == "3":
            actualizar_venta(gestion_ventas)

        elif opcion == "4":
            eliminar_venta(gestion_ventas)

        elif opcion == "5":
            mostrar_todas_las_ventas(gestion_ventas)

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, elige una opción válida.")

        input("Presiona Enter para continuar...")
        limpiar_consola()

if __name__ == "__main__":
    main()

