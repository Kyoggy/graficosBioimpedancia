#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioimpedance Analyzer - Main Entry Point

Professional body composition analysis tool for bioimpedance data.
"""

import sys
import os
from pathlib import Path

# Add src to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

def main():
    """Main entry point for the application."""
    print("🏥 Bioimpedance Analyzer - Professional Edition")
    print("=" * 50)
    print("Choose an option:")
    print("1. Open Modern Desktop Interface (CustomTkinter)")
    print("2. Open Classic GUI Interface (Tkinter)")
    print("3. Analyze data from command line")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                print("🚀 Opening Modern Desktop Interface...")
                from ui.modern_gui import main as modern_gui_main
                modern_gui_main()
                break
            elif choice == "2":
                from ui.interface_gráfica import main as gui_main
                gui_main()
                break
            elif choice == "3":
                from analisar_dados import main as cli_main
                cli_main()
                break
            elif choice == "4":
                print("Goodbye! 👋")
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
