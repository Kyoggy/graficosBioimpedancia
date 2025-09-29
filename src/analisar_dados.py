#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de conveniencia para analisar dados de bioimpedancia
"""

import sys
import os

# Adiciona o diretorio core ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from bioimpedance_analyzer import BioimpedanceAnalyzer

def main():
    print("?? Analisador de Dados de Bioimpedancia")
    print("=" * 50)
    
    # Procura por arquivos CSV na pasta data/raw
    import glob
    csv_files = glob.glob('../data/raw/*.csv')
    
    if not csv_files:
        print("? Nenhum arquivo CSV encontrado na pasta 'data/'")
        print("?? Coloque um arquivo .csv na pasta 'data/' e execute novamente")
        return
    
    if len(csv_files) == 1:
        data_file = csv_files[0]
        print(f"?? Usando arquivo: {data_file}")
    else:
        print("?? Múltiplos arquivos encontrados:")
        for i, file in enumerate(csv_files, 1):
            print(f"  {i}. {file}")
        
        try:
            choice = int(input("Escolha o número do arquivo: ")) - 1
            data_file = csv_files[choice]
        except (ValueError, IndexError):
            print("? Escolha inválida.")
            return
    
    # Verifica se o arquivo existe
    if not os.path.exists(data_file):
        print(f"? Arquivo não encontrado: {data_file}")
        return
    
    # Cria o analisador e gera o relatório
    analyzer = BioimpedanceAnalyzer(data_file)
    analyzer.generate_report()

if __name__ == "__main__":
    main()
