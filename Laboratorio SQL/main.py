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
    """Solicita al usuario información para agregar una venta."""
    while True:
        try:
            id_venta = int(input("ID de la venta: "))
            if gestion_ventas.buscar_venta(id_venta): 
                print(f"Error: La venta con ID {id_venta} ya existe. Por favor, elige un ID diferente.")
                continue
            break
        except ValueError:
            print("Error: El ID de la venta debe ser un número entero. Por favor, ingrese de nuevo.")

    while True:
        fecha_venta = input("Fecha de la venta (AAAA-MM-DD): ")
        if Venta.validar_fecha_venta(None, fecha_venta):
            break
        else:
            print("Por favor, ingrese de nuevo en formato (AAAA-MM-DD).")

    cliente = input("Cliente: ")
    producto_vendido = input("Producto vendido: ")
    descripcion = input("Descripción: ")

    while True:
        try:
            monto = float(input("Monto: "))
            break
        except ValueError:
            print("Error: El monto debe ser un número. Por favor, ingrese de nuevo.")

    metodo_pago = input("Método de pago: ")
    vendedor = input("Vendedor: ")

    es_venta_online = input("¿Venta online o Venta local? (1/2): ") == '1'

    if es_venta_online:
        direccion_envio = input("Dirección de envío: ")
        while True:
            fecha_envio = input("Fecha de envío (AAAA-MM-DD): ")
            if Venta.validar_fecha_venta(None, fecha_envio):
                break
            else:
                print("Error: El formato de la fecha debe ser AAAA-MM-DD. Por favor, ingrese de nuevo.")

        venta = VentaOnline(id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, direccion_envio, fecha_envio)
    else:
        direccion_local = input("Dirección del local: ")
        localidad = input("Localidad: ")

        venta = VentaLocal(id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, direccion_local, localidad)

    gestion_ventas.agregar_venta(venta)

def buscar_venta(gestion_ventas):
    id_venta = input("ID de la venta a buscar: ")
    venta = gestion_ventas.buscar_venta(id_venta)
    if venta:
        print(venta)
    else:
        print(f"La venta con ID {id_venta} no existe en la base de datos.")

def actualizar_venta(gestion_ventas):
    id_venta = input("ID de la venta a actualizar: ")

    if not id_venta.isdigit():
        print("El ID de la venta debe ser un número entero.")
        return

    nueva_fecha_venta = input("Nueva fecha de venta (YYYY-MM-DD, presiona Enter para omitir): ") or None
    nuevo_cliente = input("Nuevo cliente (presiona Enter para omitir): ") or None
    nuevo_producto_vendido = input("Nuevo producto vendido (presiona Enter para omitir): ") or None
    nueva_descripcion = input("Nueva descripción (presiona Enter para omitir): ") or None
    nuevo_monto_input = input("Nuevo monto (presiona Enter para omitir): ") or None

    nuevo_monto = float(nuevo_monto_input) if nuevo_monto_input and nuevo_monto_input.replace('.', '', 1).isdigit() else None

    nuevo_metodo_pago = input("Nuevo método de pago (presiona Enter para omitir): ") or None
    nuevo_vendedor = input("Nuevo vendedor (presiona Enter para omitir): ") or None

    es_venta_online = input("¿Venta online o Venta local? (1/2): ") == '1'
    
    if es_venta_online:
        nueva_direccion_envio = input("Nueva dirección de envío (presiona Enter para omitir): ") or None
        nueva_fecha_envio = input("Nueva fecha de envío (presiona Enter para omitir): ") or None

        gestion_ventas.actualizar_venta(
            id_venta,
            nueva_fecha_venta,
            nuevo_cliente,
            nuevo_producto_vendido,
            nueva_descripcion,
            nuevo_monto,
            nuevo_metodo_pago,
            nuevo_vendedor,
            direccion_envio=nueva_direccion_envio,
            fecha_envio=nueva_fecha_envio
        )
    else:
        nueva_direccion_local = input("Nueva dirección del local (presiona Enter para omitir): ") or None
        nueva_localidad = input("Nueva localidad (presiona Enter para omitir): ") or None

        gestion_ventas.actualizar_venta(
            id_venta,
            nueva_fecha_venta,
            nuevo_cliente,
            nuevo_producto_vendido,
            nueva_descripcion,
            nuevo_monto,
            nuevo_metodo_pago,
            nuevo_vendedor,
            direccion_local=nueva_direccion_local,
            localidad=nueva_localidad
        )

def eliminar_venta(gestion_ventas):
    id_venta = input("ID de la venta a eliminar: ")

    if not id_venta.isdigit():
        print("Error: ID de venta debe ser un número entero")
        return
    
    gestion_ventas.eliminar_venta(id_venta)

def mostrar_todas_las_ventas(gestion_ventas):
    try:
        ventas = gestion_ventas.mostrar_todas_las_ventas()
        if not ventas:
            print("No hay ventas registradas")
            return

        for venta in ventas:
            print('=' * 30)
            print(venta)

    except Exception as e:
        print(f"Error al mostrar las ventas: {e}")

def main():
    gestion_ventas = GestionVentas()

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
            confirmacion = input("¿Estás seguro de que deseas salir? (S/N): ").lower()
            if confirmacion == 's':
                print("Saliendo del programa.")
                break

        else:
            print("Opción inválida. Por favor, elige una opción válida.")

        input("Presiona Enter para continuar...")
        limpiar_consola()

if __name__ == "__main__":
    main()

