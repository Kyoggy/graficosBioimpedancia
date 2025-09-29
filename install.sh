#!/bin/bash
# Bioimpedance Analyzer - Installation Script

echo "?? Bioimpedance Analyzer - Professional Edition"
echo "=============================================="
echo "Installing dependencies..."

# Check if running on Ubuntu/Debian
if command -v apt &> /dev/null; then
    echo "?? Installing system dependencies..."
    sudo apt update
    sudo apt install -y python3-pandas python3-matplotlib python3-seaborn python3-openpyxl python3-tk python3-pip
    
    echo "?? Installing Python dependencies..."
    pip3 install -r requirements.txt
    
    echo "?? Installing CustomTkinter for modern interface..."
    pip3 install customtkinter
    
elif command -v yum &> /dev/null; then
    echo "?? Installing system dependencies (RHEL/CentOS)..."
    sudo yum install -y python3-pandas python3-matplotlib python3-seaborn python3-openpyxl tkinter python3-pip
    
    echo "?? Installing Python dependencies..."
    pip3 install -r requirements.txt
    
    echo "?? Installing CustomTkinter for modern interface..."
    pip3 install customtkinter
    
else
    echo "??  Unsupported system. Please install dependencies manually:"
    echo "   - python3-pandas"
    echo "   - python3-matplotlib" 
    echo "   - python3-seaborn"
    echo "   - python3-openpyxl"
    echo "   - python3-tk"
fi

# Make scripts executable
chmod +x main.py
chmod +x src/analisar_dados.py
chmod +x src/ui/interface_grafica.py

echo "? Installation completed!"
echo ""
echo "?? To run the application:"
echo "   python3 main.py"
echo ""
echo "?? Project structure:"
echo "   src/core/     - Core analysis modules"
echo "   src/ui/       - User interface modules"
echo "   data/raw/     - Raw CSV data files"
echo "   data/exports/ - Generated charts and reports"
echo "   docs/         - Documentation"
