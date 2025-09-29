#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para abrir a interface gráfica do analisador de bioimpedância
"""

import sys
import os

# Adiciona o diretorio atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from interface_gráfica import main
    main()
except ImportError as e:
    print(f"Erro ao importar a interface gráfica: {e}")
    print("Certifique-se de que o tkinter esta instalado:")
    print("sudo apt install python3-tk")
    sys.exit(1)
except Exception as e:
    print(f"Erro ao executar a interface: {e}")
    sys.exit(1)
