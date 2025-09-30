#!/bin/bash
# Script de demonstração do executável do Analisador de Bioimpedância

echo "🏥 Demonstração do Analisador de Bioimpedância - Versão Executável"
echo "=================================================================="
echo

# Verifica se o executável existe
if [ ! -f "./AnalisadorBioimpedancia" ]; then
    echo "❌ Executável não encontrado!"
    echo "Execute primeiro: python3 build_executable.py"
    exit 1
fi

echo "✅ Executável encontrado: $(ls -lh AnalisadorBioimpedancia | awk '{print $5}')"
echo

# Mostra informações do sistema
echo "📊 Informações do Sistema:"
echo "  • Sistema Operacional: $(uname -s) $(uname -r)"
echo "  • Arquitetura: $(uname -m)"
echo "  • Python (sistema): $(python3 --version 2>/dev/null || echo 'Não instalado')"
echo

# Mostra opções de execução
echo "🚀 Opções de Execução:"
echo "  1. Executar diretamente: ./AnalisadorBioimpedancia"
echo "  2. Usar script launcher: ./run_analisador.sh"
echo "  3. Instalar no sistema: ./install.sh"
echo

# Pergunta se quer executar
read -p "Deseja executar o programa agora? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Iniciando Analisador de Bioimpedância..."
    echo "   (Pressione Ctrl+C para sair)"
    echo
    ./AnalisadorBioimpedancia
else
    echo "💡 Para executar depois, use: ./AnalisadorBioimpedancia"
fi
