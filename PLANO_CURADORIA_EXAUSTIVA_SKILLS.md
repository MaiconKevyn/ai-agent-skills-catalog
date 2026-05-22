# Exhaustive Agent Skills Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fazer uma busca mais exaustiva pelas skills mais importantes para Claude e Codex, reorganizando o repositório por categorias pesquisáveis e atualizando o README para posicionar o projeto como um hub central de consulta.

**Architecture:** O repositório deve evoluir de um único catálogo em `SKILLS.md` para um catálogo navegável com índice principal, páginas por categoria, metadados estruturados e validações automáticas. O Markdown continua sendo a fonte humana de leitura, mas um arquivo estruturado deve permitir busca, filtros, deduplicação e geração futura de índices.

**Tech Stack:** Markdown, YAML ou JSON, Python 3 standard library, GitHub CLI, GitHub API, links oficiais e diretórios públicos de skills.

---

## Resultado Esperado

Ao final da implementação deste plano, o repositório deve conter:

- um índice central atualizado em `README.md`;
- um catálogo principal atualizado em `SKILLS.md`;
- páginas por categoria em `categories/`;
- um arquivo estruturado em `data/skills.yml`;
- um arquivo de fontes em `data/sources.yml`;
- scripts simples em `scripts/` para validar links, duplicatas e consistência;
- documentação clara para adicionar novas skills;
- commit e push feitos no branch `main`.

## Escopo Da Busca Exaustiva

A busca deve priorizar skills para:

- Claude Code;
- OpenAI Codex;
- agentes compatíveis com o padrão `SKILL.md`;
- Cursor, Gemini CLI, GitHub Copilot, Windsurf e OpenCode quando a skill também for reutilizável por Claude/Codex;
- MCP, browser automation, segurança, AI engineering, design, produto e engenharia de software.

Não incluir:

- skills sem link público verificável;
- skills sem `SKILL.md`, README ou documentação equivalente;
- skills abandonadas sem utilidade clara;
- repositórios com finalidade maliciosa, automação abusiva ou risco óbvio;
- duplicatas piores de uma skill oficial ou mais madura.

## Fontes Obrigatórias

Começar por estas fontes, porque elas são oficiais, amplas ou têm forte sinal público:

| Fonte | Link | Tipo | Uso |
|---|---|---|---|
| OpenAI Skills | https://github.com/openai/skills | Oficial | Skills para Codex. |
| OpenAI Codex Skills Docs | https://developers.openai.com/codex/skills | Oficial | Regras de uso e empacotamento para Codex. |
| Anthropic Skills | https://github.com/anthropics/skills | Oficial | Skills para Claude. |
| Claude Code Skills Docs | https://code.claude.com/docs/en/skills | Oficial | Regras de criação e uso no Claude Code. |
| Agent Skills Standard | https://agentskills.io/ | Padrão | Formato aberto de skills e interoperabilidade. |
| Vercel Agent Skills | https://vercel.com/docs/agent-resources/skills | Oficial | Diretório oficial de skills da Vercel. |
| Vercel Agent Skills Repo | https://github.com/vercel-labs/agent-skills | Oficial | Coleção da Vercel para agentes e apps modernos. |
| Awesome Agent Skills | https://github.com/VoltAgent/awesome-agent-skills | Diretório | Lista ampla de skills compatíveis com Claude, Codex, Gemini CLI e Cursor. |
| Awesome Skills Directory | https://www.awesomeskills.dev/ | Diretório | Descoberta de skills por popularidade e compatibilidade. |
| Awesome Agent Skills Directory | https://awesomeagentskills.dev/ | Diretório | Índice pesquisável de skills e MCP servers. |
| MDSkill | https://mdskill.dev/ | Diretório | Diretório com sinal de segurança, estrelas e plataforma. |
| GitHub Topic agent-skills | https://github.com/topics/agent-skills | Diretório | Descoberta de repositórios recentes e populares. |
| Superpowers | https://github.com/obra/superpowers | Workflow | Skills de metodologia para engenharia agentic. |
| Trail of Bits Skills | https://github.com/trailofbits/skills | Segurança | Skills de auditoria, análise e segurança. |
| shadcn/ui Skills | https://github.com/shadcn-ui/ui/tree/main/skills | UI | Skills e padrões para UI/components. |

## Taxonomia Alvo

Criar páginas separadas em `categories/` com estes arquivos:

| Categoria | Arquivo |
|---|---|
| Engenharia de Software | `categories/software-engineering.md` |
| Python | `categories/python.md` |
| UX/UI e Frontend | `categories/ux-ui-frontend.md` |
| Produto | `categories/product.md` |
| Agile e Scrum Master | `categories/agile-scrum.md` |
| Arquitetura Limpa | `categories/clean-architecture.md` |
| Arquitetura de IA | `categories/ai-architecture.md` |
| AI Engineering | `categories/ai-engineering.md` |
| Segurança | `categories/security.md` |
| Browser e E2E | `categories/browser-e2e.md` |
| Documentos e Office | `categories/docs-office.md` |
| Dados e Analytics | `categories/data-analytics.md` |
| MCP e Tool Use | `categories/mcp-tool-use.md` |
| DevOps e Deploy | `categories/devops-deploy.md` |
| Pesquisa e Escrita | `categories/research-writing.md` |

Cada página deve conter:

- visão geral da categoria;
- tabela com skill, plataforma, fonte, maturidade e descrição;
- seção "Top picks" com as skills mais úteis;
- seção "Quando usar";
- link de volta para `README.md` e `SKILLS.md`.

## Modelo De Dados

Criar `data/skills.yml` com esta estrutura:

```yaml
skills:
  - name: "modern-python"
    url: "https://github.com/trailofbits/skills/tree/main/plugins/modern-python"
    source: "Trail of Bits Skills"
    source_url: "https://github.com/trailofbits/skills"
    platforms:
      - "Claude"
      - "Codex"
      - "SKILL.md"
    categories:
      - "Python"
      - "Engenharia de Software"
    maturity: "high"
    signal:
      official: false
      stars: null
      maintained: true
      security_review_needed: false
    description_ptbr: "Skill para práticas modernas de Python, typing, estrutura e segurança."
    notes: "Prioritária para projetos Python."
```

Criar `data/sources.yml` com esta estrutura:

```yaml
sources:
  - name: "OpenAI Skills"
    url: "https://github.com/openai/skills"
    type: "official"
    platforms:
      - "Codex"
    discovery_method: "GitHub API"
    priority: "high"
```

## Critérios De Priorização

Classificar cada skill com uma maturidade:

| Maturidade | Regra |
|---|---|
| `high` | Oficial, muito usada, documentada, com escopo claro e baixo risco. |
| `medium` | Comunitária, útil, documentada, mas com menor sinal público. |
| `experimental` | Promissora, recente ou específica, requer revisão antes de uso. |
| `watchlist` | Deve ser acompanhada, mas ainda não entra no catálogo principal. |

Critérios para entrar em "Top picks":

- resolve problema recorrente em projetos reais;
- tem documentação clara;
- funciona para Claude, Codex ou padrão `SKILL.md`;
- tem sinal de manutenção, estrelas, uso ou origem oficial;
- não exige confiança cega em scripts perigosos.

## Plano De Implementação

### Task 1: Criar estrutura de diretórios

**Files:**
- Create: `categories/`
- Create: `data/`
- Create: `scripts/`

- [ ] **Step 1: Criar diretórios**

```bash
mkdir -p categories data scripts
```

Expected: os diretórios `categories`, `data` e `scripts` existem.

- [ ] **Step 2: Confirmar árvore**

```bash
find . -maxdepth 2 -type d -not -path './.git*' | sort
```

Expected: listar `./assets`, `./categories`, `./data` e `./scripts`.

### Task 2: Criar inventário de fontes

**Files:**
- Create: `data/sources.yml`

- [ ] **Step 1: Registrar fontes obrigatórias**

Criar `data/sources.yml` com todas as fontes da seção "Fontes Obrigatórias".

- [ ] **Step 2: Validar URLs das fontes**

```bash
python3 scripts/check_links.py data/sources.yml
```

Expected: todas as URLs retornam status HTTP menor que 400 ou redirect aceitável.

### Task 3: Implementar validadores mínimos

**Files:**
- Create: `scripts/check_links.py`
- Create: `scripts/check_catalog.py`

- [ ] **Step 1: Criar `scripts/check_links.py`**

O script deve:

- receber arquivos Markdown/YAML como argumentos;
- extrair links `http` e `https`;
- testar cada link com `HEAD` e fallback para `GET`;
- imprimir `checked=N failed=0` quando tudo passa;
- retornar exit code `1` se houver falha.

- [ ] **Step 2: Criar `scripts/check_catalog.py`**

O script deve:

- ler `data/skills.yml`;
- garantir que cada skill tem `name`, `url`, `source`, `platforms`, `categories`, `maturity` e `description_ptbr`;
- rejeitar nomes duplicados;
- rejeitar URLs duplicadas, exceto quando a duplicata estiver marcada como coleção;
- validar maturidade em `high`, `medium`, `experimental` ou `watchlist`;
- confirmar que cada categoria tem arquivo correspondente em `categories/`.

- [ ] **Step 3: Rodar scripts**

```bash
python3 scripts/check_links.py README.md SKILLS.md CURATION.md PLANO_IMPLEMENTACAO.md PLANO_CURADORIA_EXAUSTIVA_SKILLS.md
python3 scripts/check_catalog.py
```

Expected: ambos retornam exit code `0`.

### Task 4: Buscar candidates oficiais

**Files:**
- Modify: `data/skills.yml`
- Modify: `SKILLS.md`

- [ ] **Step 1: Coletar OpenAI Skills**

```bash
curl -fsSL https://api.github.com/repos/openai/skills/contents/skills/.curated?ref=main
curl -fsSL https://api.github.com/repos/openai/skills/contents/skills/.system?ref=main
```

Expected: registrar todas as skills oficiais relevantes para Codex.

- [ ] **Step 2: Coletar Anthropic Skills**

```bash
curl -fsSL https://api.github.com/repos/anthropics/skills/contents/skills?ref=main
```

Expected: registrar todas as skills oficiais relevantes para Claude.

- [ ] **Step 3: Coletar Vercel Agent Skills**

```bash
curl -fsSL https://api.github.com/repos/vercel-labs/agent-skills/contents?ref=main
```

Expected: registrar skills aplicáveis a frontend, Next.js, Vercel, AI SDK, deploy, auth, storage e observability.

### Task 5: Buscar candidates comunitários com sinal forte

**Files:**
- Modify: `data/skills.yml`
- Modify: `data/sources.yml`
- Modify: `SKILLS.md`

- [ ] **Step 1: Revisar diretórios públicos**

Abrir e buscar candidates em:

```text
https://www.awesomeskills.dev/
https://awesomeagentskills.dev/
https://mdskill.dev/
https://github.com/topics/agent-skills
```

Expected: registrar apenas repositórios com link público, descrição clara e utilidade geral.

- [ ] **Step 2: Revisar coleções comunitárias**

Priorizar:

```text
https://github.com/VoltAgent/awesome-agent-skills
https://github.com/obra/superpowers
https://github.com/trailofbits/skills
https://github.com/antfu/skills
https://github.com/lackeyjb/playwright-skill
https://github.com/product-on-purpose/pm-skills
```

Expected: registrar skills maduras e mover experimentais para `watchlist`.

- [ ] **Step 3: Filtrar risco**

Para cada skill comunitária com scripts:

```bash
find <repo-or-skill-folder> -maxdepth 3 -type f | sort
```

Expected: skills com scripts sensíveis, downloads externos ou automação destrutiva ficam como `experimental` ou `watchlist`.

### Task 6: Gerar páginas por categoria

**Files:**
- Create: `categories/*.md`
- Modify: `SKILLS.md`

- [ ] **Step 1: Criar página para cada categoria**

Cada arquivo deve usar este formato:

```markdown
# Nome Da Categoria

Voltar: [README](../README.md) | [Catálogo principal](../SKILLS.md)

## Top Picks

| Skill | Plataforma | Fonte | Maturidade | O que é |
|---|---|---|---|---|

## Todas As Skills

| Skill | Plataforma | Fonte | Maturidade | O que é |
|---|---|---|---|---|

## Quando Usar

- Use esta categoria quando ...
```

- [ ] **Step 2: Atualizar `SKILLS.md`**

`SKILLS.md` deve virar índice de alto nível apontando para `categories/*.md`, mantendo uma tabela resumida das top skills.

### Task 7: Atualizar README para busca e navegação

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Atualizar badges**

Atualizar o número total de skills após a expansão.

- [ ] **Step 2: Adicionar navegação por categoria**

Criar seção "Explore Por Categoria" com links para todos os arquivos em `categories/`.

- [ ] **Step 3: Adicionar fontes de descoberta**

Criar seção "Fontes de Descoberta" com links para oficiais, diretórios e coleções comunitárias.

- [ ] **Step 4: Adicionar fluxo de contribuição**

Explicar que novas skills devem entrar primeiro em `data/skills.yml`, depois nas páginas de categoria.

### Task 8: Validar consistência final

**Files:**
- Validate: `README.md`
- Validate: `SKILLS.md`
- Validate: `categories/*.md`
- Validate: `data/*.yml`
- Validate: `scripts/*.py`

- [ ] **Step 1: Rodar validação de links**

```bash
python3 scripts/check_links.py README.md SKILLS.md CURATION.md PLANO_IMPLEMENTACAO.md PLANO_CURADORIA_EXAUSTIVA_SKILLS.md categories/*.md data/*.yml
```

Expected: `checked=N failed=0`.

- [ ] **Step 2: Rodar validação do catálogo**

```bash
python3 scripts/check_catalog.py
```

Expected: `catalog=valid`.

- [ ] **Step 3: Procurar placeholders**

```bash
grep -RInE 'TB[D]|TO''DO|exemplo[.]com|Nome da skil[l]|Descrição curt[a]|link-public[o]' README.md SKILLS.md CURATION.md categories data scripts *.md
```

Expected: nenhum resultado fora de blocos explicativos intencionais.

- [ ] **Step 4: Validar diff**

```bash
git diff --stat
git diff -- README.md SKILLS.md CURATION.md PLANO_CURADORIA_EXAUSTIVA_SKILLS.md categories data scripts
```

Expected: diff contém apenas documentação, catálogo e scripts de validação.

### Task 9: Commit e push obrigatórios

**Files:**
- Commit: todos os arquivos alterados/criados por este plano

- [ ] **Step 1: Conferir status**

```bash
git status --short --branch
```

Expected: somente arquivos do catálogo, planos, categorias, dados e scripts aparecem como modificados ou novos.

- [ ] **Step 2: Stage explícito**

```bash
git add README.md SKILLS.md CURATION.md PLANO_CURADORIA_EXAUSTIVA_SKILLS.md categories data scripts
```

Expected: somente arquivos da curadoria exaustiva entram no índice.

- [ ] **Step 3: Commit**

```bash
git commit -m "docs: plan exhaustive agent skills catalog expansion"
```

Expected: commit criado.

- [ ] **Step 4: Push**

```bash
git push origin main
```

Expected: `main` remoto recebe o commit.

- [ ] **Step 5: Verificação pós-push**

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
git ls-remote origin refs/heads/main
```

Expected: worktree limpo e `HEAD`, `origin/main` e remoto apontam para o mesmo SHA.

## Checklist De Aceite

- [ ] `PLANO_CURADORIA_EXAUSTIVA_SKILLS.md` existe e descreve busca, organização, validação, commit e push.
- [ ] `README.md` aponta para o novo plano e explica a próxima fase de organização por categorias.
- [ ] As fontes principais para Claude e Codex estão listadas.
- [ ] A taxonomia futura cobre engenharia, produto, design, arquitetura, IA, segurança, dados e documentos.
- [ ] O plano deixa claro que a implementação final precisa fazer commit e push.
