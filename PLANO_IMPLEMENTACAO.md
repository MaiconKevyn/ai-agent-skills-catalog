# AI Agent Skills Catalog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transformar este repositório em um catálogo curado de skills úteis para Codex, Claude e agentes de desenvolvimento em projetos reais.

**Architecture:** O repositório deve ser documental e mínimo: um catálogo principal em Markdown, uma política simples de curadoria e um ciclo de revisão para manter links e descrições consistentes. Não haverá código de aplicação, infraestrutura, notebooks ou arquivos herdados do antigo projeto MinIO/DuckDB.

**Tech Stack:** Markdown, Git, fontes públicas oficiais e curadorias públicas de skills.

---

## Nome Do Repositório

**Nome escolhido:** `ai-agent-skills-catalog`

**Motivo:** o nome comunica que o objetivo não é específico de Codex ou Claude, mas sim um catálogo prático de skills para agentes de IA usados em engenharia, produto, design, arquitetura e operações de software.

**Descrição curta sugerida para o GitHub:** Curadoria de skills úteis para Codex, Claude e agentes de IA aplicados a projetos de software, produto, UX/UI, arquitetura e engenharia de IA.

## Estado Inicial

O conteúdo antigo do projeto `datawarehouse-minio-duckdb` deve ser removido por completo. O repositório deve começar sem Dockerfile, scripts, notebooks, código Python, cache, arquivos de IDE ou documentação antiga.

Arquivos esperados após esta etapa inicial:

- `PLANO_IMPLEMENTACAO.md`: este plano.

Arquivos esperados após a implementação do catálogo:

- `README.md`: visão geral curta do repositório e link para o catálogo.
- `SKILLS.md`: catálogo principal com as skills selecionadas.
- `CURATION.md`: critérios usados para aceitar, rejeitar e revisar skills.

## Fontes Iniciais Verificadas

Use estas fontes como ponto de partida obrigatório:

| Fonte | Link | Uso no catálogo |
|---|---|---|
| OpenAI Skills Catalog | https://github.com/openai/skills | Fonte oficial para skills compatíveis com Codex. |
| OpenAI Codex Skills Docs | https://developers.openai.com/codex/skills | Documentação oficial sobre uso de skills no Codex. |
| Anthropic Skills Repository | https://github.com/anthropics/skills | Fonte oficial de exemplos e skills para Claude. |
| Claude Code Skills Docs | https://code.claude.com/docs/en/skills | Documentação oficial sobre criação, organização e uso de skills no Claude Code. |
| Agent Skills Standard | https://agentskills.io | Referência de formato e interoperabilidade de skills. |
| Awesome Claude Skills | https://awesomeclaudeskills.com | Diretório público para priorizar skills populares e descobrir repositórios úteis. |
| Superpowers | https://github.com/obra/superpowers | Biblioteca de skills de workflow para desenvolvimento agentic. |
| Trail of Bits Skills | https://github.com/trailofbits/skills | Skills focadas em segurança, análise e revisão técnica. |
| Playwright Skill | https://github.com/lackeyjb/playwright-skill | Skill útil para automação e verificação browser-based. |
| shadcn/ui Skill | https://github.com/shadcn-ui/ui | Referência de skill/contexto para componentes e padrões de UI. |

## Escopo Do Catálogo

O `SKILLS.md` deve listar apenas skills ou coleções realmente úteis para projetos gerais. Cada entrada deve ter somente:

- nome da skill ou coleção;
- link;
- o que ela é.

Não incluir tutorial longo, instalação detalhada, opinião extensa ou comparação profunda. O objetivo é ser um índice limpo para consulta futura.

## Categorias Obrigatórias

O catálogo deve cobrir pelo menos estas categorias:

| Categoria | Objetivo |
|---|---|
| Engenharia de Software | Boas práticas de código, refatoração, revisão, testes, Git e CI. |
| Python | Qualidade, estrutura, testes, packaging, linting, typing e produtividade em Python. |
| UX/UI | Design de interfaces, acessibilidade, sistemas de design, shadcn/ui e validação visual. |
| Produto | Discovery, PRD, requisitos, priorização, user stories e definição de sucesso. |
| Scrum Master / Agile | Facilitação, planning, retro, refinamento, impedimentos e saúde do time. |
| Arquitetura Limpa | Boundaries, DDD, modularidade, SOLID, testes e redução de acoplamento. |
| Arquitetura de IA | RAG, agentes, evals, observabilidade, roteamento de modelos e pipelines. |
| AI Engineering | Prompting, tool use, evals, fine-tuning, guardrails, custo, latência e produção. |
| Segurança | Threat modeling, code review de segurança, SAST, supply chain e secrets. |
| Browser / E2E | Playwright, screenshots, verificação visual e fluxos end-to-end. |
| Documentos / Office | PDF, DOCX, XLSX, PPTX e automações documentais. |
| Dados / Analytics | Notebooks, SQL, data quality, visualização e análise exploratória. |

## Formato Final Do `SKILLS.md`

Use este formato exato:

```markdown
# AI Agent Skills Catalog

Catálogo curado de skills úteis para Codex, Claude e agentes de IA em projetos de software, produto, design, arquitetura e engenharia de IA.

Última revisão: YYYY-MM-DD

## Índice

- [Engenharia de Software](#engenharia-de-software)
- [Python](#python)
- [UX/UI](#uxui)
- [Produto](#produto)
- [Scrum Master / Agile](#scrum-master--agile)
- [Arquitetura Limpa](#arquitetura-limpa)
- [Arquitetura de IA](#arquitetura-de-ia)
- [AI Engineering](#ai-engineering)
- [Segurança](#segurança)
- [Browser / E2E](#browser--e2e)
- [Documentos / Office](#documentos--office)
- [Dados / Analytics](#dados--analytics)

## Engenharia de Software

| Skill | Link | O que é |
|---|---|---|
| Nome da skill | https://exemplo.com | Descrição curta, objetiva e verificável. |
```

Regras de descrição:

- escrever em PT-BR;
- usar uma frase curta;
- explicar a utilidade real da skill;
- não usar marketing;
- não repetir o nome da skill como descrição;
- não listar skills sem link público verificável.

## Critérios De Seleção

Uma skill entra no catálogo quando atende a pelo menos dois critérios:

- vem de fonte oficial, mantida ou amplamente usada;
- resolve um problema recorrente de projeto;
- é reutilizável em múltiplos contextos;
- tem documentação pública suficiente para avaliação;
- tem escopo claro e acionável;
- reduz risco operacional, técnico ou de qualidade;
- ajuda Codex, Claude ou outro agente a trabalhar com mais consistência.

Uma skill fica fora do catálogo quando:

- o link está morto;
- a descrição é vaga;
- parece abandonada e sem uso claro;
- é específica demais para um produto que o usuário não usa;
- executa automação sensível sem instruções de segurança;
- duplica outra skill melhor documentada.

## Plano De Implementação

### Task 1: Confirmar limpeza do repositório

**Files:**
- Validate: raiz do repositório

- [ ] **Step 1: Verificar arquivos restantes**

```bash
find . -maxdepth 3 -not -path './.git*' -print | sort
```

Expected: listar somente `.` e `./PLANO_IMPLEMENTACAO.md`.

- [ ] **Step 2: Verificar status Git**

```bash
git status --short
```

Expected: arquivos antigos aparecem como removidos e `PLANO_IMPLEMENTACAO.md` aparece como novo.

### Task 2: Criar estrutura documental mínima

**Files:**
- Create: `README.md`
- Create: `CURATION.md`
- Create: `SKILLS.md`

- [ ] **Step 1: Criar README.md**

Conteúdo esperado:

```markdown
# AI Agent Skills Catalog

Catálogo curado de skills úteis para Codex, Claude e agentes de IA aplicados a projetos de software, produto, UX/UI, arquitetura e engenharia de IA.

## Arquivos

- [SKILLS.md](SKILLS.md): catálogo principal.
- [CURATION.md](CURATION.md): critérios de curadoria.
- [PLANO_IMPLEMENTACAO.md](PLANO_IMPLEMENTACAO.md): plano de implementação.
```

- [ ] **Step 2: Criar CURATION.md**

Conteúdo esperado:

```markdown
# Critérios De Curadoria

Uma skill entra no catálogo quando tem link público verificável, utilidade recorrente em projetos e escopo claro.

Uma skill fica fora quando o link está morto, a descrição é vaga, o escopo é muito específico ou há alternativa mais confiável.

Cada revisão deve checar links, remover duplicatas e manter descrições curtas em PT-BR.
```

- [ ] **Step 3: Criar SKILLS.md com a estrutura base**

Use o formato definido na seção `Formato Final Do SKILLS.md`.

### Task 3: Buscar e registrar candidatos

**Files:**
- Modify: `SKILLS.md`

- [ ] **Step 1: Revisar fontes oficiais**

Abrir e extrair candidatos de:

```text
https://github.com/openai/skills
https://github.com/anthropics/skills
https://code.claude.com/docs/en/skills
https://agentskills.io
```

Expected: selecionar skills oficiais ou coleções oficiais que cubram Codex, Claude, documentos, desenvolvimento, automação e workflows.

- [ ] **Step 2: Revisar fontes comunitárias confiáveis**

Abrir e extrair candidatos de:

```text
https://awesomeclaudeskills.com
https://github.com/obra/superpowers
https://github.com/trailofbits/skills
https://github.com/lackeyjb/playwright-skill
https://github.com/shadcn-ui/ui
```

Expected: selecionar somente entradas com utilidade geral, documentação pública e link verificável.

- [ ] **Step 3: Mapear cada candidato para uma categoria**

Cada candidato deve aparecer em apenas uma categoria principal. Se uma skill servir para duas categorias, escolher a categoria onde ela tem maior uso prático.

### Task 4: Escrever o catálogo inicial

**Files:**
- Modify: `SKILLS.md`

- [ ] **Step 1: Preencher Engenharia de Software**

Incluir skills para revisão de código, debugging, TDD, planejamento, GitHub, CI e execução de planos.

- [ ] **Step 2: Preencher Python**

Incluir skills para qualidade de código Python, testes, packaging, linting, typing e análise de dados quando aplicável.

- [ ] **Step 3: Preencher UX/UI**

Incluir skills para design systems, shadcn/ui, acessibilidade, verificação visual e frontend.

- [ ] **Step 4: Preencher Produto e Agile**

Incluir skills para PRD, priorização, user stories, facilitação, retros e refinamento.

- [ ] **Step 5: Preencher Arquitetura, IA e AI Engineering**

Incluir skills para arquitetura limpa, agentes, RAG, evals, observabilidade, guardrails e produção.

- [ ] **Step 6: Preencher Segurança, Browser, Documentos e Dados**

Incluir skills para segurança, Playwright, PDF/DOCX/XLSX/PPTX e analytics.

### Task 5: Revisar inconsistências

**Files:**
- Modify: `SKILLS.md`
- Modify: `CURATION.md` se algum critério precisar ficar mais explícito

- [ ] **Step 1: Validar links**

```bash
python - <<'PY'
from pathlib import Path
import re

text = Path("SKILLS.md").read_text()
links = sorted(set(re.findall(r"https?://[^\s)]+", text)))
for link in links:
    print(link)
PY
```

Expected: imprimir todos os links usados para revisão manual ou validação via browser.

- [ ] **Step 2: Procurar descrições longas**

```bash
awk -F '|' '/^\| [^|-]/ { if (length($4) > 140) print NR ":" $0 }' SKILLS.md
```

Expected: nenhuma linha de descrição deve ultrapassar 140 caracteres, exceto se houver justificativa clara.

- [ ] **Step 3: Procurar entradas incompletas**

```bash
grep -nE 'TBD|TODO|exemplo.com|Nome da skill|Descrição curta' SKILLS.md
```

Expected: nenhum resultado.

- [ ] **Step 4: Revisar duplicatas**

```bash
awk -F '|' '/^\| \[/ { gsub(/^ +| +$/, "", $2); print $2 }' SKILLS.md | sort | uniq -d
```

Expected: nenhum nome duplicado.

### Task 6: Fechar primeira versão

**Files:**
- Modify: `README.md`
- Modify: `SKILLS.md`
- Modify: `CURATION.md`

- [ ] **Step 1: Atualizar data de revisão**

Em `SKILLS.md`, preencher `Última revisão` com a data da revisão final.

- [ ] **Step 2: Validar diff**

```bash
git diff --stat
git diff -- README.md SKILLS.md CURATION.md PLANO_IMPLEMENTACAO.md
```

Expected: diff deve conter apenas documentação do novo catálogo.

- [ ] **Step 3: Commit sugerido**

```bash
git add README.md SKILLS.md CURATION.md PLANO_IMPLEMENTACAO.md
git commit -m "docs: repurpose repository as agent skills catalog"
```

Expected: commit criado sem arquivos antigos ou gerados.

## Revisão Final Antes De Publicar

Antes de push ou rename remoto:

- [ ] Confirmar se o repositório remoto deve ser renomeado para `ai-agent-skills-catalog`.
- [ ] Confirmar se o histórico antigo deve ser mantido ou se será recriado em um repo novo.
- [ ] Confirmar se `datawarehouse-minio-duckdb` pode deixar de existir no GitHub com esse nome.
- [ ] Rodar `git status --short --branch`.
- [ ] Revisar `git remote -v`.

## Próxima Ação Recomendada

Executar este plano criando `README.md`, `CURATION.md` e `SKILLS.md`, depois preencher o catálogo inicial a partir das fontes verificadas.
