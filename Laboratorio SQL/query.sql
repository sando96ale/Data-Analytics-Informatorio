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

INSERT INTO Ventas (id_venta, fecha_venta, cliente, producto_vendido, descripcion, monto, metodo_pago, vendedor)
VALUES (1, '2024-10-01', 'Juan Perez', 'Tarjeta Gráfica', 'NVIDIA RTX 3080', 1200.50, 'Tarjeta de crédito', 'Martin Sánchez'),
(2, '2024-10-02', 'Lucia Martinez', 'Procesador', 'Intel i9 11900K', 450.75, 'Transferencia bancaria', 'Camila Gomez'),
(3, '2024-10-03', 'Marcos Diaz', 'Monitor', 'Monitor Gaming 27" 144Hz', 299.99, 'Efectivo', 'Federico Sánchez'),
(4, '2024-10-03', 'Sofía Lopez', 'Mouse', 'Mouse Razer DeathAdder V2', 59.99, 'Tarjeta de débito', 'Jorge Lopez'),
(5, '2024-10-04', 'Esteban Salazar', 'Memoria RAM', 'Corsair Vengeance 16GB DDR4', 79.99, 'Efectivo', 'Camila Gomez'),
(6, '2024-10-05', 'Laura Fernandez', 'Motherboard', 'MSI Z590 Gaming Plus', 199.99, 'Tarjeta de crédito', 'Jorge Lopez'),
(7, '2024-10-06', 'Diego Gonzalez', 'Mouse Pad', 'SteelSeries QcK Large', 19.99, 'Transferencia bancaria', 'Martin Sánchez');

INSERT INTO VentaOnline (id_venta, direccion_envio, fecha_envio)
VALUES (1, 'Buenos Aires 49, Quitilipi', '2024-10-02'),
(5, 'Saavedra 1298, Resisitencia', '2024-10-05'),
(7, 'Jujuy 192, Saenz Peña', '2024-10-06');

INSERT INTO VentaLocal (id_venta, direccion_local, localidad)
VALUES 
(2, 'Mendoza 123, Local 8', 'Resistencia'),
(3, 'Sargento Cabral 134, Local 6', 'Quitilipi'),
(4, 'Hipolito Irigoyen 1454, Local 3', 'Villa Angela'),
(6, 'San Martin, Local 1', 'Resistencia');

SELECT * FROM Ventas;