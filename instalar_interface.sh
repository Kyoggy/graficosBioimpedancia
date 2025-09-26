#!/bin/bash

echo "??? Instalando dependências para interface gráfica..."
echo "=================================================="

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "? Python3 não encontrado. Por favor, instale o Python3 primeiro."
    exit 1
fi

echo "? Python3 encontrado"

# Instala tkinter se necessário
echo "?? Verificando tkinter..."
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "?? Instalando tkinter..."
    sudo apt update
    sudo apt install -y python3-tk
    if [ $? -eq 0 ]; then
        echo "? tkinter instalado com sucesso!"
    else
        echo "? Erro ao instalar tkinter"
        exit 1
    fi
else
    echo "? tkinter já está instalado"
fi

# Verifica se as outras dependências estão instaladas
echo "?? Verificando outras dependências..."
python3 -c "import pandas, matplotlib, seaborn" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "?? Instalando dependências de análise..."
    sudo apt install -y python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
    if [ $? -eq 0 ]; then
        echo "? Dependências instaladas com sucesso!"
    else
        echo "? Erro ao instalar dependências"
        exit 1
    fi
else
    echo "? Dependências de análise já estão instaladas"
fi

echo ""
echo "?? Instalação concluída!"
echo ""
echo "Para usar a interface gráfica:"
echo "  python3 abrir_interface.py"
echo ""
echo "Para usar o analisador de linha de comando:"
echo "  python3 analisar_dados.py"
echo ""
