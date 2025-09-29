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
from tkinter import font

# Adiciona o diretorio scripts ao path
sys.path.append('scripts')

class BioimpedanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Bioimpedancia - Interface Moderna")
        self.root.geometry("800x900")
        self.root.resizable(True, True)
        
        # ConfiguraÃ§Ã£o de tema moderno
        self.setup_modern_theme()
        
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
    
    def setup_modern_theme(self):
        """Configura tema moderno com cores e estilos"""
        # Cores modernas
        self.colors = {
            'primary': '#2E86AB',      # Azul moderno
            'secondary': '#A23B72',    # Rosa moderno
            'success': '#F18F01',      # Laranja
            'danger': '#C73E1D',       # Vermelho
            'light': '#F8F9FA',        # Cinza claro
            'dark': '#212529',         # Cinza escuro
            'white': '#FFFFFF',
            'gray': '#6C757D'
        }
        
        # Configura estilo ttk
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configura cores personalizadas
        self.style.configure('Title.TLabel', 
                           font=('Segoe UI', 20, 'bold'),
                           foreground=self.colors['primary'])
        
        self.style.configure('Card.TFrame',
                           background=self.colors['white'],
                           relief='solid',
                           borderwidth=1)
        
        self.style.configure('Modern.TButton',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 10))
        
        self.style.configure('Success.TButton',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 10))
        
        self.style.configure('Danger.TButton',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 10))
        
        # Configura cores dos botÃµes
        self.style.map('Modern.TButton',
                      background=[('active', self.colors['primary']),
                                ('pressed', '#1e5f7a')])
        
        self.style.map('Success.TButton',
                      background=[('active', self.colors['success']),
                                ('pressed', '#d17a00')])
        
        self.style.map('Danger.TButton',
                      background=[('active', self.colors['danger']),
                                ('pressed', '#a02d16')])
        
        # Configura cor de fundo
        self.root.configure(bg=self.colors['light'])
        
    def create_widgets(self):
        """Cria os widgets da interface"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Configura o grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Header simplificado
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        header_frame.columnconfigure(0, weight=1)
        
        # TÃ­tulo principal
        title_label = ttk.Label(header_frame, text="Analisador de Bioimpedancia", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=(0, 5))
        
        # SubtÃ­tulo
        subtitle_label = ttk.Label(header_frame, 
                                  text="Controle completo de dados corporais",
                                  font=('Segoe UI', 10),
                                  foreground=self.colors['gray'])
        subtitle_label.grid(row=1, column=0, pady=(0, 10))
        
        # Notebook para abas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Aba 1: Entrada de Dados
        self.create_data_entry_tab()
        
        # Aba 2: Gerenciar Dados
        self.create_data_management_tab()
        
        # Aba 3: Dashboard
        self.create_dashboard_tab()
        
        # Status bar simplificado
        self.create_status_bar(main_frame)
        
        # Configura validacao
        self.setup_validation()
    
    def create_data_entry_tab(self):
        """Cria a aba de entrada de dados"""
        # Frame da aba
        entry_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(entry_frame, text="Entrada de Dados")
        
        # Configura o grid
        entry_frame.columnconfigure(0, weight=1)
        entry_frame.columnconfigure(1, weight=1)
        
        # Seção de arquivo (compacta)
        file_frame = ttk.LabelFrame(entry_frame, text="Arquivo", padding="10")
        file_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Label(file_frame, text="CSV:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.file_label = ttk.Label(file_frame, text=self.csv_file, 
                                   background=self.colors['light'], 
                                   relief="solid", 
                                   anchor="w",
                                   font=('Segoe UI', 9),
                                   padding=(8, 4))
        self.file_label.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(file_frame, text="Alterar", 
                  command=self.select_file,
                  style='Modern.TButton').grid(row=0, column=2)
        
        # Campos de entrada organizados
        self.create_data_fields(entry_frame)
        
        # Botões de ação
        self.create_action_buttons(entry_frame)
    
    def create_data_fields(self, parent):
        """Cria os campos de entrada de dados"""
        # Frame para campos
        fields_frame = ttk.LabelFrame(parent, text="Dados Corporais", padding="15")
        fields_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        fields_frame.columnconfigure(1, weight=1)
        fields_frame.columnconfigure(3, weight=1)
        
        # Campos organizados em duas colunas
        fields = [
            ("Data:", self.var_data, 0, "Hoje"),
            ("Peso (kg):", self.var_peso, 1, None),
            ("IMC:", self.var_imc, 2, None),
            ("Gordura (%):", self.var_gordura_pct, 3, None),
            ("Gordura (kg):", self.var_gordura_kg, 4, None),
            ("Massa Muscular (%):", self.var_massa_muscular_pct, 5, None),
            ("Massa Muscular (kg):", self.var_massa_muscular_kg, 6, None),
            ("Metabolismo (kcal/dia):", self.var_metabolismo, 7, None),
            ("Obesidade (%):", self.var_obesidade_pct, 8, None)
        ]
        
        for i, (label_text, var, row, button_text) in enumerate(fields):
            col = 0 if i < 5 else 2
            row_pos = i if i < 5 else i - 5
            
            # Label
            ttk.Label(fields_frame, text=label_text, 
                     font=('Segoe UI', 10)).grid(
                row=row_pos, column=col, sticky=tk.W, pady=5, padx=(0, 10))
            
            # Entry
            entry = ttk.Entry(fields_frame, textvariable=var, width=18, 
                            font=('Segoe UI', 10))
            entry.grid(row=row_pos, column=col + 1, sticky=(tk.W, tk.E), 
                     pady=5, padx=(0, 15))
            
            # Botão especial para data
            if button_text == "Hoje":
                ttk.Button(fields_frame, text=button_text, 
                          command=self.set_today,
                          style='Modern.TButton').grid(
                    row=row_pos, column=col + 2, padx=(5, 0), pady=5)
    
    def create_action_buttons(self, parent):
        """Cria os botões de ação"""
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Salvar Dados", 
                  command=self.save_data, 
                  style='Success.TButton').pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Limpar Campos", 
                  command=self.clear_fields,
                  style='Modern.TButton').pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Gerar Gráficos", 
                  command=self.generate_charts,
                  style='Modern.TButton').pack(side=tk.LEFT)
    
    def create_data_management_tab(self):
        """Cria a aba de gerenciamento de dados"""
        # Frame da aba
        mgmt_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(mgmt_frame, text="Gerenciar Dados")
        
        # Configura o grid
        mgmt_frame.columnconfigure(0, weight=1)
        mgmt_frame.rowconfigure(1, weight=1)
        
        # Botões de ação
        action_frame = ttk.Frame(mgmt_frame)
        action_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Button(action_frame, text="Atualizar Lista", 
                  command=self.refresh_management_data,
                  style='Modern.TButton').pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(action_frame, text="Adicionar Novo", 
                  command=self.add_new_data_quick,
                  style='Success.TButton').pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(action_frame, text="Limpar Todos os Dados", 
                  command=self.clear_all_data,
                  style='Danger.TButton').pack(side=tk.LEFT)
        
        # TreeView para dados
        self.create_data_tree(mgmt_frame)
    
    def create_data_tree(self, parent):
        """Cria a TreeView para gerenciar dados"""
        # Frame para a tabela
        table_frame = ttk.Frame(parent)
        table_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        
        # Treeview
        self.data_tree = ttk.Treeview(table_frame, yscrollcommand=v_scrollbar.set, 
                                     xscrollcommand=h_scrollbar.set, selectmode='browse')
        
        v_scrollbar.config(command=self.data_tree.yview)
        h_scrollbar.config(command=self.data_tree.xview)
        
        # Layout
        self.data_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Carrega os dados
        self.load_data_to_tree(self.data_tree)
        
        # Bind duplo clique para editar
        self.data_tree.bind('<Double-1>', lambda e: self.edit_selected_row(self.data_tree, self.root))
        
        # Menu de contexto
        self.create_context_menu()
    
    def create_context_menu(self):
        """Cria menu de contexto para a TreeView"""
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Editar", command=self.edit_selected_data)
        self.context_menu.add_command(label="Excluir", command=self.delete_selected_data)
        
        self.data_tree.bind("<Button-3>", self.show_context_menu)
    
    def show_context_menu(self, event):
        """Mostra menu de contexto"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def create_dashboard_tab(self):
        """Cria a aba de dashboard"""
        # Frame da aba
        dashboard_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(dashboard_frame, text="Dashboard")
        
        # Configura o grid
        dashboard_frame.columnconfigure(0, weight=1)
        dashboard_frame.columnconfigure(1, weight=1)
        
        # Métricas rápidas
        self.create_quick_metrics(dashboard_frame)
        
        # Botão para gerar gráficos
        ttk.Button(dashboard_frame, text="Gerar Relatório Completo", 
                  command=self.generate_charts,
                  style='Success.TButton').grid(row=1, column=0, columnspan=2, pady=20)
    
    def create_quick_metrics(self, parent):
        """Cria métricas rápidas no dashboard"""
        # Frame para métricas
        metrics_frame = ttk.LabelFrame(parent, text="Métricas Rápidas", padding="15")
        metrics_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Carrega métricas dos dados
        self.load_quick_metrics(metrics_frame)
    
    def load_quick_metrics(self, parent):
        """Carrega métricas rápidas dos dados"""
        try:
            if os.path.exists(self.csv_file):
                with open(self.csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                
                if rows:
                    # Calcula métricas
                    pesos = [float(row['peso']) for row in rows if row['peso']]
                    datas = [row['data'] for row in rows if row['data']]
                    
                    if pesos:
                        peso_atual = pesos[-1]
                        peso_anterior = pesos[-2] if len(pesos) > 1 else peso_atual
                        variacao = peso_atual - peso_anterior
                        
                        # Mostra métricas
                        ttk.Label(parent, text=f"Peso Atual: {peso_atual} kg", 
                                 font=('Segoe UI', 12, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
                        
                        ttk.Label(parent, text=f"Variação: {variacao:+.1f} kg", 
                                 font=('Segoe UI', 12),
                                 foreground=self.colors['success'] if variacao < 0 else self.colors['danger']).grid(row=1, column=0, sticky=tk.W, pady=5)
                        
                        ttk.Label(parent, text=f"Total de Registros: {len(rows)}", 
                                 font=('Segoe UI', 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
                        
                        ttk.Label(parent, text=f"Última Atualização: {datas[-1]}", 
                                 font=('Segoe UI', 10),
                                 foreground=self.colors['gray']).grid(row=3, column=0, sticky=tk.W, pady=5)
                else:
                    ttk.Label(parent, text="Nenhum dado encontrado", 
                             font=('Segoe UI', 12),
                             foreground=self.colors['gray']).grid(row=0, column=0, sticky=tk.W, pady=5)
        except Exception as e:
            ttk.Label(parent, text=f"Erro ao carregar métricas: {str(e)}", 
                     font=('Segoe UI', 12),
                     foreground=self.colors['danger']).grid(row=0, column=0, sticky=tk.W, pady=5)
    
    def create_status_bar(self, parent):
        """Cria barra de status simplificada"""
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_label = ttk.Label(status_frame, text="Pronto para adicionar novos dados", 
                                    font=('Segoe UI', 9),
                                    foreground=self.colors['success'])
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
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
            
            self.update_status(f"Dados salvos com sucesso! Data: {data['data']}, Peso: {data['peso']}kg", "success")
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
        """Abre uma janela para gerenciar os dados (CRUD)"""
        try:
            if not os.path.exists(self.csv_file):
                messagebox.showerror("Erro", "Arquivo CSV nao encontrado!")
                return
            
            # Cria nova janela
            view_window = tk.Toplevel(self.root)
            view_window.title("Gerenciador de Dados - CRUD")
            view_window.geometry("1000x600")
            view_window.resizable(True, True)
            
            # Frame principal
            main_frame = ttk.Frame(view_window)
            main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Frame superior com botÃÂµes
            button_frame = ttk.Frame(main_frame)
            button_frame.pack(fill=tk.X, pady=(0, 10))
            
            ttk.Button(button_frame, text="Atualizar Lista", 
                      command=lambda: self.refresh_data_tree(tree, view_window)).pack(side=tk.LEFT, padx=(0, 5))
            
            ttk.Button(button_frame, text="Editar Selecionado", 
                      command=lambda: self.edit_selected_row(tree, view_window)).pack(side=tk.LEFT, padx=(0, 5))
            
            ttk.Button(button_frame, text="Excluir Selecionado", 
                      command=lambda: self.delete_selected_row(tree, view_window)).pack(side=tk.LEFT, padx=(0, 5))
            
            ttk.Button(button_frame, text="Adicionar Novo", 
                      command=lambda: self.add_new_row_from_manager(view_window)).pack(side=tk.LEFT, padx=(0, 5))
            
            # Frame para a tabela
            table_frame = ttk.Frame(main_frame)
            table_frame.pack(fill=tk.BOTH, expand=True)
            
            # Scrollbars
            v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
            h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
            
            # Treeview
            tree = ttk.Treeview(table_frame, yscrollcommand=v_scrollbar.set, 
                               xscrollcommand=h_scrollbar.set, selectmode='browse')
            
            v_scrollbar.config(command=tree.yview)
            h_scrollbar.config(command=tree.xview)
            
            # Layout
            tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
            h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
            
            table_frame.columnconfigure(0, weight=1)
            table_frame.rowconfigure(0, weight=1)
            
            # Carrega os dados
            self.load_data_to_tree(tree)
            
            # Bind duplo clique para editar
            tree.bind('<Double-1>', lambda e: self.edit_selected_row(tree, view_window))
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao visualizar dados: {str(e)}")
    
    def load_data_to_tree(self, tree):
        """Carrega os dados do CSV na TreeView"""
        try:
            # Limpa a tree
            for item in tree.get_children():
                tree.delete(item)
            
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                columns = reader.fieldnames
                
                # Configura as colunas
                tree['columns'] = columns
                tree['show'] = 'headings'
                
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=120, minwidth=80)
                
                # Adiciona os dados
                for i, row in enumerate(reader):
                    values = [row[col] for col in columns]
                    tree.insert('', tk.END, iid=i, values=values)
                    
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {str(e)}")
    
    def refresh_data_tree(self, tree, parent_window):
        """Atualiza a TreeView com os dados mais recentes"""
        self.load_data_to_tree(tree)
        self.update_status("Lista de dados atualizada")
    
    def edit_selected_row(self, tree, parent_window):
        """Edita a linha selecionada"""
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma linha para editar")
            return
        
        # Pega os dados da linha selecionada
        item = tree.item(selected[0])
        values = item['values']
        
        # Cria janela de ediÃÂ§ÃÂ£o
        edit_window = tk.Toplevel(parent_window)
        edit_window.title("Editar Dados")
        edit_window.geometry("500x600")
        edit_window.transient(parent_window)
        edit_window.grab_set()
        
        # Frame principal
        edit_frame = ttk.Frame(edit_window, padding="20")
        edit_frame.pack(fill=tk.BOTH, expand=True)
        
        # VariÃÂ¡veis para os campos
        edit_vars = {}
        columns = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                  'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
        
        for i, col in enumerate(columns):
            edit_vars[col] = tk.StringVar(value=values[i] if i < len(values) else "")
        
        # Cria os campos de entrada
        row = 0
        for col in columns:
            ttk.Label(edit_frame, text=f"{col.replace('_', ' ').title()}:").grid(
                row=row, column=0, sticky=tk.W, pady=5)
            ttk.Entry(edit_frame, textvariable=edit_vars[col], width=30).grid(
                row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
            row += 1
        
        # Frame para botÃÂµes
        button_frame = ttk.Frame(edit_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        
        def save_edit():
            """Salva as alteracoes"""
            try:
                # Valida os dados
                errors = []
                if not edit_vars['data'].get():
                    errors.append("Data e obrigatoria")
                if not edit_vars['peso'].get():
                    errors.append("Peso e obrigatorio")
                
                if errors:
                    messagebox.showerror("Erro", "\n".join(errors))
                    return
                
                # LÃÂª todos os dados
                with open(self.csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                
                # Atualiza a linha selecionada
                row_index = int(selected[0])
                if 0 <= row_index < len(rows):
                    for col in columns:
                        rows[row_index][col] = edit_vars[col].get()
                    
                    # Salva de volta
                    with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=columns)
                        writer.writeheader()
                        writer.writerows(rows)
                    
                    messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
                    edit_window.destroy()
                    self.refresh_data_tree(tree, parent_window)
                    self.update_status("Dados editados com sucesso")
                else:
                    messagebox.showerror("Erro", "ÃÂndice de linha invÃÂ¡lido")
                    
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar alteraÃÂ§ÃÂµes: {str(e)}")
        
        ttk.Button(button_frame, text="Salvar", command=save_edit).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Cancelar", command=edit_window.destroy).pack(side=tk.LEFT)
    
    def delete_selected_row(self, tree, parent_window):
        """Exclui a linha selecionada"""
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma linha para excluir")
            return
        
        # Confirma a exclusÃÂ£o
        item = tree.item(selected[0])
        values = item['values']
        data_str = f"Data: {values[0]}, Peso: {values[1]}kg"
        
        if messagebox.askyesno("Confirmar ExclusÃÂ£o", 
                              f"Tem certeza que deseja excluir esta entrada?\n\n{data_str}"):
            try:
                # LÃÂª todos os dados
                with open(self.csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                    columns = reader.fieldnames
                
                # Remove a linha selecionada
                row_index = int(selected[0])
                if 0 <= row_index < len(rows):
                    del rows[row_index]
                    
                    # Salva de volta
                    with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=columns)
                        writer.writeheader()
                        writer.writerows(rows)
                    
                    messagebox.showinfo("Sucesso", "Linha excluÃÂ­da com sucesso!")
                    self.refresh_data_tree(tree, parent_window)
                    self.update_status("Linha excluÃÂ­da com sucesso")
                else:
                    messagebox.showerror("Erro", "ÃÂndice de linha invÃÂ¡lido")
                    
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir linha: {str(e)}")
    
    def add_new_row_from_manager(self, parent_window):
        """Abre janela para adicionar nova linha a partir do gerenciador"""
        # Cria uma janela de entrada rÃÂ¡pida
        add_window = tk.Toplevel(parent_window)
        add_window.title("Adicionar Nova Entrada")
        add_window.geometry("400x500")
        add_window.transient(parent_window)
        add_window.grab_set()
        
        # Frame principal
        add_frame = ttk.Frame(add_window, padding="20")
        add_frame.pack(fill=tk.BOTH, expand=True)
        
        # VariÃÂ¡veis para os campos
        add_vars = {}
        columns = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                  'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
        
        for col in columns:
            add_vars[col] = tk.StringVar()
        
        # Define data de hoje por padrÃÂ£o
        add_vars['data'].set(date.today().strftime("%Y-%m-%d"))
        
        # Cria os campos de entrada
        row = 0
        for col in columns:
            ttk.Label(add_frame, text=f"{col.replace('_', ' ').title()}:").grid(
                row=row, column=0, sticky=tk.W, pady=5)
            ttk.Entry(add_frame, textvariable=add_vars[col], width=25).grid(
                row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
            row += 1
        
        # Frame para botÃÂµes
        button_frame = ttk.Frame(add_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        
        def save_new():
            """Salva a nova entrada"""
            try:
                # Valida os dados
                errors = []
                if not add_vars['data'].get():
                    errors.append("Data e obrigatoria")
                if not add_vars['peso'].get():
                    errors.append("Peso e obrigatorio")
                
                if errors:
                    messagebox.showerror("Erro", "\n".join(errors))
                    return
                
                # Prepara os dados
                data = {}
                for col in columns:
                    data[col] = add_vars[col].get() or ''
                
                # Salva no arquivo
                file_exists = os.path.exists(self.csv_file)
                with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=columns)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(data)
                
                messagebox.showinfo("Sucesso", "Nova entrada adicionada com sucesso!")
                add_window.destroy()
                
                # Atualiza a lista no gerenciador
                for widget in parent_window.winfo_children():
                    if isinstance(widget, ttk.Frame):
                        for child in widget.winfo_children():
                            if isinstance(child, ttk.Treeview):
                                self.load_data_to_tree(child)
                                break
                
                self.update_status(f"Nova entrada adicionada: {data['data']} - {data['peso']}kg")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar nova entrada: {str(e)}")
        
        ttk.Button(button_frame, text="Salvar", command=save_new).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Cancelar", command=add_window.destroy).pack(side=tk.LEFT)
    
    def clear_all_data(self):
        """Limpa todos os dados do arquivo CSV"""
        if not os.path.exists(self.csv_file):
            messagebox.showwarning("Aviso", "Arquivo CSV nÃÂ£o encontrado!")
            return
        
        # Confirma a operaÃÂ§ÃÂ£o
        if messagebox.askyesno("Confirmar Limpeza", 
                              "Tem certeza que deseja APAGAR TODOS os dados?\n\nEsta operaÃÂ§ÃÂ£o nÃÂ£o pode ser desfeita!"):
            try:
                # Cria um arquivo vazio com apenas o cabeÃÂ§alho
                columns = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                          'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
                
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=columns)
                    writer.writeheader()
                
                messagebox.showinfo("Sucesso", "Todos os dados foram removidos!")
                self.update_status("Arquivo CSV limpo - todos os dados removidos")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao limpar dados: {str(e)}")
    
    def refresh_management_data(self):
        """Atualiza os dados na aba de gerenciamento"""
        self.load_data_to_tree(self.data_tree)
        self.update_status("Lista de dados atualizada", "success")
    
    def add_new_data_quick(self):
        """Adiciona novo dado rapidamente"""
        # Muda para a aba de entrada de dados
        self.notebook.select(0)
        self.update_status("Pronto para adicionar novo dado", "info")
    
    def edit_selected_data(self):
        """Edita o dado selecionado"""
        selected = self.data_tree.selection()
        if selected:
            self.edit_selected_row(self.data_tree, self.root)
        else:
            messagebox.showwarning("Aviso", "Selecione uma linha para editar")
    
    def delete_selected_data(self):
        """Exclui o dado selecionado"""
        selected = self.data_tree.selection()
        if selected:
            self.delete_selected_row(self.data_tree, self.root)
        else:
            messagebox.showwarning("Aviso", "Selecione uma linha para excluir")
    
    def update_status(self, message, status_type="info"):
        """Atualiza a mensagem de status com Ã­cones"""
        icons = {
            "info": "??",
            "success": "?",
            "warning": "??",
            "error": "?",
            "loading": "?"
        }
        
        icon = icons.get(status_type, "??")
        colored_message = f"{icon} {message}"
        
        # Atualiza cor baseada no tipo
        colors = {
            "info": self.colors['primary'],
            "success": self.colors['success'],
            "warning": self.colors['secondary'],
            "error": self.colors['danger'],
            "loading": self.colors['gray']
        }
        
        self.status_label.config(
            text=colored_message,
            foreground=colors.get(status_type, self.colors['primary'])
        )
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
