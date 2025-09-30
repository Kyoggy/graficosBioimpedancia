#!/bin/bash
# Script de instalação para o Analisador de Bioimpedância
# Versão: 1.0

set -e  # Para em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_message() {
    echo -e "${2}${1}${NC}"
}

print_header() {
    echo
    print_message "🏥 Analisador de Bioimpedância - Instalador" "$BLUE"
    print_message "=============================================" "$BLUE"
    echo
}

print_success() {
    print_message "✅ $1" "$GREEN"
}

print_warning() {
    print_message "⚠️  $1" "$YELLOW"
}

print_error() {
    print_message "❌ $1" "$RED"
}

# Verifica se é root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        print_warning "Executando como root. Isso não é necessário para a instalação."
        read -p "Deseja continuar? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
}

# Verifica dependências do sistema
check_dependencies() {
    print_message "🔍 Verificando dependências do sistema..." "$BLUE"
    
    # Verifica Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 não encontrado. Instale com: sudo apt install python3"
        exit 1
    fi
    print_success "Python 3 encontrado: $(python3 --version)"
    
    # Verifica pip
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 não encontrado. Instale com: sudo apt install python3-pip"
        exit 1
    fi
    print_success "pip3 encontrado"
    
    # Verifica dependências do sistema (opcional)
    print_message "📦 Verificando dependências opcionais do sistema..." "$BLUE"
    
    missing_deps=()
    
    if ! dpkg -l | grep -q python3-tk; then
        missing_deps+=("python3-tk")
    fi
    
    if ! dpkg -l | grep -q python3-pil; then
        missing_deps+=("python3-pil")
    fi
    
    if [ ${#missing_deps[@]} -gt 0 ]; then
        print_warning "Algumas dependências opcionais não foram encontradas:"
        for dep in "${missing_deps[@]}"; do
            echo "  - $dep"
        done
        echo
        read -p "Deseja instalá-las automaticamente? (Y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
            print_message "📦 Instalando dependências do sistema..." "$BLUE"
            sudo apt update
            sudo apt install -y "${missing_deps[@]}"
            print_success "Dependências do sistema instaladas"
        fi
    else
        print_success "Todas as dependências do sistema estão instaladas"
    fi
}

# Instala dependências Python
install_python_deps() {
    print_message "🐍 Instalando dependências Python..." "$BLUE"
    
    # Cria ambiente virtual se não existir
    if [ ! -d "venv" ]; then
        print_message "📁 Criando ambiente virtual..." "$BLUE"
        python3 -m venv venv
        print_success "Ambiente virtual criado"
    fi
    
    # Ativa ambiente virtual
    source venv/bin/activate
    print_success "Ambiente virtual ativado"
    
    # Atualiza pip
    pip install --upgrade pip
    print_success "pip atualizado"
    
    # Instala dependências
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        print_success "Dependências Python instaladas"
    else
        print_error "Arquivo requirements.txt não encontrado"
        exit 1
    fi
}

# Cria executável
build_executable() {
    print_message "🔨 Construindo executável..." "$BLUE"
    
    # Ativa ambiente virtual
    source venv/bin/activate
    
    # Executa script de build
    if [ -f "build_executable.py" ]; then
        python3 build_executable.py
        print_success "Executável construído"
    else
        print_error "Script build_executable.py não encontrado"
        exit 1
    fi
}

# Instala no sistema
install_system() {
    print_message "📋 Instalando no sistema..." "$BLUE"
    
    # Cria diretório de instalação
    INSTALL_DIR="$HOME/.local/bin"
    mkdir -p "$INSTALL_DIR"
    
    # Copia executável
    if [ -f "AnalisadorBioimpedancia" ]; then
        cp "AnalisadorBioimpedancia" "$INSTALL_DIR/"
        chmod +x "$INSTALL_DIR/AnalisadorBioimpedancia"
        print_success "Executável instalado em $INSTALL_DIR"
    else
        print_error "Executável não encontrado"
        exit 1
    fi
    
    # Adiciona ao PATH se necessário
    if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
        print_success "Adicionado ao PATH no .bashrc"
        print_warning "Reinicie o terminal ou execute: source ~/.bashrc"
    fi
    
    # Instala arquivo .desktop
    if [ -f "AnalisadorBioimpedancia.desktop" ]; then
        mkdir -p "$HOME/.local/share/applications"
        cp "AnalisadorBioimpedancia.desktop" "$HOME/.local/share/applications/"
        print_success "Arquivo .desktop instalado"
    fi
}

# Cria script de desinstalação
create_uninstaller() {
    print_message "📝 Criando script de desinstalação..." "$BLUE"
    
    cat > uninstall.sh << 'EOF'
#!/bin/bash
# Script de desinstalação do Analisador de Bioimpedância

echo "🗑️  Desinstalando Analisador de Bioimpedância..."

# Remove executável
rm -f "$HOME/.local/bin/AnalisadorBioimpedancia"

# Remove arquivo .desktop
rm -f "$HOME/.local/share/applications/AnalisadorBioimpedancia.desktop"

# Remove do PATH (comentado para não quebrar outros programas)
# sed -i '/export PATH="\$HOME\/.local\/bin:\$PATH"/d' "$HOME/.bashrc"

echo "✅ Desinstalação concluída"
echo "💡 Reinicie o terminal para aplicar as mudanças"
EOF
    
    chmod +x uninstall.sh
    print_success "Script de desinstalação criado: uninstall.sh"
}

# Função principal
main() {
    print_header
    check_root
    
    # Verifica se estamos no diretório correto
    if [ ! -f "main.py" ]; then
        print_error "Execute este script no diretório raiz do projeto"
        exit 1
    fi
    
    # Executa instalação
    check_dependencies
    install_python_deps
    build_executable
    install_system
    create_uninstaller
    
    echo
    print_success "🎉 Instalação concluída com sucesso!"
    echo
    print_message "📋 Como usar:" "$BLUE"
    echo "  • Execute: AnalisadorBioimpedancia"
    echo "  • Ou use o script: ./run_analisador.sh"
    echo
    print_message "📁 Arquivos criados:" "$BLUE"
    echo "  • Executável: $HOME/.local/bin/AnalisadorBioimpedancia"
    echo "  • Script launcher: ./run_analisador.sh"
    echo "  • Script desinstalação: ./uninstall.sh"
    echo
    print_warning "💡 Reinicie o terminal ou execute: source ~/.bashrc"
    echo
}

# Executa função principal
main "$@"