#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para construir o executável do Analisador de Bioimpedância
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """Verifica se o PyInstaller está instalado"""
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado")
        return True
    except ImportError:
        print("❌ PyInstaller não encontrado. Instalando...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller>=5.13.0"])
            print("✅ PyInstaller instalado com sucesso")
            return True
        except subprocess.CalledProcessError:
            print("❌ Erro ao instalar PyInstaller")
            return False

def clean_build_dirs():
    """Limpa diretórios de build anteriores"""
    dirs_to_clean = ["build", "dist", "__pycache__"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"🧹 Limpando diretório {dir_name}...")
            shutil.rmtree(dir_name)
    
    # Limpa arquivos .spec antigos
    for spec_file in Path(".").glob("*.spec"):
        print(f"🧹 Removendo {spec_file}...")
        spec_file.unlink()

def build_executable():
    """Constrói o executável"""
    print("🔨 Iniciando construção do executável...")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",  # Arquivo único
        "--windowed",  # Sem console (GUI)
        "--name=AnalisadorBioimpedancia",  # Nome do executável
        "--icon=assets/icon.ico" if os.path.exists("assets/icon.ico") else "",  # Ícone (opcional)
        "--add-data=data:data",  # Inclui pasta de dados
        "--hidden-import=customtkinter",
        "--hidden-import=matplotlib.backends.backend_tkagg",
        "--hidden-import=PIL",
        "--hidden-import=PIL._tkinter_finder",
        "--hidden-import=seaborn",
        "--hidden-import=pandas",
        "--hidden-import=numpy",
        "--hidden-import=openpyxl",
        "main.py"
    ]
    
    # Remove argumentos vazios
    cmd = [arg for arg in cmd if arg]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executável construído com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao construir executável: {e}")
        return False

def create_launcher_script():
    """Cria um script launcher para facilitar o uso"""
    launcher_content = '''#!/bin/bash
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
'''
    
    with open("run_analisador.sh", "w") as f:
        f.write(launcher_content)
    
    # Torna o script executável
    os.chmod("run_analisador.sh", 0o755)
    print("✅ Script launcher criado: run_analisador.sh")

def create_desktop_file():
    """Cria um arquivo .desktop para integração com o sistema"""
    desktop_content = f'''[Desktop Entry]
Version=1.0
Type=Application
Name=Analisador de Bioimpedância
Comment=Análise profissional de composição corporal
Exec={os.path.abspath('.')}/AnalisadorBioimpedancia
Icon={os.path.abspath('.')}/assets/icon.png
Terminal=false
Categories=Science;MedicalSoftware;
'''
    
    os.makedirs("assets", exist_ok=True)
    with open("AnalisadorBioimpedancia.desktop", "w") as f:
        f.write(desktop_content)
    
    print("✅ Arquivo .desktop criado: AnalisadorBioimpedancia.desktop")

def main():
    """Função principal"""
    print("🏥 Construtor de Executável - Analisador de Bioimpedância")
    print("=" * 60)
    
    # Verifica se estamos no diretório correto
    if not os.path.exists("main.py"):
        print("❌ Execute este script no diretório raiz do projeto")
        sys.exit(1)
    
    # Verifica PyInstaller
    if not check_pyinstaller():
        sys.exit(1)
    
    # Limpa builds anteriores
    clean_build_dirs()
    
    # Constrói o executável
    if build_executable():
        print("\n🎉 Executável criado com sucesso!")
        print("📁 Localização: ./dist/AnalisadorBioimpedancia")
        
        # Move o executável para o diretório atual
        if os.path.exists("dist/AnalisadorBioimpedancia"):
            shutil.copy("dist/AnalisadorBioimpedancia", ".")
            print("📁 Executável copiado para o diretório atual")
        
        # Cria scripts auxiliares
        create_launcher_script()
        create_desktop_file()
        
        print("\n📋 Instruções de uso:")
        print("1. Execute: ./run_analisador.sh")
        print("2. Ou execute diretamente: ./AnalisadorBioimpedancia")
        print("3. Para instalar no sistema: sudo cp AnalisadorBioimpedancia.desktop /usr/share/applications/")
        
    else:
        print("❌ Falha na construção do executável")
        sys.exit(1)

if __name__ == "__main__":
    main()
