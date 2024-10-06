from datetime import datetime, date
import mysql.connector
from mysql.connector import Error
from decouple import config

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
        if isinstance(fecha_venta, (datetime, date)):
            return fecha_venta
        else:
            try:
                fecha = datetime.strptime(fecha_venta, "%Y-%m-%d")
                return fecha
            except ValueError:
                print("El formato de la fecha debe ser AAAA-MM-DD.")
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
        if isinstance(self.fecha_venta, (datetime, date)):
            fecha_venta_str = self.fecha_venta.strftime("%Y-%m-%d")
        else:
            fecha_venta_str = 'No disponible'
        return (f"ID Venta: {self.id_venta}\n"
                f"Fecha de la venta: {fecha_venta_str}\n"
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
            datetime.strptime(fecha_envio, "%Y-%m-%d")
            return fecha_envio
        except ValueError:
            print("El formato de la fecha debe ser AAAA-MM-DD.")
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
    def __init__(self):
        try:
            self.host = config('DB_HOST')
            self.database = config('DB_NAME')
            self.user = config('DB_USER')
            self.password = config('DB_PASSWORD')
            self.port = config('DB_PORT')
        except KeyError as e:
            raise Exception(f"Falta la configuración de la base de datos: {e}")

    def connect(self):
        '''Establece una conexion con la base de datos'''
        try:
            connection = mysql.connector.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password,
                port = self.port
            )

            if connection.is_connected():
                return connection
            else:
                raise Error('Error al conectar a la base de datos.')
        
        except mysql.connector.InterfaceError:
            print(f"Error de conexión al servidor.")
            return None
        except mysql.connector.ProgrammingError:
            print(f"Error de autenticación: Usuario o contraseña incorrectos.")
            return None
        except mysql.connector.DatabaseError:
            print(f"Error en la base de datos. Verifique la configuración.")
            return None
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        except Exception as ve:
            print(f"Error inesperado: {ve}")
            return None

    def agregar_venta(self, venta):
        """Agrega una venta a la base de datos."""
        connection = self.connect()
        if not connection:
            return False

        try:
            with connection.cursor() as cursor:
                # Verifica si el id_venta existe.
                cursor.execute("SELECT id_venta FROM ventas WHERE id_venta = %s", (venta.id_venta,))
                if cursor.fetchone():
                    print(f"La venta con ID {venta.id_venta} ya existe.")
                    return False
                
                # Inserta la venta principal.
                venta_query = '''
                INSERT INTO ventas (id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(venta_query, (venta.id_venta, venta.fecha_venta, venta.cliente, venta.producto_vendido, 
                                            venta.descripcion, venta.monto, venta.metodo_pago, venta.vendedor))
                    
                # Inserta la venta según el tipo.
                if isinstance(venta, VentaOnline):
                    query = '''
                    INSERT INTO ventaonline (id_venta, direccion_envio, fecha_envio)
                    VALUES (%s, %s, %s)
                    '''
                    cursor.execute(query, (venta.id_venta, venta.direccion_envio, venta.fecha_envio))

                elif isinstance(venta, VentaLocal):
                    query = '''
                    INSERT INTO ventalocal (id_venta, direccion_local, localidad)
                    VALUES (%s, %s, %s)
                    '''
                    cursor.execute(query, (venta.id_venta, venta.direccion_local, venta.localidad))

                connection.commit()
                print(f"La venta del producto: {venta.producto_vendido}, se ha guardado con éxito.")
                return True

        except mysql.connector.Error as err:
            print(f"Error al intentar agregar la venta a la base de datos: {err}")
            connection.rollback()
            return False
        except Exception as e:
            print(f"Ocurrió un error inesperado al intentar agregar la venta: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()
    
    def buscar_venta(self, id_venta):
        """Busca una venta por su ID."""
        connection = self.connect()
        if not connection:
            return None
        
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ventas WHERE id_venta = %s", (id_venta,))
                venta_data = cursor.fetchone()

                if venta_data:
                    cursor.execute("SELECT direccion_envio, fecha_envio FROM ventaonline WHERE id_venta = %s", (id_venta,))
                    online_data = cursor.fetchone()
                
                    if online_data:
                        venta = VentaOnline.from_dict({**venta_data, **online_data})
                    else:
                        cursor.execute("SELECT direccion_local, localidad FROM ventalocal WHERE id_venta = %s", (id_venta,))
                        local_data = cursor.fetchone()

                        if local_data:
                            venta = VentaLocal.from_dict({**venta_data, **local_data})
                        else:
                            venta = None

                else:
                    print(f"No se encontró una venta con ID {id_venta}")
                    venta = None

        except mysql.connector.Error as err:
            print(f"Error al intentar buscar la venta: {err}")
            return None
        except Exception as e:
            print(f"Ocurrió un error al intentar buscar la venta: {e}")
            return None
        finally:
            connection.close()
        
        return venta

    def actualizar_venta(self, id_venta, fecha_venta=None, cliente=None, producto_vendido=None, descripcion=None, monto=None, metodo_pago=None, vendedor=None, direccion_envio=None, fecha_envio=None, direccion_local=None, localidad=None):
        """Actualiza los datos de una venta existente."""
        connection = self.connect()
        if not connection:
            return False
        
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM ventas WHERE id_venta = %s', (id_venta,))
                if not cursor.fetchone():
                    print(f'No existe una venta con el id {id_venta}')
                    return False


                cursor.execute("""
                    UPDATE ventas 
                    SET fecha_venta = COALESCE(%s, fecha_venta), 
                        cliente = COALESCE(%s, cliente),
                        producto_vendido = COALESCE(%s, producto_vendido), 
                        descripcion = COALESCE(%s, descripcion),
                        monto = COALESCE(%s, monto),
                        metodo_pago = COALESCE(%s, metodo_pago),
                        vendedor = COALESCE(%s, vendedor) 
                    WHERE id_venta = %s
                    """, (fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor, id_venta)
                    )

                if direccion_envio or fecha_envio:
                    cursor.execute("""
                        UPDATE ventaonline 
                        SET direccion_envio = COALESCE(%s, direccion_envio),
                            fecha_envio = COALESCE(%s, fecha_envio)
                        WHERE id_venta = %s
                    """, (direccion_envio, fecha_envio, id_venta))

                elif direccion_local or localidad:
                    cursor.execute("""
                        UPDATE ventalocal 
                        SET direccion_local = COALESCE(%s, direccion_local),
                            localidad = COALESCE(%s, localidad)
                        WHERE id_venta = %s
                    """, (direccion_local, localidad, id_venta))
                    
            connection.commit()
            print(f'La venta con el id {id_venta} ha sido actualizada con éxito')
            return True

        except mysql.connector.Error as err:
            print(f"Error al intentar actualizar la venta: {err}")
            connection.rollback()
            return False
        except Exception as e:
            print(f"Ocurrió un error al intentar actualizar la venta: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    def eliminar_venta(self, id_venta):
        """Elimina una venta de la base de datos."""
        connection = self.connect()
        if not connection:
            return False
        
        try:
            with connection.cursor() as cursor:
                id_venta = int(id_venta)
                cursor.execute('SELECT * FROM ventas WHERE id_venta = %s', (id_venta,))
                if not cursor.fetchone():
                    print(f'No existe una venta con el id {id_venta}')
                    return False

                cursor.execute('DELETE FROM ventaonline WHERE id_venta = %s', (id_venta,))
                cursor.execute('DELETE FROM ventalocal WHERE id_venta = %s', (id_venta,))
                cursor.execute('DELETE FROM ventas WHERE id_venta = %s', (id_venta,))

                if cursor.rowcount > 0:
                    connection.commit()
                    print(f'La venta con el id {id_venta} ha sido eliminada con éxito')
                    return True
                else:
                    print(f'No se pudo eliminar la venta con el id {id_venta}')
                    return False

        except mysql.connector.Error as err:
            print(f"Error en la base de datos al intentar eliminar la venta: {err}")
        except Exception as e:
            print(f"Ocurrió un error al intentar eliminar la venta: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()
    
    def mostrar_todas_las_ventas(self):
        """Muestra todas las ventas de la base de datos, tanto online como locales."""
        connection = self.connect()
        if not connection:
            return False
        
        try:
            connection = self.connect()
            if connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute('SELECT * FROM ventas')
                    ventas_data = cursor.fetchall()

                    ventas = []
                    for venta_data in ventas_data:
                        id_venta =  venta_data['id_venta']

                        cursor.execute('SELECT direccion_envio, fecha_envio FROM ventaonline WHERE id_venta = %s', (id_venta,))
                        online_data = cursor.fetchone()

                        if online_data:
                            venta_data['direccion_envio'] = online_data['direccion_envio']
                            venta_data['fecha_envio'] = online_data['fecha_envio']
                            venta = VentaOnline(**venta_data)
                        
                        else:
                            cursor.execute('SELECT direccion_local, localidad FROM ventalocal WHERE id_venta = %s', (id_venta,))
                            local_data = cursor.fetchone()

                            if  local_data:
                                venta_data['direccion_local'] = local_data['direccion_local']
                                venta_data['localidad'] = local_data['localidad']
                                venta = VentaLocal(**venta_data)
                            else:
                                continue
                                
                        ventas.append(venta)

                    return ventas

        except mysql.connector.Error as err:
            print(f"Error en la base de datos al intentar mostrar todas las ventas: {err}")
            return False
        except Exception as e:
            print(f"Ocurrió un error al intentar mostrar todas las ventas: {e}")
            return False
        finally:
            connection.close()

