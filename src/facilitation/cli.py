#!/usr/bin/env python3
"""
Interface de linha de comando para a Linguagem Facilitation
"""

import sys
import os
import argparse
from pathlib import Path

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from facilitation import interpretar

def main():
    parser = argparse.ArgumentParser(
        description="Linguagem Facilitation - Interpretador",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python -m facilitation.cli exemplo.f
  python -m facilitation.cli --interactive
  python -m facilitation.cli --version
        """
    )
    
    parser.add_argument(
        'arquivo',
        nargs='?',
        help='Arquivo .f para executar'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Modo interativo'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='Facilitation Language v1.0.0'
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        modo_interativo()
    elif args.arquivo:
        executar_arquivo(args.arquivo)
    else:
        # Se não especificou arquivo nem modo interativo, tentar executar exemplo.f
        if os.path.exists('exemplo.f'):
            executar_arquivo('exemplo.f')
        else:
            print("❌ Nenhum arquivo especificado e exemplo.f não encontrado.")
            print("Use --help para ver as opções disponíveis.")
            sys.exit(1)

def executar_arquivo(arquivo):
    """Executa um arquivo .f"""
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo '{arquivo}' não encontrado.")
        sys.exit(1)
    
    if not arquivo.endswith('.f'):
        print(f"❌ Arquivo '{arquivo}' não tem extensão .f")
        sys.exit(1)
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        print(f"🚀 Executando {arquivo}...")
        print("=" * 50)
        
        interpretar(codigo)
        
        print("=" * 50)
        print("✅ Execução concluída!")
        
    except Exception as e:
        print(f"❌ Erro ao executar {arquivo}: {e}")
        sys.exit(1)

def modo_interativo():
    """Modo interativo para testar comandos"""
    print("🐍 Facilitation Language - Modo Interativo")
    print("Digite 'sair' para sair, 'ajuda' para ajuda")
    print("=" * 50)
    
    codigo_completo = ""
    
    while True:
        try:
            linha = input("facilitation> ")
            
            if linha.lower() in ['sair', 'exit', 'quit']:
                print("👋 Até logo!")
                break
            
            if linha.lower() in ['ajuda', 'help']:
                mostrar_ajuda()
                continue
            
            if linha.strip() == '':
                continue
            
            codigo_completo += linha + "\n"
            
            # Tentar executar o código acumulado
            try:
                interpretar(codigo_completo)
                codigo_completo = ""  # Limpar após execução bem-sucedida
            except Exception as e:
                # Se der erro, pode ser que o código não esteja completo
                # Continuar acumulando linhas
                pass
                
        except KeyboardInterrupt:
            print("\n👋 Até logo!")
            break
        except EOFError:
            print("\n👋 Até logo!")
            break

def mostrar_ajuda():
    """Mostra ajuda do modo interativo"""
    print("""
📚 Comandos disponíveis:
  escreva "mensagem"     - Exibe uma mensagem
  entrada texto nome     - Recebe entrada do usuário
  variavel bool x = Falso - Declara uma variável
  se condicao            - Estrutura condicional
  pare                   - Para a execução
  
📝 Exemplos:
  escreva "Olá, Mundo!"
  entrada texto nome "Digite seu nome: "
  variavel bool ativo = Verdadeiro
  
🔧 Comandos especiais:
  sair                   - Sai do modo interativo
  ajuda                  - Mostra esta ajuda
""")

if __name__ == "__main__":
    main() 