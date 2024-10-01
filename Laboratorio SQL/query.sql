CREATE DATABASE ventas;

USE ventas;

CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY,
    fecha_venta DATE NOT NULL,
    cliente VARCHAR(50) NOT NULL,
    producto_vendido VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255),
    monto DECIMAL(10, 2) NOT NULL,
    metodo_pago VARCHAR(30) NOT NULL,
    vendedor VARCHAR(50) NOT NULL
);

CREATE TABLE VentaOnline (
    id_venta INT PRIMARY KEY,
    direccion_envio VARCHAR(255) NOT NULL,
    fecha_envio DATE NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta) -- Relación con Ventas
);

CREATE TABLE VentaLocal (
    id_venta INT PRIMARY KEY,
    direccion_local VARCHAR(255) NOT NULL,
    localidad VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta) -- Relación con Ventas
);

DESCRIBE TABLE VentaLocal;

ALTER TABLE Ventas 
MODIFY COLUMN metodo_pago VARCHAR(40) NOT NULL;