#!/usr/bin/env python3
"""
Script para configurar o repositório Git para o projeto Facilitation Language
"""

import os
import subprocess
import sys

def run_command(command):
    """Executa um comando e retorna o resultado"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    print("🚀 Configurando repositório Git para Facilitation Language")
    print("=" * 60)
    
    # Verificar se Git está instalado
    success, stdout, stderr = run_command("git --version")
    if not success:
        print("❌ Git não está instalado. Por favor, instale o Git primeiro.")
        return
    
    print(f"✅ Git encontrado: {stdout.strip()}")
    
    # Inicializar repositório Git
    if not os.path.exists(".git"):
        success, stdout, stderr = run_command("git init")
        if success:
            print("✅ Repositório Git inicializado")
        else:
            print(f"❌ Erro ao inicializar Git: {stderr}")
            return
    else:
        print("✅ Repositório Git já existe")
    
    # Adicionar todos os arquivos
    success, stdout, stderr = run_command("git add .")
    if success:
        print("✅ Arquivos adicionados ao staging")
    else:
        print(f"❌ Erro ao adicionar arquivos: {stderr}")
        return
    
    # Fazer commit inicial
    success, stdout, stderr = run_command('git commit -m "Initial commit: Facilitation Language v1.0.0"')
    if success:
        print("✅ Commit inicial realizado")
    else:
        print(f"❌ Erro ao fazer commit: {stderr}")
        return
    
    print("\n🎉 Configuração concluída!")
    print("\n📋 Próximos passos:")
    print("1. Crie um repositório no GitHub")
    print("2. Execute os comandos:")
    print("   git remote add origin https://github.com/perepepeu/facilitation-lang.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("\n3. Atualize o README.md com o link correto do seu repositório")
    print("4. Configure as GitHub Actions se necessário")
    
    print("\n📁 Arquivos criados:")
    files = [
        ".gitignore",
        "requirements.txt", 
        "setup.py",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/feature_request.md",
        ".github/workflows/python-app.yml"
    ]
    
    for file in files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} (não encontrado)")

if __name__ == "__main__":
    main() 