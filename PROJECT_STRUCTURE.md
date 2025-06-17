# 📁 Estrutura do Projeto

```
facilitation-lang/
├── src/                          # Código fonte
│   └── facilitation/             # Pacote principal
│       ├── __init__.py          # Inicialização do pacote
│       ├── lexer.py             # Analisador léxico
│       ├── parser.py            # Analisador sintático
│       ├── interpreter.py       # Interpretador
│       └── cli.py               # Interface de linha de comando
├── examples/                     # Exemplos de código
│   ├── exemplo.f                # Exemplo básico
│   ├── demo.f                   # Demonstração
│   └── teste.f                  # Testes
├── .github/                      # Configurações do GitHub
│   ├── ISSUE_TEMPLATE/          # Templates para issues
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/               # GitHub Actions
│       └── python-app.yml
├── main.py                      # Arquivo principal
├── setup.py                     # Configuração de instalação
├── requirements.txt             # Dependências
├── README.md                    # Documentação principal
├── CONTRIBUTING.md              # Guia de contribuição
├── CHANGELOG.md                 # Histórico de mudanças
├── CODE_OF_CONDUCT.md           # Código de conduta
├── LICENSE                      # Licença MIT
├── .gitignore                   # Arquivos ignorados pelo Git
├── GITHUB_SETUP.md              # Guia para GitHub
├── setup_git.py                 # Script de configuração Git
└── PROJECT_STRUCTURE.md         # Este arquivo
```

## 🏗️ Arquitetura

### **src/facilitation/**
- **lexer.py**: Converte código fonte em tokens
- **parser.py**: Converte tokens em árvore sintática (AST)
- **interpreter.py**: Executa a AST
- **cli.py**: Interface de linha de comando
- **__init__.py**: Inicialização e exportações do pacote

### **examples/**
- Arquivos `.f` com exemplos de código
- Demonstrações das funcionalidades
- Testes da linguagem

### **Documentação**
- **README.md**: Documentação principal
- **CONTRIBUTING.md**: Como contribuir
- **CHANGELOG.md**: Histórico de versões
- **CODE_OF_CONDUCT.md**: Código de conduta

### **Configuração**
- **setup.py**: Configuração para distribuição
- **requirements.txt**: Dependências
- **.gitignore**: Arquivos ignorados
- **.github/**: Configurações do GitHub

## 🚀 Como Usar

### Execução básica:
```bash
python main.py
```

### Executar arquivo específico:
```bash
python main.py examples/exemplo.f
```

### Modo interativo:
```bash
python -m src.facilitation.cli --interactive
```

### Instalação:
```bash
pip install -e .
facilitation examples/exemplo.f
```

## 📋 Padrões de Desenvolvimento

1. **Estrutura src/**: Código fonte organizado
2. **Documentação**: README e guias completos
3. **Testes**: Exemplos funcionais
4. **CI/CD**: GitHub Actions configurado
5. **Licença**: MIT para uso livre
6. **Contribuição**: Guias e templates

---

**Estrutura profissional e escalável!** 🎯 