from datetime import datetime
import json

class Venta:
    def __init__(self, id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor):
        self.__id_venta = self.validar_id_venta(id_venta)
        self.__fecha_venta = self.validar_fecha_venta(fecha_venta)
        self.__cliente = cliente
        self.__producto_vendido = producto_vendido
        self.__descripcion = descripcion
        self.__monto = self.validar_monto(monto)
        self.__metodo_pago = metodo_pago
        self.__vendedor = vendedor

    @property
    def id_venta(self):
        return self.__id_venta
    
    @property
    def fecha_venta(self):
        return self.__fecha_venta
    
    @property
    def cliente(self):
        return self.__cliente.capitalize()
    
    @property
    def producto_vendido(self):
        return self.__producto_vendido
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def monto(self):
        return self.__monto
    
    @property
    def metodo_pago(self):
        return self.__metodo_pago.capitalize()
    
    @property
    def vendedor(self):
        return self.__vendedor.capitalize()

    @id_venta.setter
    def id_venta(self, nuevo_id_venta):
        self.__id_venta = self.validar_id_venta(nuevo_id_venta)

    @fecha_venta.setter
    def fecha_venta(self, nueva_fecha_venta):
        self.__fecha_venta = self.validar_fecha_venta(nueva_fecha_venta)

    @cliente.setter
    def cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente

    @producto_vendido.setter
    def producto_vendido(self, nuevo_producto_vendido):
        self.__producto_vendido = nuevo_producto_vendido

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

    @monto.setter
    def monto(self, nuevo_monto):
        self.__monto = self.validar_monto(nuevo_monto)

    @metodo_pago.setter
    def metodo_pago(self, nuevo_metodo_pago):
        self.__metodo_pago = nuevo_metodo_pago

    @vendedor.setter
    def vendedor(self, nuevo_vendedor):
        self.__vendedor = nuevo_vendedor

    def validar_id_venta(self, id_venta):
        try:
            id_venta_num = int(id_venta)
            if id_venta_num <= 0:
                raise ValueError("El ID de venta no puede ser un número negativo o cero.")
            return id_venta_num
        except ValueError as ve:
            print(f"Error del valor del ID: {ve}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def validar_fecha_venta(self, fecha_venta):
        try:
            datetime.strptime(fecha_venta, "%d-%m-%Y")
            return fecha_venta
        except ValueError:
            print("El formato de la fecha debe ser DD-MM-AAAA.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def validar_monto(self, monto):
        try:
            monto_num = float(monto)
            if monto_num <= 0:
                raise ValueError("El monto no puede ser un número negativo o cero.")
            return monto_num
        except ValueError as ve:
            print(f"Error del valor del monto: {ve}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "fecha_venta": self.fecha_venta,
            "cliente": self.cliente,
            "producto_vendido": self.producto_vendido,
            "descripcion": self.descripcion,
            "monto": self.monto,
            "metodo_pago": self.metodo_pago,
            "vendedor": self.vendedor
        }
    
    def __str__(self):
        return (f"ID Venta: {self.id_venta}\n"
                f"Fecha de la venta: {self.fecha_venta}\n"
                f"Cliente: {self.cliente}\n"
                f"Producto vendido: {self.producto_vendido}\n"
                f"Descripción: {self.descripcion}\n"
                f"Monto: {self.monto}\n"
                f"Método de pago: {self.metodo_pago}\n"
                f"Vendedor: {self.vendedor}")

class VentaOnline(Venta):
    def __init__(self, id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, direccion_envio, fecha_envio):
        super().__init__(id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor)
        self.__direccion_envio = direccion_envio
        self.__fecha_envio = fecha_envio

    @property
    def direccion_envio(self):
        return self.__direccion_envio.capitalize()
    
    @property
    def fecha_envio(self):
        return self.__fecha_envio

    @direccion_envio.setter
    def direccion_envio(self, nueva_direccion_envio):
        self.__direccion_envio = nueva_direccion_envio

    @fecha_envio.setter
    def fecha_envio(self, nueva_fecha_envio):
        self.__fecha_envio = self.validar_fecha_envio(nueva_fecha_envio)

    def validar_fecha_envio(self, fecha_envio):
        try:
            datetime.strptime(fecha_envio, "%d-%m-%Y")
            return fecha_envio
        except ValueError:
            print("El formato de la fecha debe ser DD-MM-AAAA.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    
    @staticmethod
    def from_dict(data):
        if 'direccion_envio' not in data or 'fecha_envio' not in data:
            raise KeyError("Faltan datos para crear una instancia de VentaOnline.")
        return VentaOnline(
            id_venta=data["id_venta"],
            fecha_venta=data["fecha_venta"],
            cliente=data["cliente"],
            producto_vendido=data["producto_vendido"],
            descripcion=data["descripcion"],
            monto=data["monto"],
            metodo_pago=data["metodo_pago"],
            vendedor=data["vendedor"],
            direccion_envio=data["direccion_envio"],
            fecha_envio=data["fecha_envio"]
        )

    def to_dict(self):
        data = super().to_dict()
        data["direccion_envio"] = self.direccion_envio
        data["fecha_envio"] = self.fecha_envio
        return data
    
    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Dirección de envio: {self.direccion_envio}\n"
                f"Fecha del envio: {self.fecha_envio}")

class VentaLocal(Venta):
    def __init__(self, id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, direccion_local, localidad):
        super().__init__(id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor)
        self.__direccion_local = direccion_local
        self.__localidad = localidad

    @property
    def direccion_local(self):
        return self.__direccion_local.capitalize()
    
    @property
    def localidad(self):
        return self.__localidad.capitalize()

    @direccion_local.setter
    def direccion_local(self, nueva_direccion_local):
        self.__direccion_local = nueva_direccion_local

    @localidad.setter
    def localidad(self, nueva_localidad):
        self.__localidad = nueva_localidad

    @staticmethod
    def from_dict(data):
        if 'direccion_local' not in data or 'localidad' not in data:
            raise KeyError("Faltan datos para crear una instancia de VentaLocal.")
        return VentaLocal(
            id_venta=data["id_venta"],
            fecha_venta=data["fecha_venta"],
            cliente=data["cliente"],
            producto_vendido=data["producto_vendido"],
            descripcion=data["descripcion"],
            monto=data["monto"],
            metodo_pago=data["metodo_pago"],
            vendedor=data["vendedor"],
            direccion_local=data["direccion_local"],
            localidad=data["localidad"]
        )

    def to_dict(self):
        data = super().to_dict()
        data["direccion_local"] = self.direccion_local
        data["localidad"] = self.localidad
        return data
    
    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Dirección del local: {self.direccion_local}\n"
                f"Localidad: {self.localidad}")

class GestionVentas:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, "r") as file:
                datos = json.load(file)
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado.")
            datos = {}
            self.guardar_datos(datos)
        except json.JSONDecodeError:
            print(f"Error al decodificar JSON en el archivo {self.archivo}.")
            datos = {}
            self.guardar_datos(datos)
        except Exception as e:
            print(f"Error inesperado al leer datos del archivo: {e}")
            datos = {}
        return datos
        
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, "w") as file:
                json.dump(datos, file, indent=4)
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado.")
        except IOError as e:
            print(f"Error al guardar los datos en el archivo {self.archivo}: {e}")
        except Exception as e:
            print(f"Error inesperado al intentar guardar los datos en el archivo {self.archivo}: {e}")

    def agregar_venta(self, venta):
        try:
            datos = self.leer_datos()
            id_venta = venta.id_venta
            if not str(id_venta) in datos.keys():
                datos[id_venta] = venta.to_dict()
                self.guardar_datos(datos)
                print(f"Venta con ID {venta.id_venta} agregada correctamente.")
            else:
                print(f"Ya existe una venta registrada con el ID {id_venta}")
        except Exception as e:
            print(f"Ocurrió un error al intentar agregar la venta: {e}")
    
    def buscar_venta(self, id_venta):
        try:
            datos = self.leer_datos()
            if str(id_venta) in datos:
                venta_data = datos[str(id_venta)]
                if 'direccion_envio' in venta_data:
                    return VentaOnline.from_dict(venta_data)
                elif 'direccion_local' in venta_data:
                    return VentaLocal.from_dict(venta_data)
                else:
                    return Venta.from_dict(venta_data)
            else:
                print("Venta no encontrada.")
        except Exception as e:
            print(f"Ocurrió un error al intentar buscar la venta: {e}")


    def actualizar_venta(self, id_venta, cliente=None, producto_vendido=None, descripcion=None, monto=None, metodo_pago=None, vendedor=None, direccion_envio=None, fecha_envio=None):
        try:
            ventas = self.leer_datos()
            if str(id_venta) in ventas:
                if cliente:
                    ventas[str(id_venta)]['cliente'] = cliente
                if producto_vendido:
                    ventas[str(id_venta)]['producto_vendido'] = producto_vendido
                if descripcion:
                    ventas[str(id_venta)]['descripcion'] = descripcion
                if monto:
                    try:
                        ventas[str(id_venta)]['monto'] = float(monto)
                    except ValueError:
                        print("El monto debe ser un número.")
                        return
                if metodo_pago:
                    ventas[str(id_venta)]['metodo_pago'] = metodo_pago
                if vendedor:
                    ventas[str(id_venta)]['vendedor'] = vendedor
                if direccion_envio:
                    ventas[str(id_venta)]['direccion_envio'] = direccion_envio
                if fecha_envio:
                    ventas[str(id_venta)]['fecha_envio'] = fecha_envio
                
                self.guardar_datos(ventas)
                print("Venta actualizada correctamente.")
            else:
                print("ID de venta no encontrado.")
        except Exception as e:
            print(f"Ocurrió un error al intentar buscar la venta: {e}")


    def eliminar_venta(self, id_venta):
        try:
            datos = self.leer_datos()
            if id_venta in datos.keys():
                datos.pop(id_venta)
                self.guardar_datos(datos)
                print(f"Venta con ID {id_venta} eliminada correctamente.")
            else:
                print(f"No se encontró una venta con el ID {id_venta}")
        except Exception as e:
            print(f"Ocurrió un error al intentar eliminar la venta: {e}")

    def mostrar_todas_las_ventas(self):
        try:
            datos = self.leer_datos()
            if datos:
                for venta in datos.values():
                    print(f"ID Venta: {venta['id_venta']}")
                    print(f"Fecha de la venta: {venta['fecha_venta']}")
                    print(f"Cliente: {venta['cliente']}")
                    print(f"Producto vendido: {venta['producto_vendido']}")
                    print(f"Descripción: {venta['descripcion']}")
                    print(f"Monto: {venta['monto']}")
                    print(f"Método de pago: {venta['metodo_pago']}")
                    print(f"Vendedor: {venta['vendedor']}")
                    if 'direccion_envio' in venta:
                        print(f"Dirección de envio: {venta['direccion_envio']}")
                        print(f"Fecha del envio: {venta['fecha_envio']}")
                    if 'direccion_local' in venta:
                        print(f"Dirección del local: {venta['direccion_local']}")
                        print(f"Localidad: {venta['localidad']}")
                    print('-' * 20)
            else:
                print("No hay ventas registradas.")
        except Exception as e:
            print(f"Ocurrió un error al intentar mostrar todas las ventas: {e}")

