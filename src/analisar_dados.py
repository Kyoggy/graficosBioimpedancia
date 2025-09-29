#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de conveniencia para analisar dados de bioimpedância
"""

import sys
import os

# Adiciona o diretorio core ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from bioimpedance_analyzer import BioimpedanceAnalyzer

def main():
    print("🏥 Analisador de Dados de Bioimpedancia")
    print("=" * 50)
    
    # Procura por arquivos CSV na pasta data/raw
    import glob
    # Caminho para o arquivo de dados (relativo ao diretório do projeto)
    csv_files = ["data/raw/dados_bioimpedancia.csv"]
    
    # Usa sempre o arquivo fixo
    data_file = csv_files[0]
    print(f"📊 Usando arquivo: {data_file}")
    
    # Verifica se o arquivo existe
    if not os.path.exists(data_file):
        print(f"❌ Arquivo não encontrado: {data_file}")
        return
    
    # Cria o analisador e gera o relatório
    analyzer = BioimpedanceAnalyzer(data_file)
    analyzer.generate_report()

if __name__ == "__main__":
    main()