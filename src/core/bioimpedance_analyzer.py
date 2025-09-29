#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador de Bioimpedanciometria - Script para analisar dados corporais
Especializado para dados de balanca de bioimpedância
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
import sys
import numpy as np

# Configuracao do estilo dos graficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class BioimpedanceAnalyzer:
    def __init__(self, data_file):
        """
        Inicializa o analisador com o arquivo de dados de bioimpedância
        
        Args:
            data_file (str): Caminho para o arquivo de dados (CSV)
        """
        self.data_file = data_file
        self.data = None
        
    def load_data(self):
        """Carrega os dados do arquivo CSV"""
        try:
            self.data = pd.read_csv(self.data_file)
            
            print(f"✅ Dados de bioimpedância carregados com sucesso!")
            print(f"📊 Total de medições: {len(self.data)}")
            print(f"📋 Colunas disponíveis: {list(self.data.columns)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")
            return False
    
    def prepare_data(self):
        """Prepara os dados para analise"""
        if self.data is None:
            print("❌ Nenhum dado carregado. Execute load_data() primeiro.")
            return False
        
        # Converte a coluna de data para datetime
        if 'data' in self.data.columns:
            self.data['data'] = pd.to_datetime(self.data['data'])
            print(f"📅 Coluna de data convertida: {self.data['data'].dtype}")
        
        # Converte colunas numericas
        numeric_columns = ['peso', 'imc', 'Gordura/porcento', 'Gordura/%', 'Gordura/KG', 
                          'Massa Musucular/porcento', 'Massa Musucular/%', 'Massa Muscular/KG', 
                          'Metabolismo', 'Obesidade/porcento', 'Obesidade/%']
        
        for col in numeric_columns:
            if col in self.data.columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
                print(f"🔢 Coluna numerica convertida: {col}")
        
        return True
    
    def create_weight_evolution(self):
        """Cria grafico de evolucao do peso"""
        if self.data is None or 'peso' not in self.data.columns:
            print("❌ Dados de peso não encontrados.")
            return
        
        clean_data = self.data.dropna(subset=['data', 'peso'])
        
        if len(clean_data) == 0:
            print("❌ Nenhum dado valido encontrado.")
            return
        
        plt.figure(figsize=(14, 8))
        plt.plot(clean_data['data'], clean_data['peso'], 
                marker='o', linewidth=3, markersize=8, color='#2E86AB')
        
        plt.title('Evolucao do Peso Corporal', fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Data', fontsize=14)
        plt.ylabel('Peso (kg)', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # Adiciona estatisticas
        min_weight = clean_data['peso'].min()
        max_weight = clean_data['peso'].max()
        current_weight = clean_data['peso'].iloc[-1]
        first_weight = clean_data['peso'].iloc[0]
        change = current_weight - first_weight
        
        stats_text = f'Peso inicial: {first_weight:.1f} kg\n'
        stats_text += f'Peso atual: {current_weight:.1f} kg\n'
        stats_text += f'Mudanca: {change:+.1f} kg\n'
        stats_text += f'Peso minimo: {min_weight:.1f} kg\n'
        stats_text += f'Peso maximo: {max_weight:.1f} kg'
        
        plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
                verticalalignment='top', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig('../data/exports/evolucao_peso.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("📈 Grafico de evolucao do peso salvo como 'data/evolucao_peso.png'")
    
    def create_body_composition(self):
        """Cria grafico de composicao corporal"""
        if self.data is None:
            print("❌ Nenhum dado carregado.")
            return
        
        # Verifica se as colunas necessarias existem
        gordura_col = None
        massa_col = None
        
        for col in self.data.columns:
            if 'Gordura' in col and ('%' in col or 'porcento' in col):
                gordura_col = col
            elif 'Massa Musucular' in col and ('%' in col or 'porcento' in col):
                massa_col = col
        
        if not gordura_col or not massa_col:
            print("❌ Colunas de composicao corporal não encontradas.")
            return
        
        clean_data = self.data.dropna(subset=['data', gordura_col, massa_col])
        
        if len(clean_data) == 0:
            print("❌ Nenhum dado valido encontrado.")
            return
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
        
        # Grafico de percentual de gordura
        ax1.plot(clean_data['data'], clean_data[gordura_col], 
                marker='o', linewidth=3, markersize=8, color='#E74C3C', label='Gordura (%)')
        ax1.set_title('Evolucao do Percentual de Gordura', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Gordura (%)', fontsize=12)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Grafico de percentual de massa muscular
        ax2.plot(clean_data['data'], clean_data[massa_col], 
                marker='s', linewidth=3, markersize=8, color='#27AE60', label='Massa Muscular (%)')
        ax2.set_title('Evolucao do Percentual de Massa Muscular', fontsize=16, fontweight='bold')
        ax2.set_xlabel('Data', fontsize=12)
        ax2.set_ylabel('Massa Muscular (%)', fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('../data/exports/composicao_corporal.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("💪 Grafico de composicao corporal salvo como 'data/composicao_corporal.png'")
    
    def create_imc_analysis(self):
        """Cria analise do IMC"""
        if self.data is None or 'imc' not in self.data.columns:
            print("❌ Dados de IMC não encontrados.")
            return
        
        clean_data = self.data.dropna(subset=['data', 'imc'])
        
        if len(clean_data) == 0:
            print("❌ Nenhum dado valido encontrado.")
            return
        
        plt.figure(figsize=(14, 8))
        plt.plot(clean_data['data'], clean_data['imc'], 
                marker='o', linewidth=3, markersize=8, color='#8E44AD')
        
        # Adiciona linhas de referencia do IMC
        plt.axhline(y=18.5, color='green', linestyle='--', alpha=0.7, label='Abaixo do peso')
        plt.axhline(y=25, color='yellow', linestyle='--', alpha=0.7, label='Peso normal')
        plt.axhline(y=30, color='orange', linestyle='--', alpha=0.7, label='Sobrepeso')
        plt.axhline(y=35, color='red', linestyle='--', alpha=0.7, label='Obesidade')
        
        plt.title('Evolucao do Indice de Massa Corporal (IMC)', fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Data', fontsize=14)
        plt.ylabel('IMC', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.xticks(rotation=45)
        
        # Adiciona estatisticas
        current_imc = clean_data['imc'].iloc[-1]
        first_imc = clean_data['imc'].iloc[0]
        imc_change = current_imc - first_imc
        
        # Classifica o IMC atual
        if current_imc < 18.5:
            classification = "Abaixo do peso"
        elif current_imc < 25:
            classification = "Peso normal"
        elif current_imc < 30:
            classification = "Sobrepeso"
        else:
            classification = "Obesidade"
        
        stats_text = f'IMC inicial: {first_imc:.1f}\n'
        stats_text += f'IMC atual: {current_imc:.1f}\n'
        stats_text += f'Mudanca: {imc_change:+.1f}\n'
        stats_text += f'Classificacao: {classification}'
        
        plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
                verticalalignment='top', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig('../data/exports/analise_imc.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("📊 Analise de IMC salva como 'data/analise_imc.png'")
    
    def create_metabolism_analysis(self):
        """Cria analise do metabolismo"""
        if self.data is None or 'Metabolismo' not in self.data.columns:
            print("❌ Dados de metabolismo não encontrados.")
            return
        
        clean_data = self.data.dropna(subset=['data', 'Metabolismo'])
        
        if len(clean_data) == 0:
            print("❌ Nenhum dado valido encontrado.")
            return
        
        plt.figure(figsize=(14, 8))
        plt.plot(clean_data['data'], clean_data['Metabolismo'], 
                marker='o', linewidth=3, markersize=8, color='#F39C12')
        
        plt.title('Evolucao do Metabolismo Basal', fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Data', fontsize=14)
        plt.ylabel('Metabolismo (kcal/dia)', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # Adiciona estatisticas
        current_metabolism = clean_data['Metabolismo'].iloc[-1]
        first_metabolism = clean_data['Metabolismo'].iloc[0]
        metabolism_change = current_metabolism - first_metabolism
        
        stats_text = f'Metabolismo inicial: {first_metabolism:.0f} kcal/dia\n'
        stats_text += f'Metabolismo atual: {current_metabolism:.0f} kcal/dia\n'
        stats_text += f'Mudanca: {metabolism_change:+.0f} kcal/dia'
        
        plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
                verticalalignment='top', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='orange', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig('../data/exports/analise_metabolismo.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("❌? Analise de metabolismo salva como 'data/analise_metabolismo.png'")
    
    def create_comprehensive_dashboard(self):
        """Cria dashboard completo com todos os indicadores"""
        if self.data is None:
            print("❌ Nenhum dado carregado.")
            return
        
        clean_data = self.data.dropna(subset=['data'])
        
        if len(clean_data) == 0:
            print("❌ Nenhum dado valido encontrado.")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Peso
        if 'peso' in clean_data.columns:
            ax1.plot(clean_data['data'], clean_data['peso'], 
                    marker='o', linewidth=2, markersize=6, color='#2E86AB')
            ax1.set_title('Peso (kg)', fontweight='bold')
            ax1.grid(True, alpha=0.3)
        
        # IMC
        if 'imc' in clean_data.columns:
            ax2.plot(clean_data['data'], clean_data['imc'], 
                    marker='s', linewidth=2, markersize=6, color='#8E44AD')
            ax2.set_title('IMC', fontweight='bold')
            ax2.grid(True, alpha=0.3)
        
        # Gordura
        gordura_col = None
        for col in clean_data.columns:
            if 'Gordura' in col and ('%' in col or 'porcento' in col):
                gordura_col = col
                break
        
        if gordura_col:
            ax3.plot(clean_data['data'], clean_data[gordura_col], 
                    marker='^', linewidth=2, markersize=6, color='#E74C3C')
            ax3.set_title('Gordura (%)', fontweight='bold')
            ax3.grid(True, alpha=0.3)
        
        # Massa Muscular
        massa_col = None
        for col in clean_data.columns:
            if 'Massa Musucular' in col and ('%' in col or 'porcento' in col):
                massa_col = col
                break
        
        if massa_col:
            ax4.plot(clean_data['data'], clean_data[massa_col], 
                    marker='d', linewidth=2, markersize=6, color='#27AE60')
            ax4.set_title('Massa Muscular (%)', fontweight='bold')
            ax4.grid(True, alpha=0.3)
        
        # Ajusta os eixos x
        for ax in [ax1, ax2, ax3, ax4]:
            ax.tick_params(axis='x', rotation=45)
        
        plt.suptitle('Dashboard de Composicao Corporal', fontsize=20, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig('../data/exports/dashboard_completo.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("❌? Dashboard completo salvo como 'data/dashboard_completo.png'")
    
    def generate_summary_report(self):
        """Gera relatorio resumo dos dados"""
        if self.data is None:
            print("❌ Nenhum dado carregado.")
            return
        
        clean_data = self.data.dropna(subset=['data'])
        
        if len(clean_data) == 0:
            print("❌ Nenhum dado valido encontrado.")
            return
        
        print("\n" + "="*70)
        print("❌? RELATORIO DE COMPOSICAO CORPORAL")
        print("="*70)
        
        # Dados mais recentes
        latest = clean_data.iloc[-1]
        first = clean_data.iloc[0]
        
        print(f"\n?? Periodo: {first['data'].strftime('%d/%m/%Y')} a {latest['data'].strftime('%d/%m/%Y')}")
        print(f"❌? Total de medições: {len(clean_data)}")
        
        print(f"\n?? PESO:")
        if 'peso' in clean_data.columns:
            peso_change = latest['peso'] - first['peso']
            print(f"   ? Inicial: {first['peso']:.1f} kg")
            print(f"   ? Atual: {latest['peso']:.1f} kg")
            print(f"   ? Mudanca: {peso_change:+.1f} kg")
        
        print(f"\n?? IMC:")
        if 'imc' in clean_data.columns:
            imc_change = latest['imc'] - first['imc']
            print(f"   ? Inicial: {first['imc']:.1f}")
            print(f"   ? Atual: {latest['imc']:.1f}")
            print(f"   ? Mudanca: {imc_change:+.1f}")
        
        print(f"\n?? GORDURA:")
        gordura_col = None
        for col in clean_data.columns:
            if 'Gordura' in col and ('%' in col or 'porcento' in col):
                gordura_col = col
                break
        
        if gordura_col:
            gordura_change = latest[gordura_col] - first[gordura_col]
            print(f"   ? Inicial: {first[gordura_col]:.1f}%")
            print(f"   ? Atual: {latest[gordura_col]:.1f}%")
            print(f"   ? Mudanca: {gordura_change:+.1f}%")
        
        print(f"\n?? MASSA MUSCULAR:")
        massa_col = None
        for col in clean_data.columns:
            if 'Massa Musucular' in col and ('%' in col or 'porcento' in col):
                massa_col = col
                break
        
        if massa_col:
            massa_change = latest[massa_col] - first[massa_col]
            print(f"   ? Inicial: {first[massa_col]:.1f}%")
            print(f"   ? Atual: {latest[massa_col]:.1f}%")
            print(f"   ? Mudanca: {massa_change:+.1f}%")
        
        print(f"\n?? METABOLISMO:")
        if 'Metabolismo' in clean_data.columns:
            metab_change = latest['Metabolismo'] - first['Metabolismo']
            print(f"   ? Inicial: {first['Metabolismo']:.0f} kcal/dia")
            print(f"   ? Atual: {latest['Metabolismo']:.0f} kcal/dia")
            print(f"   ? Mudanca: {metab_change:+.0f} kcal/dia")
        
        print("\n" + "="*70)
    
    def generate_report(self):
        """Gera relatorio completo com todos os graficos"""
        print("❌? Iniciando analise de dados de bioimpedância...")
        print("=" * 60)
        
        if not self.load_data():
            return
        
        if not self.prepare_data():
            return
        
        print("\n?? Gerando relatorio resumo...")
        print("-" * 40)
        self.generate_summary_report()
        
        print("\n?? Gerando graficos...")
        print("-" * 40)
        
        self.create_weight_evolution()
        self.create_body_composition()
        self.create_imc_analysis()
        self.create_metabolism_analysis()
        self.create_comprehensive_dashboard()
        
        print("\n? Analise concluida! Todos os graficos foram salvos na pasta 'data/'")
        print("=" * 60)

def main():
    """Funcao principal"""
    print("❌? Analisador de Bioimpedancia - Composicao Corporal")
    print("=" * 60)
    
    # Verifica se o arquivo foi especificado
    if len(sys.argv) > 1:
        data_file = sys.argv[1]
    else:
        # Procura por arquivos CSV na pasta data
        import glob
        csv_files = glob.glob('data/*.csv')
        
        if not csv_files:
            print("❌ Nenhum arquivo CSV encontrado na pasta 'data/'")
            print("❌? Coloque um arquivo .csv na pasta 'data/' e execute novamente")
            return
        
        if len(csv_files) == 1:
            data_file = csv_files[0]
            print(f"❌? Usando arquivo: {data_file}")
        else:
            print("❌? Multiplos arquivos encontrados:")
            for i, file in enumerate(csv_files, 1):
                print(f"  {i}. {file}")
            
            try:
                choice = int(input("Escolha o numero do arquivo: ")) - 1
                data_file = csv_files[choice]
            except (ValueError, IndexError):
                print("❌ Escolha invalida.")
                return
    
    # Verifica se o arquivo existe
    if not os.path.exists(data_file):
        print(f"❌ Arquivo não encontrado: {data_file}")
        return
    
    # Cria o analisador e gera o relatorio
    analyzer = BioimpedanceAnalyzer(data_file)
    analyzer.generate_report()

if __name__ == "__main__":
    main()