
import tkinter as tk
from tkinter import simpledialog, ttk

class SistemaNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Notas")
        
        self.alumnos = {}
        self.materias = ["Matemáticas", "Física", "Química", "Historia", "Geografía"]
        
        # Nombre del estudiante
        self.nombre = tk.StringVar()
        
        # Etiqueta y entrada de texto para el nombre del alumno
        tk.Label(root, text="Nombre del Alumno:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(root, textvariable=self.nombre)
        self.nombre_entry.grid(row=0, column=1)
        
        # Etiqueta y lista desplegable para la materia
        tk.Label(root, text="Materia:").grid(row=1, column=0)
        self.materia_combobox = ttk.Combobox(root, values=self.materias, state="readonly")
        self.materia_combobox.grid(row=1, column=1)
        
        # Botón para agregar la nota
        tk.Button(root, text="Agregar Nota", command=self.agregar_nota).grid(row=2, columnspan=2)
        
        # Botón para agregar materia
        tk.Button(root, text="Agregar Materia", command=self.agregar_materia).grid(row=1, column=2)
        
        # Botón para mostrar resultados
        tk.Button(root, text="Mostrar Resultados", command=self.mostrar_resultados).grid(row=3, columnspan=3)
        
    def agregar_materia(self):
        nueva_materia = simpledialog.askstring("Nueva Materia", "Ingrese el nombre de la nueva materia:")
        if nueva_materia:
            self.materias.append(nueva_materia)
            self.materia_combobox["values"] = self.materias
            self.materia_combobox.set(nueva_materia)
        
    def agregar_nota(self):
        nombre = self.nombre.get()
        materia = self.materia_combobox.get()
        nota = float(simpledialog.askstring("Nueva Nota", f"Ingrese la nota para {materia}:"))
        
        if nombre not in self.alumnos:
            self.alumnos[nombre] = {}
        if materia not in self.alumnos[nombre]:
            self.alumnos[nombre][materia] = []
        self.alumnos[nombre][materia].append(nota)
        
    def mostrar_resultados(self):
        resultados = tk.Toplevel()
        resultados.title("Resultados")
        
        tabla = tk.Text(resultados, height=10, width=80)
        tabla.grid(row=1, column=1, columnspan= 7)
        
        tabla.insert(tk.END, "Nombre\t")
        for materia in self.materias:
            tabla.insert(tk.END, f"{materia}\t")
        tabla.insert(tk.END, "Promedio\n")
        
        for nombre, materias in self.alumnos.items():
            tabla.insert(tk.END, f"{nombre}\t")
            for materia in self.materias:
                notas = materias.get(materia, [])
                promedio = sum(notas) / len(notas) if notas else 0
                tabla.insert(tk.END, f"{', '.join(map(str, notas))}\t")
            promedio_total = sum(sum(materias.get(materia, [])) for materia in self.materias) / len(self.materias)
            tabla.insert(tk.END, f"{promedio_total:.2f}\n")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaNotas(root)
    root.mainloop()
