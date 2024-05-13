import tkinter as tk

class SistemaContable:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Contable")
        
        # Etiquetas y entradas de texto para ingresos
        tk.Label(root, text="Ingresos").grid(row=0, column=0, sticky="w")
        self.ingreso_nombre_entry = tk.Entry(root)
        self.ingreso_nombre_entry.grid(row=1, column=0)
        self.ingreso_cantidad_entry = tk.Entry(root)
        self.ingreso_cantidad_entry.grid(row=1, column=1)
        self.ingresos = {}
        
        # Etiquetas y entradas de texto para gastos
        tk.Label(root, text="Gastos").grid(row=2, column=0, sticky="w")
        self.gasto_nombre_entry = tk.Entry(root)
        self.gasto_nombre_entry.grid(row=3, column=0)
        self.gasto_cantidad_entry = tk.Entry(root)
        self.gasto_cantidad_entry.grid(row=3, column=1)
        self.gastos = {}
        
        # Botón para agregar ingresos
        tk.Button(root, text="Agregar Ingreso", command=self.agregar_ingreso).grid(row=1, column=2)
        
        # Botón para agregar gastos
        tk.Button(root, text="Agregar Gasto", command=self.agregar_gasto).grid(row=3, column=2)
        
        # Botón para calcular el balance
        tk.Button(root, text="Calcular Balance", command=self.mostrar_detalle_balance).grid(row=5, columnspan=3)
        
    def agregar_ingreso(self):
        nombre = self.ingreso_nombre_entry.get()
        cantidad = float(self.ingreso_cantidad_entry.get())
        self.ingresos[nombre] = cantidad
        self.ingreso_nombre_entry.delete(0, tk.END)
        self.ingreso_cantidad_entry.delete(0, tk.END)
        
    def agregar_gasto(self):
        nombre = self.gasto_nombre_entry.get()
        cantidad = float(self.gasto_cantidad_entry.get())
        self.gastos[nombre] = cantidad
        self.gasto_nombre_entry.delete(0, tk.END)
        self.gasto_cantidad_entry.delete(0, tk.END)
        
    def mostrar_detalle_balance(self):
        detalle = "Detalle del Balance:\n"
        detalle += "-" * 20 + "\n"
        detalle += "Ingresos:\n"
        for nombre, cantidad in self.ingresos.items():
            detalle += f"{nombre}: ${cantidad:.2f}\n"
        detalle += "-" * 20 + "\n"
        detalle += "Gastos:\n"
        for nombre, cantidad in self.gastos.items():
            detalle += f"{nombre}: ${cantidad:.2f}\n"
        detalle += "-" * 20 + "\n"
        
        total_ingresos = sum(self.ingresos.values())
        total_gastos = sum(self.gastos.values())
        detalle += f"Total de Ingresos: ${total_ingresos:.2f}\n"
        detalle += f"Total de Gastos: ${total_gastos:.2f}\n"
        
        balance = total_ingresos - total_gastos
        detalle += f"Balance: ${balance:.2f}\n"
        
        popup = tk.Toplevel()
        popup.title("Detalle del Balance")
        tk.Label(popup, text=detalle).pack()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaContable(root)
    root.mainloop()
