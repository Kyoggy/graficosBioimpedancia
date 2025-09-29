#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration file for Bioimpedance Analyzer
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
EXPORTS_DIR = DATA_DIR / "exports"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Default files
DEFAULT_CSV_FILE = RAW_DATA_DIR / "dados_bioimpedancia.csv"

# Chart settings
CHART_DPI = 300
CHART_STYLE = 'seaborn-v0_8'
CHART_PALETTE = "husl"

# GUI settings
GUI_TITLE = "Analisador de Bioimpedância - Professional Edition"
GUI_SIZE = "800x900"

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, EXPORTS_DIR, PROCESSED_DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
