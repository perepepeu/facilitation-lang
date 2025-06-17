# 🚀 Guia Completo para GitHub

## Passo a Passo para Publicar no GitHub

### 1. Preparar o Projeto

Execute o script de configuração:
```bash
python setup_git.py
```

### 2. Criar Repositório no GitHub

1. Acesse [github.com](https://github.com)
2. Clique em "New repository"
3. Configure:
   - **Repository name**: `facilitation-lang`
   - **Description**: `Uma linguagem de programação em português para facilitar o aprendizado`
   - **Visibility**: Public (recomendado)
   - **NÃO** inicialize com README (já temos um)
4. Clique em "Create repository"

### 3. Conectar ao GitHub

Execute os comandos:

```bash
git remote add origin https://github.com/perepepeu/facilitation-lang.git
git branch -M main
git push -u origin main
```

### 4. Configurar GitHub Pages (Opcional)

1. Vá em Settings > Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)
5. Save

### 5. Configurar Issues e Projects

1. **Issues**: Já configurados com templates
2. **Projects**: Crie um board para organizar tarefas
3. **Wiki**: Ative se quiser documentação adicional

### 6. Configurar GitHub Actions

O workflow já está configurado em `.github/workflows/python-app.yml`

### 7. Adicionar Badges ao README

Adicione estes badges no topo do README.md:

```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/perepepeu/facilitation-lang/python-app.yml?branch=main)](https://github.com/perepepeu/facilitation-lang/actions)
[![GitHub Issues](https://img.shields.io/github/issues/perepepeu/facilitation-lang)](https://github.com/perepepeu/facilitation-lang/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/perepepeu/facilitation-lang)](https://github.com/perepepeu/facilitation-lang/pulls)
```

### 8. Configurar Releases

1. Vá em Releases
2. "Create a new release"
3. Tag: `v1.0.0`
4. Title: `Facilitation Language v1.0.0`
5. Description: Use o conteúdo do CHANGELOG.md
6. Publish release

### 9. Configurar Topics

Adicione estes topics no repositório:
- `programming-language`
- `education`
- `portuguese`
- `interpreter`
- `lexer`
- `parser`
- `python`

### 10. Configurar Social Preview

1. Vá em Settings > General
2. Scroll até "Social preview"
3. Upload uma imagem 1280x640px

## 📋 Checklist Final

- [ ] Repositório criado no GitHub
- [ ] Código enviado para o GitHub
- [ ] README.md atualizado com links corretos
- [ ] Badges adicionados
- [ ] Issues templates funcionando
- [ ] GitHub Actions configurado
- [ ] Release v1.0.0 criado
- [ ] Topics adicionados
- [ ] Social preview configurado
- [ ] Projeto compartilhado nas redes sociais

## 🎯 Próximos Passos

1. **Compartilhar**: Divulgue seu projeto
2. **Manter**: Responda issues e pull requests
3. **Evoluir**: Continue desenvolvendo novas funcionalidades
4. **Documentar**: Mantenha a documentação atualizada

## 🔗 Links Úteis

- [GitHub Guides](https://guides.github.com/)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://github.com/features/actions)
- [GitHub Issues](https://guides.github.com/features/issues/)

---

**Parabéns!** 🎉 Seu projeto Facilitation Language está agora no GitHub! 