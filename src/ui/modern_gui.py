#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Desktop Moderna do Analisador de Bioimpedancia
Usando CustomTkinter para uma experiencia desktop moderna e elegante
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import seaborn as sns
import sys
import os
from datetime import datetime, date
import numpy as np

# Adiciona o diretorio core ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))

from bioimpedance_analyzer import BioimpedanceAnalyzer
import sys
import os
sys.path.append(os.path.dirname(__file__))
import data_manager

# Configuracao do tema
ctk.set_appearance_mode("light")  # "light" ou "dark"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class ModernBioimpedanceGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Analisador de Bioimpedância - Professional Edition")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        
        # Variaveis
        self.data = None
        # Caminho para o arquivo de dados (relativo ao diretório do projeto)
        self.csv_file = "data/raw/dados_bioimpedancia.csv"
        self.current_chart = "weight"
        self.data_frame = None  # Para a tabela de dados
        
        # Configuracao do estilo
        self.setup_styles()
        
        # Cria a interface
        self.create_widgets()
        
        # Carrega dados iniciais
        self.load_data()
    
    def setup_styles(self):
        """Configura estilos personalizados"""
        # Cores personalizadas
        self.colors = {
            'primary': '#2E86AB',
            'secondary': '#A23B72', 
            'success': '#F18F01',
            'warning': '#C73E1D',
            'background': '#F8F9FA',
            'surface': '#FFFFFF',
            'text': '#2C3E50'
        }
    
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cabecalho
        self.create_header()
        
        # Cria o gerenciador de dados
        self.data_manager = data_manager.DataManager(self)
        
        # Cria as abas
        self.create_tabs()
        
        # Rodape
        self.create_footer()
    
    def create_header(self):
        """Cria o cabecalho da aplicacao"""
        header_frame = ctk.CTkFrame(self.main_frame, height=80)
        header_frame.pack(fill="x", padx=10, pady=(10, 5))
        header_frame.pack_propagate(False)
        
        # Titulo principal
        title_label = ctk.CTkLabel(
            header_frame,
            text="Analisador de Bioimpedancia",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=self.colors['primary']
        )
        title_label.pack(side="left", padx=20, pady=20)
        
        # Subtitulo
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Professional Edition - Interface Moderna",
            font=ctk.CTkFont(size=14),
            text_color=self.colors['text']
        )
        subtitle_label.pack(side="left", padx=(0, 20), pady=20)
        
        # Botao de carregar dados
        # Botão removido - sempre usa o arquivo fixo
    
    def create_tabs(self):
        """Cria o sistema de abas"""
        # Frame para as abas
        self.tab_frame = ctk.CTkFrame(self.main_frame)
        self.tab_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Cria o notebook (sistema de abas)
        self.notebook = tk.ttk.Notebook(self.tab_frame)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Aba 1: Visualização de Gráficos (Principal)
        self.visualization_tab = ctk.CTkFrame(self.notebook)
        self.notebook.add(self.visualization_tab, text="📈 Gráficos")
        self.create_visualization_tab(self.visualization_tab)
        
        # Aba 2: Dashboard
        self.dashboard_tab = ctk.CTkFrame(self.notebook)
        self.notebook.add(self.dashboard_tab, text="📊 Dashboard")
        self.create_dashboard_tab(self.dashboard_tab)
        
        # Aba 3: Entrada de Dados
        self.entry_tab = ctk.CTkFrame(self.notebook)
        self.notebook.add(self.entry_tab, text="📝 Entrada de Dados")
        self.data_manager.create_data_entry_tab(self.entry_tab)
        
        # Aba 4: Gerenciamento de Dados
        self.management_tab = ctk.CTkFrame(self.notebook)
        self.notebook.add(self.management_tab, text="📊 Gerenciar Dados")
        self.data_manager.create_data_management_tab(self.management_tab)
    
    def create_visualization_tab(self, parent):
        """Cria a aba de visualização de gráficos"""
        # Layout em duas colunas
        left_frame = ctk.CTkFrame(parent, width=300)
        left_frame.pack(side="left", fill="y", padx=(10, 5), pady=10)
        left_frame.pack_propagate(False)
        
        right_frame = ctk.CTkFrame(parent)
        right_frame.pack(side="right", fill="both", expand=True, padx=(5, 10), pady=10)
        
        # Painel esquerdo - Controles
        self.create_control_panel(left_frame)
        
        # Painel direito - Visualizacao
        self.create_visualization_panel(right_frame)
    
    def create_dashboard_tab(self, parent):
        """Cria a aba de dashboard"""
        # Título
        title_label = ctk.CTkLabel(
            parent,
            text="📊 Dashboard de Composição Corporal",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.colors['primary']
        )
        title_label.pack(pady=(20, 20))
        
        # Métricas rápidas
        self.create_quick_metrics(parent)
        
        # Botão para gerar gráficos
        generate_button = ctk.CTkButton(
            parent,
            text="🔄 Gerar Todos os Gráficos",
            command=self.generate_all_charts,
            width=200,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        generate_button.pack(pady=20)
    
    def create_quick_metrics(self, parent):
        """Cria métricas rápidas"""
        if self.data is None:
            no_data_label = ctk.CTkLabel(
                parent,
                text="Nenhum dado carregado",
                font=ctk.CTkFont(size=14),
                text_color=self.colors['text']
            )
            no_data_label.pack(pady=50)
            return
        
        # Frame para métricas
        metrics_frame = ctk.CTkFrame(parent)
        metrics_frame.pack(fill="x", padx=20, pady=20)
        
        # Cria 4 colunas de métricas
        col1, col2, col3, col4 = ctk.CTkFrame(metrics_frame), ctk.CTkFrame(metrics_frame), ctk.CTkFrame(metrics_frame), ctk.CTkFrame(metrics_frame)
        
        for i, frame in enumerate([col1, col2, col3, col4]):
            frame.pack(side="left", fill="both", expand=True, padx=5, pady=10)
        
        # Peso atual
        peso_atual = self.data['peso'].iloc[-1]
        peso_inicial = self.data['peso'].iloc[0]
        peso_mudanca = peso_atual - peso_inicial
        
        ctk.CTkLabel(col1, text="Peso Atual", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        ctk.CTkLabel(col1, text=f"{peso_atual:.1f} kg", font=ctk.CTkFont(size=16, weight="bold")).pack()
        ctk.CTkLabel(col1, text=f"{peso_mudanca:+.1f} kg", font=ctk.CTkFont(size=12), 
                    text_color="green" if peso_mudanca < 0 else "red").pack()
        
        # IMC atual
        imc_atual = self.data['imc'].iloc[-1]
        imc_inicial = self.data['imc'].iloc[0]
        imc_mudanca = imc_atual - imc_inicial
        
        ctk.CTkLabel(col2, text="IMC Atual", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        ctk.CTkLabel(col2, text=f"{imc_atual:.1f}", font=ctk.CTkFont(size=16, weight="bold")).pack()
        ctk.CTkLabel(col2, text=f"{imc_mudanca:+.1f}", font=ctk.CTkFont(size=12),
                    text_color="green" if imc_mudanca < 0 else "red").pack()
        
        # Total de medições
        total_medicoes = len(self.data)
        periodo_dias = (self.data['data'].max() - self.data['data'].min()).days
        
        ctk.CTkLabel(col3, text="Medições", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        ctk.CTkLabel(col3, text=f"{total_medicoes}", font=ctk.CTkFont(size=16, weight="bold")).pack()
        ctk.CTkLabel(col3, text=f"{periodo_dias} dias", font=ctk.CTkFont(size=12)).pack()
        
        # Metabolismo (se disponível)
        if 'Metabolismo' in self.data.columns:
            metab_atual = self.data['Metabolismo'].iloc[-1]
            ctk.CTkLabel(col4, text="Metabolismo", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
            ctk.CTkLabel(col4, text=f"{metab_atual:.0f} kcal", font=ctk.CTkFont(size=16, weight="bold")).pack()
            ctk.CTkLabel(col4, text="por dia", font=ctk.CTkFont(size=12)).pack()
        else:
            ctk.CTkLabel(col4, text="Dados", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
            ctk.CTkLabel(col4, text="Disponíveis", font=ctk.CTkFont(size=16, weight="bold")).pack()
            ctk.CTkLabel(col4, text="Completos", font=ctk.CTkFont(size=12)).pack()
    
    def generate_all_charts(self):
        """Gera todos os gráficos"""
        if self.data is None:
            messagebox.showwarning("Aviso", "Nenhum dado carregado!")
            return
        
        try:
            # Muda para a aba de gráficos (primeira aba)
            self.notebook.select(0)  # Índice da aba de gráficos
            
            # Gera o gráfico de evolução do peso
            self.current_chart = "evolucao_do_peso"
            self.generate_chart()
            
            messagebox.showinfo("Sucesso", "Gráficos gerados! Verifique a aba 'Gráficos'")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar gráficos: {e}")
    
    def create_control_panel(self, parent):
        """Cria o painel de controles"""
        
        # Titulo do painel
        panel_title = ctk.CTkLabel(
            parent,
            text="Controles",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors['primary']
        )
        panel_title.pack(pady=(20, 10))
        
        # Seletor de grafico
        chart_label = ctk.CTkLabel(
            parent,
            text="Escolha o grafico:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        chart_label.pack(pady=(20, 5))
        
        self.chart_var = ctk.StringVar(value="Evolucao do Peso")
        self.chart_selector = ctk.CTkComboBox(
            parent,
            values=[
                "Evolucao do Peso",
                "Composicao Corporal", 
                "Analise de IMC",
                "Metabolismo",
                "Dashboard Completo"
            ],
            variable=self.chart_var,
            command=self.on_chart_change,
            width=250,
            height=35
        )
        self.chart_selector.pack(pady=5)
        
        # Botao para gerar grafico
        generate_button = ctk.CTkButton(
            parent,
            text="Gerar Grafico",
            command=self.generate_chart,
            width=250,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        generate_button.pack(pady=20)
        
        # Informacoes dos dados
        info_frame = ctk.CTkFrame(parent)
        info_frame.pack(fill="x", padx=10, pady=20)
        
        info_title = ctk.CTkLabel(
            info_frame,
            text="Informacoes",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.colors['primary']
        )
        info_title.pack(pady=(10, 5))
        
        self.info_text = ctk.CTkTextbox(
            info_frame,
            width=250,
            height=150,
            font=ctk.CTkFont(size=12)
        )
        self.info_text.pack(pady=(0, 10), padx=10)
        
        # Botoes de acao
        action_frame = ctk.CTkFrame(parent)
        action_frame.pack(fill="x", padx=10, pady=10)
        
        export_button = ctk.CTkButton(
            action_frame,
            text="Exportar Grafico",
            command=self.export_chart,
            width=120,
            height=35
        )
        export_button.pack(side="left", padx=5)
        
        refresh_button = ctk.CTkButton(
            action_frame,
            text="Atualizar",
            command=self.refresh_data,
            width=120,
            height=35
        )
        refresh_button.pack(side="right", padx=5)
    
    def create_visualization_panel(self, parent):
        """Cria o painel de visualizacao"""
        
        # Titulo do painel
        viz_title = ctk.CTkLabel(
            parent,
            text="Visualizacao de Graficos",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors['primary']
        )
        viz_title.pack(pady=(20, 10))
        
        # Frame para o grafico
        self.chart_frame = ctk.CTkFrame(parent)
        self.chart_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Inicializa o grafico vazio
        self.create_empty_chart()
    
    def create_empty_chart(self):
        """Cria um grafico vazio inicial"""
        self.fig = Figure(figsize=(10, 6), facecolor='white')
        self.ax = self.fig.add_subplot(111)
        self.ax.text(0.5, 0.5, 'Selecione um grafico para visualizar', 
                    ha='center', va='center', fontsize=16, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')
        
        self.canvas = FigureCanvasTkAgg(self.fig, self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def create_footer(self):
        """Cria o rodape da aplicacao"""
        footer_frame = ctk.CTkFrame(self.main_frame, height=50)
        footer_frame.pack(fill="x", padx=10, pady=(5, 10))
        footer_frame.pack_propagate(False)
        
        # Status
        self.status_label = ctk.CTkLabel(
            footer_frame,
            text="Pronto para usar",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(side="left", padx=20, pady=15)
        
        # Versao
        version_label = ctk.CTkLabel(
            footer_frame,
            text="v2.0 - Professional Edition",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['text']
        )
        version_label.pack(side="right", padx=20, pady=15)
    
    def load_data(self):
        """Carrega os dados do arquivo CSV"""
        try:
            if os.path.exists(self.csv_file):
                self.data = pd.read_csv(self.csv_file)
                self.data['data'] = pd.to_datetime(self.data['data'])
                self.update_info()
                self.status_label.configure(text=f"Dados carregados: {len(self.data)} medições")
                
                # Atualiza as tabelas se existirem
                if hasattr(self, 'data_manager'):
                    self.data_manager.refresh_data_table()
                
                return True
            else:
                self.status_label.configure(text="Arquivo de dados não encontrado")
                return False
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
            return False
    
    def load_data_dialog(self):
        """Abre dialogo para carregar arquivo de dados"""
        file_path = filedialog.askopenfilename(
            title="Selecionar arquivo de dados",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            self.csv_file = file_path
            if self.load_data():
                self.generate_chart()
    
    def update_info(self):
        """Atualiza as informacoes dos dados"""
        if self.data is not None:
            info_text = f"""Total de medições: {len(self.data)}
Periodo: {self.data['data'].min().strftime('%d/%m/%Y')} - {self.data['data'].max().strftime('%d/%m/%Y')}

Peso atual: {self.data['peso'].iloc[-1]:.1f} kg
IMC atual: {self.data['imc'].iloc[-1]:.1f}

Mudanca no peso: {self.data['peso'].iloc[-1] - self.data['peso'].iloc[0]:+.1f} kg
Mudanca no IMC: {self.data['imc'].iloc[-1] - self.data['imc'].iloc[0]:+.1f}"""
            
            self.info_text.delete("1.0", "end")
            self.info_text.insert("1.0", info_text)
    
    def on_chart_change(self, choice):
        """Callback para mudanca no seletor de grafico"""
        self.current_chart = choice.lower().replace(" ", "_")
        self.generate_chart()
    
    def generate_chart(self):
        """Gera o grafico selecionado"""
        if self.data is None:
            messagebox.showwarning("Aviso", "Nenhum dado carregado!")
            return
        
        # Limpa o grafico anterior
        self.fig.clear()
        
        chart_type = self.current_chart
        
        if chart_type == "evolucao_do_peso":
            self.create_weight_chart()
        elif chart_type == "composição_corporal":
            self.create_composition_chart()
        elif chart_type == "analise_de_imc":
            self.create_imc_chart()
        elif chart_type == "metabolismo":
            self.create_metabolism_chart()
        elif chart_type == "dashboard_completo":
            self.create_dashboard_chart()
        
        # Atualiza o canvas
        self.canvas.draw()
        self.status_label.configure(text=f"Grafico '{self.chart_var.get()}' gerado com sucesso")
    
    def create_weight_chart(self):
        """Cria grafico de evolucao do peso"""
        ax = self.fig.add_subplot(111)
        
        ax.plot(self.data['data'], self.data['peso'], 
               marker='o', linewidth=3, markersize=8, color='#2E86AB')
        
        ax.set_title('Evolucao do Peso Corporal', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Data', fontsize=12)
        ax.set_ylabel('Peso (kg)', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Rotaciona as datas
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        # Adiciona estatisticas
        min_weight = self.data['peso'].min()
        max_weight = self.data['peso'].max()
        current_weight = self.data['peso'].iloc[-1]
        first_weight = self.data['peso'].iloc[0]
        change = current_weight - first_weight
        
        stats_text = f'Peso inicial: {first_weight:.1f} kg\n'
        stats_text += f'Peso atual: {current_weight:.1f} kg\n'
        stats_text += f'Mudanca: {change:+.1f} kg'
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        self.fig.tight_layout()
    
    def create_composition_chart(self):
        """Cria grafico de composição corporal"""
        # Encontra as colunas de gordura e massa muscular
        fat_col = None
        muscle_col = None
        
        for col in self.data.columns:
            if 'Gordura' in col and ('%' in col or 'porcento' in col):
                fat_col = col
            if 'Massa' in col and ('%' in col or 'porcento' in col):
                muscle_col = col
        
        if not fat_col or not muscle_col:
            ax = self.fig.add_subplot(111)
            ax.text(0.5, 0.5, 'Colunas de composição corporal não encontradas', 
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return
        
        # Cria subplots
        ax1 = self.fig.add_subplot(211)
        ax2 = self.fig.add_subplot(212)
        
        # Grafico de gordura
        ax1.plot(self.data['data'], self.data[fat_col], 
                marker='o', linewidth=3, markersize=6, color='#ff6b6b', label='Gordura %')
        ax1.set_title('Percentual de Gordura Corporal', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Gordura (%)', fontsize=12)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Grafico de massa muscular
        ax2.plot(self.data['data'], self.data[muscle_col], 
                marker='o', linewidth=3, markersize=6, color='#4ecdc4', label='Massa Muscular %')
        ax2.set_title('Percentual de Massa Muscular', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Data', fontsize=12)
        ax2.set_ylabel('Massa Muscular (%)', fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # Rotaciona as datas
        for ax in [ax1, ax2]:
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        self.fig.suptitle('Composicao Corporal', fontsize=16, fontweight='bold')
        self.fig.tight_layout()
    
    def create_imc_chart(self):
        """Cria grafico de analise de IMC"""
        ax = self.fig.add_subplot(111)
        
        ax.plot(self.data['data'], self.data['imc'], 
               marker='o', linewidth=3, markersize=8, color='#ffa726')
        
        # Adiciona linhas de referencia do IMC
        ax.axhline(y=18.5, color='green', linestyle='--', alpha=0.7, label='Abaixo do peso')
        ax.axhline(y=25, color='orange', linestyle='--', alpha=0.7, label='Peso normal')
        ax.axhline(y=30, color='red', linestyle='--', alpha=0.7, label='Sobrepeso')
        
        ax.set_title('Analise do Indice de Massa Corporal (IMC)', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Data', fontsize=12)
        ax.set_ylabel('IMC', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Rotaciona as datas
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        self.fig.tight_layout()
    
    def create_metabolism_chart(self):
        """Cria grafico de analise de metabolismo"""
        if 'Metabolismo' not in self.data.columns:
            ax = self.fig.add_subplot(111)
            ax.text(0.5, 0.5, 'Coluna de metabolismo não encontrada', 
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return
        
        ax = self.fig.add_subplot(111)
        
        ax.plot(self.data['data'], self.data['Metabolismo'], 
               marker='o', linewidth=3, markersize=8, color='#ff9800')
        
        ax.set_title('Evolucao do Metabolismo Basal', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Data', fontsize=12)
        ax.set_ylabel('Metabolismo (kcal/dia)', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Rotaciona as datas
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        self.fig.tight_layout()
    
    def create_dashboard_chart(self):
        """Cria dashboard completo"""
        # Encontra as colunas necessarias
        fat_col = None
        muscle_col = None
        
        for col in self.data.columns:
            if 'Gordura' in col and ('%' in col or 'porcento' in col):
                fat_col = col
            if 'Massa' in col and ('%' in col or 'porcento' in col):
                muscle_col = col
        
        # Cria subplots 2x2
        ax1 = self.fig.add_subplot(221)
        ax2 = self.fig.add_subplot(222)
        ax3 = self.fig.add_subplot(223)
        ax4 = self.fig.add_subplot(224)
        
        # Peso
        ax1.plot(self.data['data'], self.data['peso'], marker='o', linewidth=2, markersize=4, color='#2E86AB')
        ax1.set_title('Evolucao do Peso', fontweight='bold')
        ax1.set_ylabel('Peso (kg)')
        ax1.grid(True, alpha=0.3)
        
        # IMC
        ax2.plot(self.data['data'], self.data['imc'], marker='o', linewidth=2, markersize=4, color='#ffa726')
        ax2.set_title('IMC', fontweight='bold')
        ax2.set_ylabel('IMC')
        ax2.grid(True, alpha=0.3)
        
        # Composicao corporal
        if fat_col and muscle_col:
            ax3.plot(self.data['data'], self.data[fat_col], marker='o', linewidth=2, markersize=4, color='#ff6b6b', label='Gordura %')
            ax3.plot(self.data['data'], self.data[muscle_col], marker='o', linewidth=2, markersize=4, color='#4ecdc4', label='Massa Muscular %')
            ax3.set_title('Composicao Corporal', fontweight='bold')
            ax3.set_ylabel('Percentual (%)')
            ax3.legend()
            ax3.grid(True, alpha=0.3)
        
        # Metabolismo
        if 'Metabolismo' in self.data.columns:
            ax4.plot(self.data['data'], self.data['Metabolismo'], marker='o', linewidth=2, markersize=4, color='#ff9800')
            ax4.set_title('Metabolismo', fontweight='bold')
            ax4.set_ylabel('kcal/dia')
            ax4.grid(True, alpha=0.3)
        
        # Rotaciona as datas em todos os subplots
        for ax in [ax1, ax2, ax3, ax4]:
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        self.fig.suptitle('Dashboard Completo de Composicao Corporal', fontsize=16, fontweight='bold')
        self.fig.tight_layout()
    
    def export_chart(self):
        """Exporta o grafico atual"""
        if hasattr(self, 'fig'):
            file_path = filedialog.asksaveasfilename(
                title="Salvar grafico",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            if file_path:
                self.fig.savefig(file_path, dpi=300, bbox_inches='tight')
                messagebox.showinfo("Sucesso", f"Grafico salvo em: {file_path}")
    
    def refresh_data(self):
        """Atualiza os dados e regenera o grafico"""
        if self.load_data():
            self.generate_chart()
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
    
    def run(self):
        """Executa a aplicacao"""
        self.root.mainloop()

def main():
    """Funcao principal"""
    app = ModernBioimpedanceGUI()
    app.run()

if __name__ == "__main__":
    main()