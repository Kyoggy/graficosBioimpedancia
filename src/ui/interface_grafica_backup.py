#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Grafica para Analisador de Bioimpedancia
Permite adicionar novos dados sem abrir a planilha
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
from datetime import datetime, date
import sys

# Adiciona o diretorio scripts ao path
sys.path.append('scripts')

class BioimpedanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Bioimpedancia - Interface Grafica")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Variaveis para os campos
        self.var_data = tk.StringVar()
        self.var_peso = tk.StringVar()
        self.var_imc = tk.StringVar()
        self.var_gordura_pct = tk.StringVar()
        self.var_gordura_kg = tk.StringVar()
        self.var_massa_muscular_pct = tk.StringVar()
        self.var_massa_muscular_kg = tk.StringVar()
        self.var_metabolismo = tk.StringVar()
        self.var_obesidade_pct = tk.StringVar()
        
        # Define o arquivo CSV padrao
        self.csv_file = "data/dados_peso_exemplo.csv"
        
        self.create_widgets()
        self.load_last_data()
        
    def create_widgets(self):
        """Cria os widgets da interface"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configura o grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Titulo
        title_label = ttk.Label(main_frame, text="Analisador de Bioimpedancia", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Campos de entrada
        self.create_input_fields(main_frame)
        
        # Botoes
        self.create_buttons(main_frame)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Pronto para usar", 
                                     relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0))
    
    def create_input_fields(self, parent):
        """Cria os campos de entrada"""
        
        # Data
        ttk.Label(parent, text="Data:").grid(row=1, column=0, sticky=tk.W, pady=5)
        data_frame = ttk.Frame(parent)
        data_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Entry(data_frame, textvariable=self.var_data, width=15).pack(side=tk.LEFT)
        ttk.Button(data_frame, text="Hoje", 
                  command=self.set_today).pack(side=tk.LEFT, padx=(5, 0))
        
        # Peso
        ttk.Label(parent, text="Peso (kg):").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_peso, width=20).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # IMC
        ttk.Label(parent, text="IMC:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_imc, width=20).grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Gordura %
        ttk.Label(parent, text="Gordura (%):").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_gordura_pct, width=20).grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Gordura KG
        ttk.Label(parent, text="Gordura (kg):").grid(row=5, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_gordura_kg, width=20).grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Massa Muscular %
        ttk.Label(parent, text="Massa Muscular (%):").grid(row=6, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_massa_muscular_pct, width=20).grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Massa Muscular KG
        ttk.Label(parent, text="Massa Muscular (kg):").grid(row=7, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_massa_muscular_kg, width=20).grid(row=7, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Metabolismo
        ttk.Label(parent, text="Metabolismo (kcal/dia):").grid(row=8, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_metabolismo, width=20).grid(row=8, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Obesidade %
        ttk.Label(parent, text="Obesidade (%):").grid(row=9, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=self.var_obesidade_pct, width=20).grid(row=9, column=1, sticky=(tk.W, tk.E), pady=5)
    
    def create_buttons(self, parent):
        """Cria os botoes"""
        
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Adicionar Dados", 
                  command=self.add_data).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Carregar Arquivo", 
                  command=self.load_file).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Gerar Graficos", 
                  command=self.generate_charts).pack(side=tk.LEFT)
    
    def set_today(self):
        """Define a data de hoje"""
        self.var_data.set(date.today().strftime("%Y-%m-%d"))
    
    def add_data(self):
        """Adiciona dados ao arquivo CSV"""
        try:
            # Valida os dados
            if not self.var_data.get() or not self.var_peso.get():
                messagebox.showerror("Erro", "Data e peso sao obrigatorios!")
                return
            
            # Prepara os dados
            data = {
                'data': self.var_data.get(),
                'peso': float(self.var_peso.get()),
                'imc': float(self.var_imc.get()) if self.var_imc.get() else '',
                'Gordura/porcento': float(self.var_gordura_pct.get()) if self.var_gordura_pct.get() else '',
                'Gordura/KG': float(self.var_gordura_kg.get()) if self.var_gordura_kg.get() else '',
                'Massa Musucular/porcento': float(self.var_massa_muscular_pct.get()) if self.var_massa_muscular_pct.get() else '',
                'Massa Muscular/KG': float(self.var_massa_muscular_kg.get()) if self.var_massa_muscular_kg.get() else '',
                'Metabolismo': float(self.var_metabolismo.get()) if self.var_metabolismo.get() else '',
                'Obesidade/porcento': float(self.var_obesidade_pct.get()) if self.var_obesidade_pct.get() else ''
            }
            
            # Verifica se o arquivo existe
            file_exists = os.path.exists(self.csv_file)
            
            # Adiciona ao arquivo
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                fieldnames = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                             'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(data)
            
            messagebox.showinfo("Sucesso", "Dados adicionados com sucesso!")
            self.clear_fields()
            self.update_status("Dados adicionados com sucesso")
            
        except ValueError as e:
            messagebox.showerror("Erro", f"Valor invalido: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar dados: {e}")
    
    def clear_fields(self):
        """Limpa todos os campos"""
        self.var_data.set("")
        self.var_peso.set("")
        self.var_imc.set("")
        self.var_gordura_pct.set("")
        self.var_gordura_kg.set("")
        self.var_massa_muscular_pct.set("")
        self.var_massa_muscular_kg.set("")
        self.var_metabolismo.set("")
        self.var_obesidade_pct.set("")
    
    def load_file(self):
        """Carrega um arquivo CSV"""
        file_path = filedialog.askopenfilename(
            title="Selecionar arquivo CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            self.csv_file = file_path
            self.update_status(f"Arquivo carregado: {os.path.basename(file_path)}")
    
    def load_last_data(self):
        """Carrega os ultimos dados do arquivo"""
        try:
            if os.path.exists(self.csv_file):
                with open(self.csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                    
                    if rows:
                        last_row = rows[-1]
                        self.var_data.set(last_row.get('data', ''))
                        self.var_peso.set(last_row.get('peso', ''))
                        self.var_imc.set(last_row.get('imc', ''))
                        self.var_gordura_pct.set(last_row.get('Gordura/porcento', ''))
                        self.var_gordura_kg.set(last_row.get('Gordura/KG', ''))
                        self.var_massa_muscular_pct.set(last_row.get('Massa Musucular/porcento', ''))
                        self.var_massa_muscular_kg.set(last_row.get('Massa Muscular/KG', ''))
                        self.var_metabolismo.set(last_row.get('Metabolismo', ''))
                        self.var_obesidade_pct.set(last_row.get('Obesidade/porcento', ''))
                        
                        self.update_status(f"Ultimos dados carregados: {len(rows)} medições")
        except Exception as e:
            self.update_status(f"Erro ao carregar dados: {e}")
    
    def generate_charts(self):
        """Gera os graficos"""
        try:
            # Importa o analisador
            from bioimpedance_analyzer import BioimpedanceAnalyzer
            
            # Cria o analisador e gera os graficos
            analyzer = BioimpedanceAnalyzer(self.csv_file)
            analyzer.generate_report()
            
            messagebox.showinfo("Sucesso", "Graficos gerados com sucesso!")
            self.update_status("Graficos gerados com sucesso")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar graficos: {e}")
    
    def update_status(self, message):
        """Atualiza a mensagem de status"""
        self.status_label.config(text=message)

def main():
    """Funcao principal"""
    root = tk.Tk()
    app = BioimpedanceGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()