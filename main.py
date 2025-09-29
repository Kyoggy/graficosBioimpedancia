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
    print("?? Bioimpedance Analyzer - Professional Edition")
    print("=" * 50)
    print("Choose an option:")
    print("1. Open GUI Interface")
    print("2. Analyze data from command line")
    print("3. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                from ui.interface_grafica import main as gui_main
                gui_main()
                break
            elif choice == "2":
                from analisar_dados import main as cli_main
                cli_main()
                break
            elif choice == "3":
                print("Goodbye! ??")
                break
            else:
                print("? Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nGoodbye! ??")
            break
        except Exception as e:
            print(f"? Error: {e}")

if __name__ == "__main__":
    main()
