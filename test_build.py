#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se o build do executável funciona
"""

import os
import sys
import subprocess
from pathlib import Path

def test_imports():
    """Testa se todas as importações necessárias funcionam"""
    print("🔍 Testando importações...")
    
    try:
        import customtkinter as ctk
        print("✅ customtkinter")
    except ImportError as e:
        print(f"❌ customtkinter: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ matplotlib")
    except ImportError as e:
        print(f"❌ matplotlib: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ pandas")
    except ImportError as e:
        print(f"❌ pandas: {e}")
        return False
    
    try:
        import seaborn as sns
        print("✅ seaborn")
    except ImportError as e:
        print(f"❌ seaborn: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy")
    except ImportError as e:
        print(f"❌ numpy: {e}")
        return False
    
    return True

def test_main_import():
    """Testa se o main.py pode ser importado"""
    print("\n🔍 Testando importação do main...")
    
    try:
        # Adiciona o diretório atual ao path
        sys.path.insert(0, str(Path(__file__).parent))
        
        # Tenta importar o main
        import main
        print("✅ main.py importado com sucesso")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar main.py: {e}")
        return False

def test_gui_import():
    """Testa se a interface gráfica pode ser importada"""
    print("\n🔍 Testando importação da interface...")
    
    try:
        # Adiciona o diretório src ao path
        sys.path.insert(0, str(Path(__file__).parent / "src"))
        
        # Tenta importar a interface
        from ui.modern_gui import ModernBioimpedanceGUI
        print("✅ Interface gráfica importada com sucesso")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar interface: {e}")
        return False

def test_pyinstaller():
    """Testa se o PyInstaller está disponível"""
    print("\n🔍 Testando PyInstaller...")
    
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__}")
        return True
    except ImportError:
        print("❌ PyInstaller não encontrado")
        print("💡 Instale com: pip install pyinstaller")
        return False

def main():
    """Função principal de teste"""
    print("🧪 Teste de Build - Analisador de Bioimpedância")
    print("=" * 50)
    
    # Verifica se estamos no diretório correto
    if not os.path.exists("main.py"):
        print("❌ Execute este script no diretório raiz do projeto")
        sys.exit(1)
    
    # Executa testes
    tests = [
        test_imports,
        test_main_import,
        test_gui_import,
        test_pyinstaller
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    # Resultado final
    print("📊 Resultado dos Testes:")
    print(f"✅ Passou: {passed}/{total}")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O build deve funcionar.")
        print("\n📋 Próximos passos:")
        print("1. Execute: python3 build_executable.py")
        print("2. Ou execute: ./install.sh")
    else:
        print("❌ Alguns testes falharam. Corrija os problemas antes do build.")
        sys.exit(1)

if __name__ == "__main__":
    main()
