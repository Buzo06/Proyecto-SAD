--Tabla de Sucursales
CREATE TABLE sucursales (
    sucursal_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(15)
);

--Tabla de Empleados
CREATE TABLE empleados (
    empleado_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    puesto VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    sucursal_id INT,
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id) ON DELETE SET NULL
);

--Tabla de Especias
CREATE TABLE especias (
    especia_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100)
);

--Tabla de Hamburguesas
CREATE TABLE hamburguesas (
    hamburguesa_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion VARCHAR(100),
    especia_id INT,
    FOREIGN KEY (especia_id) REFERENCES especias(especia_id) ON DELETE SET NULL
);

--Tabla de Ventas
CREATE TABLE ventas (
    venta_id INT AUTO_INCREMENT PRIMARY KEY,
    sucursal_id INT,
    fecha_venta DATE NOT NULL,
    empleado_id INT,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(empleado_id)
);

--Tabla Detalle de Ventas
CREATE TABLE detalle_ventas (
    detalle_id INT AUTO_INCREMENT PRIMARY KEY,
    venta_id INT,
    hamburguesa_id INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES ventas(venta_id) ON DELETE CASCADE,
    FOREIGN KEY (hamburguesa_id) REFERENCES hamburguesas(hamburguesa_id)
);
