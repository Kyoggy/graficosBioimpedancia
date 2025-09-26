#!/bin/bash

echo "??? Instalando depend�ncias para interface gr�fica..."
echo "=================================================="

# Verifica se o Python est� instalado
if ! command -v python3 &> /dev/null; then
    echo "? Python3 n�o encontrado. Por favor, instale o Python3 primeiro."
    exit 1
fi

echo "? Python3 encontrado"

# Instala tkinter se necess�rio
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
    echo "? tkinter j� est� instalado"
fi

# Verifica se as outras depend�ncias est�o instaladas
echo "?? Verificando outras depend�ncias..."
python3 -c "import pandas, matplotlib, seaborn" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "?? Instalando depend�ncias de an�lise..."
    sudo apt install -y python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
    if [ $? -eq 0 ]; then
        echo "? Depend�ncias instaladas com sucesso!"
    else
        echo "? Erro ao instalar depend�ncias"
        exit 1
    fi
else
    echo "? Depend�ncias de an�lise j� est�o instaladas"
fi

echo ""
echo "?? Instala��o conclu�da!"
echo ""
echo "Para usar a interface gr�fica:"
echo "  python3 abrir_interface.py"
echo ""
echo "Para usar o analisador de linha de comando:"
echo "  python3 analisar_dados.py"
echo ""
