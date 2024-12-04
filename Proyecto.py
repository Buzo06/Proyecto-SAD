import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Conexión a la base de datos
def conectar_bd():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Cambiar según configuración
            database="proyecto_Burguer.sql"  # Cambiar al nombre de la base de datos
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None

# Crear las tablas necesarias
def crear_tablas():
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS sucursales (
                sucursal_id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                direccion VARCHAR(100) NOT NULL,
                telefono VARCHAR(15)
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                empleado_id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                puesto VARCHAR(50) NOT NULL,
                salario DECIMAL(10, 2) NOT NULL,
                fecha_contratacion DATE NOT NULL,
                sucursal_id INT,
                FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id)
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS especias (
                especia_id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                descripcion TEXT
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS hamburguesas (
                hamburguesa_id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                precio DECIMAL(10, 2) NOT NULL,
                descripcion TEXT,
                especia_id INT,
                FOREIGN KEY (especia_id) REFERENCES especias(especia_id)
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                venta_id INT AUTO_INCREMENT PRIMARY KEY,
                fecha DATETIME NOT NULL,
                sucursal_id INT,
                empleado_id INT,
                FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id),
                FOREIGN KEY (empleado_id) REFERENCES empleados(empleado_id)
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS detalle_ventas (
                detalle_id INT AUTO_INCREMENT PRIMARY KEY,
                venta_id INT,
                hamburguesa_id INT,
                cantidad INT NOT NULL,
                precio_unitario DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (venta_id) REFERENCES ventas(venta_id),
                FOREIGN KEY (hamburguesa_id) REFERENCES hamburguesas(hamburguesa_id)
            );
            """)
            conn.commit()
            print("Tablas creadas o verificadas correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al crear tablas: {e}")
        finally:
            cursor.close()
            conn.close()

# Función para insertar registros en sucursales
def insertar_sucursal(nombre, direccion, telefono):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO sucursales (nombre, direccion, telefono) VALUES (%s, %s, %s)",
                (nombre, direccion, telefono)
            )
            conn.commit()
            messagebox.showinfo("Éxito", "Sucursal agregada correctamente.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo insertar la sucursal: {e}")
        finally:
            cursor.close()
            conn.close()

# Función para consultar registros
def consultar_sucursales(tree):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM sucursales")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo consultar las sucursales: {e}")
        finally:
            cursor.close()
            conn.close()

# Interfaz gráfica
def main():
    # Crear las tablas al inicio
    crear_tablas()

    # Crear ventana principal
    root = tk.Tk()
    root.title("Gestión de Base de Datos")

    # Formulario para agregar sucursales
    frame_form = tk.Frame(root)
    frame_form.pack(pady=10)

    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_form)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Dirección:").grid(row=1, column=0, padx=5, pady=5)
    entry_direccion = tk.Entry(frame_form)
    entry_direccion.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5)
    entry_telefono = tk.Entry(frame_form)
    entry_telefono.grid(row=2, column=1, padx=5, pady=5)

    def agregar_sucursal():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        if nombre and direccion and telefono:
            insertar_sucursal(nombre, direccion, telefono)
            entry_nombre.delete(0, tk.END)
            entry_direccion.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    tk.Button(frame_form, text="Agregar Sucursal", command=agregar_sucursal).grid(row=3, columnspan=2, pady=10)

    # Tabla para mostrar sucursales
    frame_table = tk.Frame(root)
    frame_table.pack(pady=10)

    columns = ("ID", "Nombre", "Dirección", "Teléfono")
    tree = ttk.Treeview(frame_table, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack()

    tk.Button(root, text="Consultar Sucursales", command=lambda: consultar_sucursales(tree)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
