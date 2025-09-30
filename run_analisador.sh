#!/bin/bash
# Launcher para o Analisador de Bioimpedância

# Verifica se o executável existe
if [ ! -f "./AnalisadorBioimpedancia" ]; then
    echo "❌ Executável não encontrado!"
    echo "Execute primeiro: python3 build_executable.py"
    exit 1
fi

# Torna o executável executável
chmod +x ./AnalisadorBioimpedancia

# Executa o programa
echo "🚀 Iniciando Analisador de Bioimpedância..."
./AnalisadorBioimpedancia
