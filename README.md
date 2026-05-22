<p align="center">
  <img src="assets/skills-map.svg" alt="AI Agent Skills Catalog map" width="100%">
</p>

<h1 align="center">AI Agent Skills Catalog</h1>

<p align="center">
  Um hub curado das skills mais úteis para Codex, Claude e agentes de IA em projetos de software, produto, UX/UI, arquitetura e engenharia de IA.
</p>

<p align="center">
  <a href="SKILLS.md"><img alt="Curated skills" src="https://img.shields.io/badge/curated_skills-108-2dd4bf?style=for-the-badge"></a>
  <a href="SKILLS.md"><img alt="Categories" src="https://img.shields.io/badge/categories-12-7c5cff?style=for-the-badge"></a>
  <a href="CURATION.md"><img alt="Curation" src="https://img.shields.io/badge/curation-reviewed-0f172a?style=for-the-badge"></a>
  <a href="https://github.com/MaiconKevyn/ai-agent-skills-catalog"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MaiconKevyn/ai-agent-skills-catalog?style=for-the-badge"></a>
</p>

## Por Que Este Repo Existe

Skills viraram uma camada prática de operação para agentes: elas encapsulam padrões, ferramentas, critérios de decisão e workflows que um agente deve seguir sem reinventar tudo a cada tarefa. O problema é que as skills úteis estão espalhadas entre repositórios oficiais, catálogos comunitários e coleções especializadas.

Este repositório é uma curadoria enxuta para responder rápido:

- qual skill usar para uma tarefa real;
- onde está o link público confiável;
- qual problema aquela skill resolve;
- quais coleções valem acompanhar.

## Comece Aqui

| Arquivo | Para que serve |
|---|---|
| [SKILLS.md](SKILLS.md) | Catálogo principal com 108 skills e coleções organizadas por categoria. |
| [CURATION.md](CURATION.md) | Critérios para aceitar, rejeitar e revisar novas skills. |
| [PLANO_IMPLEMENTACAO.md](PLANO_IMPLEMENTACAO.md) | Plano original usado para transformar este repo em catálogo. |

## Mapa Do Catálogo

| Área | Quando usar |
|---|---|
| Engenharia de Software | Refatoração, debugging, TDD, revisão, GitHub e CI. |
| Python | Typing, testes, notebooks, análise estática e projetos empacotados. |
| UX/UI | Design systems, shadcn/ui, Figma, frontend e avaliação visual. |
| Produto | PRDs, user stories, critérios de aceite, discovery e roadmap. |
| Scrum Master / Agile | Facilitação, sprint, refinamento, retrospectivas e reuniões. |
| Arquitetura Limpa | SOLID, APIs, entrypoints, compliance com specs e handoffs técnicos. |
| Arquitetura de IA | MCP, APIs de LLM, criação de skills e estrutura de projetos agentic. |
| AI Engineering | Evals, guardrails, observabilidade, MLOps e verificação de agentes. |
| Segurança | Threat modeling, Semgrep, supply chain, revisão e análise estática. |
| Browser / E2E | Playwright, screenshots e testes web end-to-end. |
| Documentos / Office | PDF, DOCX, XLSX, PPTX, Notion e coautoria documental. |
| Dados / Analytics | CSV, dashboards, instrumentação, experimentos e métricas. |

## Repositórios Que Inspiraram A Curadoria

Referências com forte sinal do ecossistema, verificadas em 2026-05-22.

| Repositório | Sinal | Por que acompanhar |
|---|---:|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 201k+ stars | Workflows maduros para planejar, testar, revisar e finalizar tarefas agentic. |
| [anthropics/skills](https://github.com/anthropics/skills) | 138k+ stars | Repositório oficial de skills para Claude. |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 114k+ stars | Referência forte para componentes, design systems e distribuição de código. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 26k+ stars | Coleção oficial da Vercel para agentes e apps modernos. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 22k+ stars | Diretório amplo de skills compatíveis com Claude Code, Codex, Gemini CLI e Cursor. |
| [openai/skills](https://github.com/openai/skills) | 19k+ stars | Catálogo oficial de skills para Codex. |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 5k+ stars | Skills técnicas para segurança, auditoria e revisão avançada. |

## Trilhas Rápidas

| Se você quer... | Abra esta seção |
|---|---|
| Publicar código com agente | [Engenharia de Software](SKILLS.md#engenharia-de-software) |
| Melhorar qualidade Python | [Python](SKILLS.md#python) |
| Construir interface mais forte | [UX/UI](SKILLS.md#uxui) |
| Escrever PRD ou user stories | [Produto](SKILLS.md#produto) |
| Rodar cerimônias e alinhamento | [Scrum Master / Agile](SKILLS.md#scrum-master--agile) |
| Revisar arquitetura | [Arquitetura Limpa](SKILLS.md#arquitetura-limpa) |
| Projetar agentes e MCP | [Arquitetura de IA](SKILLS.md#arquitetura-de-ia) |
| Avaliar sistemas com IA | [AI Engineering](SKILLS.md#ai-engineering) |
| Checar risco técnico | [Segurança](SKILLS.md#segurança) |
| Validar app no browser | [Browser / E2E](SKILLS.md#browser--e2e) |

## Critério Editorial

Cada entrada deve ser curta, verificável e útil em projeto real. O catálogo evita descrições longas, links mortos e listas genéricas sem contexto. A regra é simples: se uma skill não ajuda um agente ou uma pessoa a executar melhor uma tarefa recorrente, ela não entra.

Leia os critérios completos em [CURATION.md](CURATION.md).

## Como Contribuir

1. Abra [SKILLS.md](SKILLS.md) e encontre a categoria correta.
2. Adicione uma entrada com nome, link e descrição objetiva.
3. Confirme que o link é público e que a skill tem documentação suficiente.
4. Mantenha a descrição em uma frase curta.

Formato:

```markdown
| modern-python | https://github.com/trailofbits/skills/tree/main/plugins/modern-python | Skill para práticas modernas de Python, typing, estrutura e segurança. |
```

## Roadmap Curto

- Adicionar tags por plataforma: Codex, Claude, Cursor, Gemini CLI e MCP.
- Separar coleções oficiais, comunitárias e especializadas.
- Criar checks automáticos para links, duplicatas e descrições longas.
- Adicionar ranking por utilidade prática e frequência de uso.
