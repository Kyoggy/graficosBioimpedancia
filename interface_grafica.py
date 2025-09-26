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
        title_label = ttk.Label(main_frame, text="Dados de Bioimpedancia", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame para selecao de arquivo
        file_frame = ttk.LabelFrame(main_frame, text="Arquivo de Dados", padding="10")
        file_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Label(file_frame, text="Arquivo CSV:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.file_label = ttk.Label(file_frame, text=self.csv_file, 
                                   background="white", relief="sunken", anchor="w")
        self.file_label.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Button(file_frame, text="Alterar", 
                  command=self.select_file).grid(row=0, column=2)
        
        # Frame para entrada de dados
        data_frame = ttk.LabelFrame(main_frame, text="Novos Dados", padding="10")
        data_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        data_frame.columnconfigure(1, weight=1)
        
        # Data
        ttk.Label(data_frame, text="Data:").grid(row=0, column=0, sticky=tk.W, pady=5)
        data_entry = ttk.Entry(data_frame, textvariable=self.var_data, width=15)
        data_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Button(data_frame, text="Hoje", 
                  command=self.set_today).grid(row=0, column=2, padx=(10, 0))
        
        # Peso
        ttk.Label(data_frame, text="Peso (kg):").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_peso, width=15).grid(row=1, column=1, 
                                                                        sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # IMC
        ttk.Label(data_frame, text="IMC:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_imc, width=15).grid(row=2, column=1, 
                                                                      sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Gordura %
        ttk.Label(data_frame, text="Gordura (%):").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_gordura_pct, width=15).grid(row=3, column=1, 
                                                                              sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Gordura KG
        ttk.Label(data_frame, text="Gordura (kg):").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_gordura_kg, width=15).grid(row=4, column=1, 
                                                                             sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Massa Muscular %
        ttk.Label(data_frame, text="Massa Muscular (%):").grid(row=5, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_massa_muscular_pct, width=15).grid(row=5, column=1, 
                                                                                     sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Massa Muscular KG
        ttk.Label(data_frame, text="Massa Muscular (kg):").grid(row=6, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_massa_muscular_kg, width=15).grid(row=6, column=1, 
                                                                                     sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Metabolismo
        ttk.Label(data_frame, text="Metabolismo (kcal/dia):").grid(row=7, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_metabolismo, width=15).grid(row=7, column=1, 
                                                                              sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Obesidade %
        ttk.Label(data_frame, text="Obesidade (%):").grid(row=8, column=0, sticky=tk.W, pady=5)
        ttk.Entry(data_frame, textvariable=self.var_obesidade_pct, width=15).grid(row=8, column=1, 
                                                                                sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Frame para botoes
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Salvar Dados", 
                  command=self.save_data, style="Accent.TButton").pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Limpar Campos", 
                  command=self.clear_fields).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Gerar Graficos", 
                  command=self.generate_charts).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Ver Dados", 
                  command=self.view_data).pack(side=tk.LEFT)
        
        # Frame para status
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_label = ttk.Label(status_frame, text="Pronto para adicionar novos dados", 
                                    background="lightgreen", relief="sunken", anchor="w")
        self.status_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Configura validacao
        self.setup_validation()
        
    def setup_validation(self):
        """Configura validacao dos campos"""
        # Valida que apenas numeros podem ser inseridos nos campos numericos
        numeric_fields = [self.var_peso, self.var_imc, self.var_gordura_pct, 
                         self.var_gordura_kg, self.var_massa_muscular_pct, 
                         self.var_massa_muscular_kg, self.var_metabolismo, self.var_obesidade_pct]
        
        for var in numeric_fields:
            var.trace('w', self.validate_numeric)
    
    def validate_numeric(self, *args):
        """Valida se o campo contem apenas numeros"""
        # Esta funcao pode ser expandida para validacao em tempo real
        pass
    
    def set_today(self):
        """Define a data de hoje"""
        today = date.today().strftime("%Y-%m-%d")
        self.var_data.set(today)
    
    def select_file(self):
        """Seleciona o arquivo CSV"""
        file_path = filedialog.askopenfilename(
            title="Selecionar arquivo CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialdir="data"
        )
        
        if file_path:
            self.csv_file = file_path
            self.file_label.config(text=file_path)
            self.update_status(f"Arquivo selecionado: {os.path.basename(file_path)}")
    
    def load_last_data(self):
        """Carrega os ultimos dados do arquivo para referencia"""
        try:
            if os.path.exists(self.csv_file):
                with open(self.csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                    
                if rows:
                    last_row = rows[-1]
                    # Define a proxima data (adiciona 1 dia a partir da ultima)
                    try:
                        last_date = datetime.strptime(last_row['data'], '%Y-%m-%d')
                        next_date = last_date.replace(day=last_date.day + 1)
                        self.var_data.set(next_date.strftime('%Y-%m-%d'))
                    except:
                        self.set_today()
                    
                    self.update_status(f"Ultima entrada: {last_row['data']} - {last_row['peso']}kg")
        except Exception as e:
            self.set_today()
            self.update_status(f"Erro ao carregar dados: {str(e)}")
    
    def validate_data(self):
        """Valida os dados inseridos"""
        errors = []
        
        # Valida data
        if not self.var_data.get():
            errors.append("Data e obrigatoria")
        else:
            try:
                datetime.strptime(self.var_data.get(), '%Y-%m-%d')
            except ValueError:
                errors.append("Data deve estar no formato YYYY-MM-DD")
        
        # Valida peso
        if not self.var_peso.get():
            errors.append("Peso e obrigatorio")
        else:
            try:
                peso = float(self.var_peso.get())
                if peso <= 0 or peso > 500:
                    errors.append("Peso deve estar entre 0 e 500 kg")
            except ValueError:
                errors.append("Peso deve ser um numero valido")
        
        # Valida IMC
        if self.var_imc.get():
            try:
                imc = float(self.var_imc.get())
                if imc <= 0 or imc > 100:
                    errors.append("IMC deve estar entre 0 e 100")
            except ValueError:
                errors.append("IMC deve ser um numero valido")
        
        # Valida outros campos numericos
        numeric_fields = [
            (self.var_gordura_pct, "Gordura (%)", 0, 100),
            (self.var_gordura_kg, "Gordura (kg)", 0, 200),
            (self.var_massa_muscular_pct, "Massa Muscular (%)", 0, 100),
            (self.var_massa_muscular_kg, "Massa Muscular (kg)", 0, 200),
            (self.var_metabolismo, "Metabolismo", 500, 5000),
            (self.var_obesidade_pct, "Obesidade (%)", 0, 100)
        ]
        
        for var, name, min_val, max_val in numeric_fields:
            if var.get():
                try:
                    value = float(var.get())
                    if value < min_val or value > max_val:
                        errors.append(f"{name} deve estar entre {min_val} e {max_val}")
                except ValueError:
                    errors.append(f"{name} deve ser um numero valido")
        
        return errors
    
    def save_data(self):
        """Salva os dados no arquivo CSV"""
        # Valida os dados
        errors = self.validate_data()
        if errors:
            messagebox.showerror("Erro de Validacao", "\n".join(errors))
            return
        
        try:
            # Verifica se o arquivo existe
            file_exists = os.path.exists(self.csv_file)
            
            # Prepara os dados
            data = {
                'data': self.var_data.get(),
                'peso': self.var_peso.get(),
                'imc': self.var_imc.get() or '',
                'Gordura/porcento': self.var_gordura_pct.get() or '',
                'Gordura/KG': self.var_gordura_kg.get() or '',
                'Massa Musucular/porcento': self.var_massa_muscular_pct.get() or '',
                'Massa Muscular/KG': self.var_massa_muscular_kg.get() or '',
                'Metabolismo': self.var_metabolismo.get() or '',
                'Obesidade/porcento': self.var_obesidade_pct.get() or ''
            }
            
            # Escreve no arquivo
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                fieldnames = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                             'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Escreve o cabecalho se o arquivo nao existe
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(data)
            
            self.update_status(f"Dados salvos com sucesso! Data: {data['data']}, Peso: {data['peso']}kg")
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            
            # Limpa os campos para proxima entrada
            self.clear_fields()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
            self.update_status(f"Erro ao salvar: {str(e)}")
    
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
        
        self.update_status("Campos limpos")
    
    def generate_charts(self):
        """Gera os graficos usando o analisador"""
        try:
            if not os.path.exists(self.csv_file):
                messagebox.showerror("Erro", "Arquivo CSV nao encontrado!")
                return
            
            # Importa e executa o analisador
            from bioimpedance_analyzer import BioimpedanceAnalyzer
            
            analyzer = BioimpedanceAnalyzer(self.csv_file)
            analyzer.generate_report()
            
            self.update_status("Graficos gerados com sucesso!")
            messagebox.showinfo("Sucesso", "Graficos gerados com sucesso! Verifique a pasta 'data/'")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar graficos: {str(e)}")
            self.update_status(f"Erro ao gerar graficos: {str(e)}")
    
    def view_data(self):
        """Abre uma janela para visualizar os dados"""
        try:
            if not os.path.exists(self.csv_file):
                messagebox.showerror("Erro", "Arquivo CSV nao encontrado!")
                return
            
            # Cria nova janela
            view_window = tk.Toplevel(self.root)
            view_window.title("Dados Salvos")
            view_window.geometry("800x400")
            
            # Cria treeview para mostrar os dados
            frame = ttk.Frame(view_window)
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Scrollbars
            v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
            h_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
            
            # Treeview
            tree = ttk.Treeview(frame, yscrollcommand=v_scrollbar.set, 
                               xscrollcommand=h_scrollbar.set)
            
            v_scrollbar.config(command=tree.yview)
            h_scrollbar.config(command=tree.xview)
            
            # Layout
            tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
            h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
            
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)
            
            # Carrega os dados
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                columns = reader.fieldnames
                
                # Configura as colunas
                tree['columns'] = columns
                tree['show'] = 'headings'
                
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=100, minwidth=50)
                
                # Adiciona os dados
                for row in reader:
                    tree.insert('', tk.END, values=[row[col] for col in columns])
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao visualizar dados: {str(e)}")
    
    def update_status(self, message):
        """Atualiza a mensagem de status"""
        self.status_label.config(text=message)
        self.root.update_idletasks()

def main():
    """Funcao principal"""
    root = tk.Tk()
    
    # Configura o estilo
    style = ttk.Style()
    style.theme_use('clam')
    
    # Cria a aplicacao
    app = BioimpedanceGUI(root)
    
    # Inicia o loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
