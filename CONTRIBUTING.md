# Guia de Contribuição

Obrigado por se interessar em contribuir com a Linguagem Facilitation! 🎉

## Como Contribuir

### 1. Fork e Clone
1. Faça um fork do repositório
2. Clone o fork para sua máquina local:
```bash
git clone https://github.com/perepepeu/facilitation-lang.git
cd facilitation-lang
```

### 2. Configurar Ambiente
1. Instale as dependências (se houver):
```bash
pip install -r requirements.txt
```

2. Teste se tudo está funcionando:
```bash
python facilitation/main.py
```

### 3. Criar uma Branch
```bash
git checkout -b feature/nova-funcionalidade
# ou
git checkout -b fix/correcao-bug
```

### 4. Desenvolver
- Adicione novas funcionalidades
- Corrija bugs
- Melhore a documentação
- Adicione testes

### 5. Testar
Certifique-se de que:
- O código funciona corretamente
- Não quebra funcionalidades existentes
- Segue as convenções do projeto

### 6. Commit e Push
```bash
git add .
git commit -m "Adiciona nova funcionalidade X"
git push origin feature/nova-funcionalidade
```

### 7. Pull Request
1. Vá para o repositório original no GitHub
2. Clique em "New Pull Request"
3. Selecione sua branch
4. Descreva suas mudanças
5. Aguarde a revisão

## Diretrizes de Código

### Python
- Use Python 3.8+
- Siga o PEP 8
- Adicione docstrings para funções
- Use nomes descritivos para variáveis

### Linguagem Facilitation
- Mantenha a sintaxe em português
- Seja consistente com os comandos existentes
- Adicione exemplos na documentação

## Estrutura do Projeto

```
facilitation-lang/
├── interpretador/          # Lexer
├── tokens/                 # Parser
├── interpreta_os_comandos/ # Interpreter
├── facilitation/           # Main application
├── exemplos/              # Exemplos de código
├── README.md              # Documentação principal
└── setup.py               # Configuração de instalação
```

## Reportando Bugs

1. Use o template de issue
2. Descreva o problema claramente
3. Inclua um exemplo mínimo reproduzível
4. Especifique sua versão do Python

## Sugerindo Funcionalidades

1. Abra uma issue
2. Descreva a funcionalidade desejada
3. Explique o benefício
4. Forneça exemplos de uso

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a licença MIT.

---

Obrigado por contribuir! 🚀 