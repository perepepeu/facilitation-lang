[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/perepepeu/facilitation-lang/python-app.yml?branch=main)](https://github.com/perepepeu/facilitation-lang/actions)
[![GitHub Issues](https://img.shields.io/github/issues/perepepeu/facilitation-lang)](https://github.com/perepepeu/facilitation-lang/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/perepepeu/facilitation-lang)](https://github.com/perepepeu/facilitation-lang/pulls)

# Linguagem Facilitation

Uma linguagem de programação simples e intuitiva em português, focada em ajudar iniciantes a aprender programação de forma fácil.

## 🚀 Características

- **Sintaxe em português**: Comandos simples e intuitivos
- **Sistema de tipos**: texto, quebrada, numero, bool
- **Estruturas condicionais**: se/senão/fim
- **Operações matemáticas**: +, -, *, /
- **Variáveis tipadas**: Declaração explícita de tipos
- **Comentários**: Sistema de documentação com #
- **Tratamento de erros**: Mensagens claras e úteis

## 📁 Estrutura do Projeto

```
facilitation-lang/
├── interpretador/          # Lexer (análise léxica)
├── tokens/                 # Parser (análise sintática)
├── interpreta_os_comandos/ # Interpreter (execução)
├── facilitation/           # Aplicação principal
├── exemplos/              # Exemplos de código
├── exemplo.f              # Exemplo de programa
└── README.md              # Documentação
```

## 🎯 Como Usar

### Executar um programa
```bash
python facilitation/main.py
```

### Exemplo de código
```facilitation
escreva "Olá, Mundo!"
entrada texto nome "Digite seu nome: "
escreva "Ola " + nome
```

## 📝 Sintaxe da Linguagem

### 1. **escreva**
Exibe uma mensagem no terminal.
```facilitation
escreva "mensagem"
```

### 2. **entrada**
Recebe um valor do usuário. Pode especificar o tipo:
- `texto` para strings
- `quebrada` para números decimais (float)
- `numero` para inteiros

Com prompt:
```facilitation
entrada texto nome "Qual é seu nome? "
entrada quebrada numero1
entrada numero numero2
```

### 3. **variavel**
Declara uma variável com tipo e valor inicial.
- `bool` para booleanos (`Verdadeiro`, `Falso`, `True`, `False`, `1`, `0`)
```facilitation
variavel bool codigo_ja_rodou = Falso
```

### 4. **se / senão / fim**
Estrutura condicional:
```facilitation
se condicao
    // comandos
senão
    // comandos
fim
```

Exemplo:
```facilitation
se operacao for "+"
    resultado = numero1 + numero2
senão
    escreva "Operação inválida."
    pare
fim
```

### 5. **pare**
Interrompe a execução do programa.
```facilitation
pare
```

### 6. **comentários**
Use `#` para comentários.
```facilitation
# Este é um comentário
```

### 7. **Atribuição**
Atribui valores a variáveis:
```facilitation
resultado = numero1 + numero2
codigo_ja_rodou = Verdadeiro
```

### 8. **Operadores**
- `+`, `-`, `*`, `/` para operações matemáticas
- `for ==`, `for` para comparações

## 📊 Tipos de Dados

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `texto` | Strings | `"Olá mundo"` |
| `quebrada` | Números decimais | `3.14`, `-2.5` |
| `numero` | Números inteiros | `42`, `-10` |
| `bool` | Booleanos | `Verdadeiro`, `Falso` |

## 🔧 Exemplo Completo

```facilitation
escreva "Calculadora Facilitation - Teste Completo"

entrada texto nome "Digite seu nome: "
escreva "Ola " + nome

entrada quebrada numero1 "Digite o primeiro numero: "
entrada quebrada numero2 "Digite o segundo numero: "

escreva "Escolha a operacao: +, -, *, /"
entrada operacao

variavel bool codigo_ja_rodou = Falso

se operacao for "+"
    resultado = numero1 + numero2
    escreva "O resultado e: " + resultado
senão operacao for "-"
    resultado = numero1 - numero2
    escreva "O resultado e: " + resultado
senão operacao for "*"
    resultado = numero1 * numero2
    escreva "O resultado e: " + resultado
senão operacao for "/"
    se numero2 for == 0
        escreva "Erro: divisao por zero!"
        pare
    fim
    resultado = numero1 / numero2
    escreva "O resultado e: " + resultado
senão
    escreva "Operacao invalida."
    pare
fim

codigo_ja_rodou = Verdadeiro
escreva "Programa finalizado com sucesso!"
```

## 🎓 Para Iniciantes

### Por que usar o Facilitation?

1. **Sintaxe simples**: Comandos em português
2. **Feedback imediato**: Veja o resultado de cada comando
3. **Sem erros complexos**: Mensagens de erro claras
4. **Aprendizado gradual**: Comece simples, evolua naturalmente

### Conceitos Básicos

- **Variável**: Um "caixa" que guarda informações
- **Tipo**: O tipo de informação (texto, número, etc.)
- **Valor**: A informação guardada na variável
- **Comando**: Instrução para o computador

## 🚧 Funcionalidades Futuras

- [ ] Loops `enquanto` e `para`
- [ ] Funções personalizadas
- [ ] Arrays/listas
- [ ] Mais operadores de comparação
- [ ] Sistema de módulos
- [ ] IDE/editor com syntax highlighting
- [ ] Compilador para bytecode
- [ ] Otimizações de performance

## 🤝 Contribuindo

Este é um projeto educacional! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novas funcionalidades
- Melhorar a documentação

Veja o [Guia de Contribuição](CONTRIBUTING.md) para mais detalhes.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔗 Links

- [Repositório no GitHub](https://github.com/perepepeu/facilitation-lang)
- [Issues](https://github.com/perepepeu/facilitation-lang/issues)
- [Pull Requests](https://github.com/perepepeu/facilitation-lang/pulls)

---

**Divirta-se programando! 🎉** 