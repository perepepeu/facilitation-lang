#!/usr/bin/env python3
"""
Facilitation Language - Arquivo principal
"""

import sys
import os

# Adicionar src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from facilitation import interpretar

def main():
    """Função principal"""
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
        if not os.path.exists(arquivo):
            print(f"❌ Arquivo '{arquivo}' não encontrado.")
            sys.exit(1)
        
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            
            print(f"🚀 Executando {arquivo}...")
            interpretar(codigo)
            
        except Exception as e:
            print(f"❌ Erro: {e}")
            sys.exit(1)
    else:
        # Executar exemplo padrão
        exemplo_path = os.path.join('examples', 'exemplo.f')
        if os.path.exists(exemplo_path):
            try:
                with open(exemplo_path, 'r', encoding='utf-8') as f:
                    codigo = f.read()
                
                print("🚀 Executando exemplo.f...")
                interpretar(codigo)
                
            except Exception as e:
                print(f"❌ Erro: {e}")
                sys.exit(1)
        else:
            print("❌ Nenhum arquivo especificado e exemplo.f não encontrado.")
            print("Use: python main.py <arquivo.f>")
            sys.exit(1)

if __name__ == "__main__":
    main() 