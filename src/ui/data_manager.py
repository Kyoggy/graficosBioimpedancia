#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerenciador de Dados para Interface Moderna
Funcionalidades CRUD para dados de bioimpedância
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import csv
import os
from datetime import datetime, date

class DataManager:
    def __init__(self, parent_gui):
        self.parent = parent_gui
        # Caminho para o arquivo de dados (relativo ao diretório do projeto)
        self.csv_file = "data/raw/dados_bioimpedancia.csv"
        self.data = parent_gui.data
        
    def create_data_entry_tab(self, parent):
        """Cria a aba de entrada de dados"""
        # Frame principal
        main_frame = ctk.CTkFrame(parent)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="📝 Entrada de Dados de Bioimpedância",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.parent.colors['primary']
        )
        title_label.pack(pady=(20, 30))
        
        # Formulário de entrada
        form_frame = ctk.CTkFrame(main_frame)
        form_frame.pack(fill="x", padx=20, pady=20)
        
        # Variáveis para os campos
        self.entry_vars = {}
        fields = [
            ('data', 'Data (YYYY-MM-DD)', '2025-01-01'),
            ('peso', 'Peso (kg)', '70.0'),
            ('imc', 'IMC', '24.5'),
            ('Gordura/porcento', 'Gordura (%)', '18.5'),
            ('Gordura/KG', 'Gordura (kg)', '13.0'),
            ('Massa Musucular/porcento', 'Massa Muscular (%)', '45.0'),
            ('Massa Muscular/KG', 'Massa Muscular (kg)', '31.5'),
            ('Metabolismo', 'Metabolismo (kcal/dia)', '1650'),
            ('Obesidade/porcento', 'Obesidade (%)', '15.0')
        ]
        
        # Cria os campos
        for i, (field, label, placeholder) in enumerate(fields):
            row = i // 2
            col = (i % 2) * 2
            
            # Label
            field_label = ctk.CTkLabel(
                form_frame,
                text=label,
                font=ctk.CTkFont(size=12, weight="bold")
            )
            field_label.grid(row=row, column=col, padx=10, pady=10, sticky="w")
            
            # Entry
            self.entry_vars[field] = ctk.StringVar(value=placeholder)
            entry = ctk.CTkEntry(
                form_frame,
                textvariable=self.entry_vars[field],
                width=200,
                height=35
            )
            entry.grid(row=row, column=col+1, padx=10, pady=10, sticky="ew")
        
        # Configura o grid
        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(3, weight=1)
        
        # Botão especial para data de hoje
        today_button = ctk.CTkButton(
            form_frame,
            text="📅 Hoje",
            command=self.set_today_date,
            width=100,
            height=35
        )
        today_button.grid(row=len(fields)//2, column=2, padx=10, pady=10)
        
        # Botões de ação
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", padx=20, pady=20)
        
        add_button = ctk.CTkButton(
            button_frame,
            text="➕ Adicionar Dados",
            command=self.add_data,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        add_button.pack(side="left", padx=10)
        
        clear_button = ctk.CTkButton(
            button_frame,
            text="🗑️ Limpar Campos",
            command=self.clear_fields,
            width=150,
            height=40
        )
        clear_button.pack(side="left", padx=10)
        
        # Botão removido - sempre usa o arquivo fixo
        
        return main_frame
    
    def create_data_management_tab(self, parent):
        """Cria a aba de gerenciamento de dados"""
        # Frame principal
        main_frame = ctk.CTkFrame(parent)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="📊 Gerenciamento de Dados",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.parent.colors['primary']
        )
        title_label.pack(pady=(20, 20))
        
        # Botões de ação
        action_frame = ctk.CTkFrame(main_frame)
        action_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        refresh_button = ctk.CTkButton(
            action_frame,
            text="🔄 Atualizar",
            command=self.refresh_data_table,
            width=120,
            height=35
        )
        refresh_button.pack(side="left", padx=10)
        
        export_button = ctk.CTkButton(
            action_frame,
            text="💾 Exportar CSV",
            command=self.export_data,
            width=120,
            height=35
        )
        export_button.pack(side="left", padx=10)
        
        clear_all_button = ctk.CTkButton(
            action_frame,
            text="🗑️ Limpar Todos",
            command=self.clear_all_data,
            width=120,
            height=35,
            fg_color="#dc3545",
            hover_color="#c82333"
        )
        clear_all_button.pack(side="right", padx=10)
        
        # Frame para a tabela
        table_frame = ctk.CTkFrame(main_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Cria a tabela usando tkinter Treeview
        self.create_data_table(table_frame)
        
        return main_frame
    
    def create_data_table(self, parent):
        """Cria a tabela de dados"""
        # Frame para a tabela
        table_container = ctk.CTkFrame(parent)
        table_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ctk.CTkScrollbar(table_container)
        scrollbar.pack(side="right", fill="y")
        
        # Treeview
        columns = ['Data', 'Peso', 'IMC', 'Gordura%', 'GorduraKG', 'Massa%', 'MassaKG', 'Metabolismo', 'Obesidade%']
        self.data_tree = tk.ttk.Treeview(
            table_container,
            columns=columns,
            show='headings',
            yscrollcommand=scrollbar.set,
            height=15
        )
        
        # Configura as colunas
        for col in columns:
            self.data_tree.heading(col, text=col)
            self.data_tree.column(col, width=100, anchor="center")
        
        self.data_tree.pack(side="left", fill="both", expand=True)
        scrollbar.configure(command=self.data_tree.yview)
        
        # Bind para edição
        self.data_tree.bind("<Double-1>", self.edit_selected_row)
        self.data_tree.bind("<Delete>", self.delete_selected_row)
        
        # Botões de ação da tabela
        table_buttons = ctk.CTkFrame(parent)
        table_buttons.pack(fill="x", padx=20, pady=(0, 10))
        
        edit_button = ctk.CTkButton(
            table_buttons,
            text="✏️ Editar Selecionado",
            command=self.edit_selected_row,
            width=150,
            height=35
        )
        edit_button.pack(side="left", padx=10)
        
        delete_button = ctk.CTkButton(
            table_buttons,
            text="🗑️ Excluir Selecionado",
            command=self.delete_selected_row,
            width=150,
            height=35,
            fg_color="#dc3545",
            hover_color="#c82333"
        )
        delete_button.pack(side="left", padx=10)
        
        # Carrega os dados na tabela
        self.refresh_data_table()
    
    def set_today_date(self):
        """Define a data de hoje"""
        today = date.today().strftime("%Y-%m-%d")
        self.entry_vars['data'].set(today)
    
    def clear_fields(self):
        """Limpa todos os campos do formulário"""
        for var in self.entry_vars.values():
            var.set("")
    
    def add_data(self):
        """Adiciona novos dados ao CSV"""
        try:
            # Valida os dados
            data_dict = {}
            for field, var in self.entry_vars.items():
                value = var.get().strip()
                if not value:
                    messagebox.showerror("Erro", f"Campo obrigatório vazio: {field}")
                    return
                data_dict[field] = value
            
            # Converte data
            try:
                datetime.strptime(data_dict['data'], '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Erro", "Formato de data inválido. Use YYYY-MM-DD")
                return
            
            # Converte valores numéricos
            numeric_fields = ['peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                            'Massa Musucular/porcento', 'Massa Muscular/KG', 
                            'Metabolismo', 'Obesidade/porcento']
            
            for field in numeric_fields:
                try:
                    float(data_dict[field])
                except ValueError:
                    messagebox.showerror("Erro", f"Valor numérico inválido: {field}")
                    return
            
            # Adiciona ao CSV
            file_exists = os.path.exists(self.csv_file)
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data_dict.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data_dict)
            
            messagebox.showinfo("Sucesso", "Dados adicionados com sucesso!")
            self.clear_fields()
            self.parent.load_data()  # Recarrega os dados
            self.refresh_data_table()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar dados: {e}")
    
    # Método removido - sempre usa o arquivo fixo
    
    def refresh_data_table(self):
        """Atualiza a tabela de dados"""
        # Limpa a tabela
        for item in self.data_tree.get_children():
            self.data_tree.delete(item)
        
        # Carrega os dados
        if self.parent.data is not None:
            for _, row in self.parent.data.iterrows():
                values = [
                    row['data'].strftime('%Y-%m-%d') if pd.notna(row['data']) else '',
                    f"{row['peso']:.1f}" if pd.notna(row['peso']) else '',
                    f"{row['imc']:.1f}" if pd.notna(row['imc']) else '',
                    f"{row.get('Gordura/porcento', ''):.1f}" if pd.notna(row.get('Gordura/porcento', '')) else '',
                    f"{row.get('Gordura/KG', ''):.1f}" if pd.notna(row.get('Gordura/KG', '')) else '',
                    f"{row.get('Massa Musucular/porcento', ''):.1f}" if pd.notna(row.get('Massa Musucular/porcento', '')) else '',
                    f"{row.get('Massa Muscular/KG', ''):.1f}" if pd.notna(row.get('Massa Muscular/KG', '')) else '',
                    f"{row.get('Metabolismo', ''):.0f}" if pd.notna(row.get('Metabolismo', '')) else '',
                    f"{row.get('Obesidade/porcento', ''):.1f}" if pd.notna(row.get('Obesidade/porcento', '')) else ''
                ]
                self.data_tree.insert('', 'end', values=values)
    
    def edit_selected_row(self, event=None):
        """Edita a linha selecionada"""
        selection = self.data_tree.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma linha para editar")
            return
        
        # Pega os dados da linha selecionada
        item = self.data_tree.item(selection[0])
        values = item['values']
        
        # Cria janela de edição
        edit_window = ctk.CTkToplevel(self.parent.root)
        edit_window.title("Editar Dados")
        edit_window.geometry("600x700")
        edit_window.transient(self.parent.root)
        
        # Centraliza a janela
        edit_window.update_idletasks()
        x = (edit_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (edit_window.winfo_screenheight() // 2) - (700 // 2)
        edit_window.geometry(f"600x700+{x}+{y}")
        
        # Força a janela a aparecer antes de fazer grab_set
        edit_window.lift()
        edit_window.focus_force()
        edit_window.grab_set()
        
        # Frame principal
        main_frame = ctk.CTkFrame(edit_window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="✏️ Editar Dados de Bioimpedância",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.parent.colors['primary']
        )
        title_label.pack(pady=(0, 20))
        
        # Formulário de edição
        form_frame = ctk.CTkScrollableFrame(main_frame, width=550, height=400)
        form_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Variáveis para os campos
        edit_vars = {}
        fields = [
            ('data', 'Data (YYYY-MM-DD)'),
            ('peso', 'Peso (kg)'),
            ('imc', 'IMC'),
            ('Gordura/porcento', 'Gordura (%)'),
            ('Gordura/KG', 'Gordura (kg)'),
            ('Massa Musucular/porcento', 'Massa Muscular (%)'),
            ('Massa Muscular/KG', 'Massa Muscular (kg)'),
            ('Metabolismo', 'Metabolismo (kcal/dia)'),
            ('Obesidade/porcento', 'Obesidade (%)')
        ]
        
        # Cria os campos com valores atuais
        for i, (field, label) in enumerate(fields):
            # Label
            field_label = ctk.CTkLabel(
                form_frame,
                text=label,
                font=ctk.CTkFont(size=12, weight="bold")
            )
            field_label.pack(pady=(10, 5), anchor="w")
            
            # Entry com valor atual
            current_value = values[i] if i < len(values) else ""
            edit_vars[field] = ctk.StringVar(value=current_value)
            entry = ctk.CTkEntry(
                form_frame,
                textvariable=edit_vars[field],
                width=500,
                height=35,
                placeholder_text=f"Digite {label.lower()}"
            )
            entry.pack(pady=(0, 10), fill="x")
        
        # Botão especial para data de hoje
        today_button = ctk.CTkButton(
            form_frame,
            text="📅 Usar Data de Hoje",
            command=lambda: edit_vars['data'].set(date.today().strftime("%Y-%m-%d")),
            width=200,
            height=35
        )
        today_button.pack(pady=10)
        
        # Botões
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", padx=10, pady=20)
        
        def save_edit():
            try:
                # Valida os dados
                data_dict = {}
                for field, var in edit_vars.items():
                    value = var.get().strip()
                    if not value:
                        messagebox.showerror("Erro", f"Campo obrigatório vazio: {field}")
                        return
                    data_dict[field] = value
                
                # Converte data
                try:
                    datetime.strptime(data_dict['data'], '%Y-%m-%d')
                except ValueError:
                    messagebox.showerror("Erro", "Formato de data inválido. Use YYYY-MM-DD")
                    return
                
                # Converte valores numéricos
                numeric_fields = ['peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                                'Massa Musucular/porcento', 'Massa Muscular/KG', 
                                'Metabolismo', 'Obesidade/porcento']
                
                for field in numeric_fields:
                    try:
                        float(data_dict[field])
                    except ValueError:
                        messagebox.showerror("Erro", f"Valor numérico inválido: {field}")
                        return
                
                # Atualiza o CSV
                self.update_csv_row(selection[0], data_dict)
                
                messagebox.showinfo("Sucesso", "Dados editados com sucesso!")
                edit_window.destroy()
                self.refresh_data_table()
                self.parent.load_data()  # Recarrega os dados
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar alterações: {e}")
        
        save_button = ctk.CTkButton(
            button_frame,
            text="💾 Salvar",
            command=save_edit,
            width=120,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        save_button.pack(side="left", padx=10)
        
        cancel_button = ctk.CTkButton(
            button_frame,
            text="❌ Cancelar",
            command=edit_window.destroy,
            width=120,
            height=40
        )
        cancel_button.pack(side="right", padx=10)
    
    def delete_selected_row(self, event=None):
        """Exclui a linha selecionada"""
        selection = self.data_tree.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma linha para excluir")
            return
        
        # Pega os dados da linha para mostrar na confirmação
        item = self.data_tree.item(selection[0])
        values = item['values']
        data_str = f"Data: {values[0]}, Peso: {values[1]}kg"
        
        if messagebox.askyesno("Confirmar Exclusão", 
                              f"Tem certeza que deseja excluir esta entrada?\n\n{data_str}"):
            try:
                # Remove a linha do CSV
                self.remove_csv_row(selection[0])
                
                messagebox.showinfo("Sucesso", "Linha excluída com sucesso!")
                self.refresh_data_table()
                self.parent.load_data()  # Recarrega os dados
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir linha: {e}")
    
    def export_data(self):
        """Exporta os dados para CSV"""
        if self.parent.data is None:
            messagebox.showwarning("Aviso", "Nenhum dado para exportar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Salvar arquivo CSV",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.parent.data.to_csv(file_path, index=False, encoding='utf-8')
                messagebox.showinfo("Sucesso", f"Dados exportados para: {file_path}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao exportar: {e}")
    
    def clear_all_data(self):
        """Limpa todos os dados"""
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja APAGAR TODOS os dados?\n\nEsta operação não pode ser desfeita!"):
            try:
                # Cria arquivo vazio com cabeçalho
                columns = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                          'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
                
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(columns)
                
                messagebox.showinfo("Sucesso", "Todos os dados foram removidos")
                self.parent.load_data()
                self.refresh_data_table()
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao limpar dados: {e}")
    
    def update_csv_row(self, row_index, new_data):
        """Atualiza uma linha específica no CSV"""
        try:
            # Lê todos os dados
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
            
            # Atualiza a linha específica
            if 0 <= row_index < len(rows):
                rows[row_index] = new_data
                
                # Escreve de volta
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=new_data.keys())
                    writer.writeheader()
                    writer.writerows(rows)
            else:
                raise IndexError("Índice de linha inválido")
                
        except Exception as e:
            raise Exception(f"Erro ao atualizar linha: {e}")
    
    def remove_csv_row(self, row_index):
        """Remove uma linha específica do CSV"""
        try:
            # Lê todos os dados
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
            
            # Remove a linha específica
            if 0 <= row_index < len(rows):
                del rows[row_index]
                
                # Escreve de volta
                if rows:  # Se ainda há dados
                    with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
                        writer.writeheader()
                        writer.writerows(rows)
                else:  # Se não há mais dados, cria arquivo vazio com cabeçalho
                    columns = ['data', 'peso', 'imc', 'Gordura/porcento', 'Gordura/KG', 
                              'Massa Musucular/porcento', 'Massa Muscular/KG', 'Metabolismo', 'Obesidade/porcento']
                    with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(columns)
            else:
                raise IndexError("Índice de linha inválido")
                
        except Exception as e:
            raise Exception(f"Erro ao remover linha: {e}")
