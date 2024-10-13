import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

class AccountingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Contable")
        self.root.geometry("800x600")

        self.accounts = {
            'Activos': ['Banco', 'Cuentas por Cobrar', 'Inventario', 'Maquinaria y Equipo'],
            'Pasivos': ['Cuentas por Pagar', 'Créditos por Pagar', 'Sueldos y Salarios'],
            'Capital': ['Inversión Inicial'],
            'Gastos': ['Gastos Operativos', 'Gastos Administrativos'],
            'Ingresos': ['Ventas', 'Ingresos Diversos']
        }

        self.create_widgets()
        self.transactions = []

    def create_widgets(self):
        # Dropdown for account types
        self.account_type_label = tk.Label(self.root, text="Tipo de Cuenta:")
        self.account_type_label.pack()

        self.account_type_var = tk.StringVar()
        self.account_type_dropdown = ttk.Combobox(self.root, textvariable=self.account_type_var)
        self.account_type_dropdown['values'] = list(self.accounts.keys())
        self.account_type_dropdown.pack()

        # Dropdown for specific account
        self.account_label = tk.Label(self.root, text="Cuenta:")
        self.account_label.pack()

        self.account_var = tk.StringVar()
        self.account_dropdown = ttk.Combobox(self.root, textvariable=self.account_var)
        self.account_dropdown.pack()

        self.account_type_dropdown.bind('<<ComboboxSelected>>', self.update_accounts)

        # Entry for date
        self.date_label = tk.Label(self.root, text="Fecha (YYYY-MM-DD):")
        self.date_label.pack()

        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        # Entry for amount
        self.amount_label = tk.Label(self.root, text="Monto:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        # Add transaction button
        self.add_transaction_button = tk.Button(self.root, text="Agregar Transacción", command=self.add_transaction)
        self.add_transaction_button.pack()

        # Table for displaying transactions
        self.transactions_label = tk.Label(self.root, text="Transacciones:")
        self.transactions_label.pack()

        self.transactions_tree = ttk.Treeview(self.root, columns=('Fecha', 'Cuenta', 'Monto', 'Tipo'), show='headings')
        self.transactions_tree.heading('Fecha', text='Fecha')
        self.transactions_tree.heading('Cuenta', text='Cuenta')
        self.transactions_tree.heading('Monto', text='Monto')
        self.transactions_tree.heading('Tipo', text='Tipo')
        self.transactions_tree.pack()

        # Buttons for generating reports
        self.generate_balance_button = tk.Button(self.root, text="Generar Balance General", command=self.generate_balance_sheet)
        self.generate_balance_button.pack()

        self.generate_pnl_button = tk.Button(self.root, text="Generar Estado de Ganancias y Pérdidas", command=self.generate_pnl)
        self.generate_pnl_button.pack()

    def update_accounts(self, event):
        account_type = self.account_type_var.get()
        if account_type in self.accounts:
            self.account_dropdown['values'] = self.accounts[account_type]
        else:
            self.account_dropdown['values'] = []

    def add_transaction(self):
        date = self.date_entry.get()
        account = self.account_var.get()
        amount = self.amount_entry.get()

        if not date or not account or not amount:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número")
            return

        account_type = self.account_type_var.get()
        self.transactions.append({'Fecha': date, 'Cuenta': account, 'Monto': amount, 'Tipo': account_type})
        self.transactions_tree.insert('', 'end', values=(date, account, amount, account_type))

    def generate_balance_sheet(self):
        # Filtra las transacciones por tipo
        balance = {'Activos': 0, 'Pasivos': 0, 'Capital': 0}
        for transaction in self.transactions:
            if transaction['Tipo'] in balance:
                balance[transaction['Tipo']] += transaction['Monto']

        # Genera el PDF del Balance General usando reportlab
        pdf_filename = "balance_general.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawString(100, 750, "Balance General")
        
        y_position = 730
        for key, value in balance.items():
            c.drawString(100, y_position, f"{key}: ${value}")
            y_position -= 20
        
        c.save()
        messagebox.showinfo("Información", f"Balance General generado como {pdf_filename}")

    def generate_pnl(self):
        # Filtra las transacciones por tipo
        pnl = {'Ingresos': 0, 'Gastos': 0}
        for transaction in self.transactions:
            if transaction['Tipo'] in pnl:
                pnl[transaction['Tipo']] += transaction['Monto']

        # Calcula las ganancias/pérdidas
        resultado = pnl['Ingresos'] - pnl['Gastos']

        # Genera el PDF del Estado de Ganancias y Pérdidas usando reportlab
        pdf_filename = "estado_ganancias_perdidas.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawString(100, 750, "Estado de Ganancias y Pérdidas")
        
        y_position = 730
        for key, value in pnl.items():
            c.drawString(100, y_position, f"{key}: ${value}")
            y_position -= 20

        c.drawString(100, y_position, f"Resultado: ${resultado}")
        c.save()
        messagebox.showinfo("Información", f"Estado de Ganancias y Pérdidas generado como {pdf_filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountingApp(root)
    root.mainloop()
