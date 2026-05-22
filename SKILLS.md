# AI Agent Skills Catalog

A curated catalog of useful skills for Codex, Claude, and AI agents working across software engineering, product, design, architecture, and AI engineering.

Last reviewed: 2026-05-22

## Index

- [Software Engineering](#software-engineering)
- [Python](#python)
- [UX/UI](#uxui)
- [Product](#product)
- [Scrum Master / Agile](#scrum-master--agile)
- [Clean Architecture](#clean-architecture)
- [AI Architecture](#ai-architecture)
- [AI Engineering](#ai-engineering)
- [Security](#security)
- [Browser / E2E](#browser--e2e)
- [Documents / Office](#documents--office)
- [Data / Analytics](#data--analytics)
- [Installation Notes](#installation-notes)

## Software Engineering

| Skill | Link | What it is |
|---|---|---|
| Superpowers | https://github.com/obra/superpowers | Workflow library for planning, testing, reviewing, and finishing agentic development tasks. |
| writing-plans | https://github.com/obra/superpowers/tree/main/skills/writing-plans | Skill for turning specifications into executable plans for agents. |
| executing-plans | https://github.com/obra/superpowers/tree/main/skills/executing-plans | Skill for executing plans task by task with checkpoints and verification. |
| systematic-debugging | https://github.com/obra/superpowers/tree/main/skills/systematic-debugging | Skill for debugging with hypotheses, evidence, and reproduction before fixing. |
| test-driven-development | https://github.com/obra/superpowers/tree/main/skills/test-driven-development | Skill for implementing changes with a red-green-refactor cycle. |
| subagent-driven-development | https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development | Skill for coordinating independent subagents with review checkpoints during larger engineering work. |
| requesting-code-review | https://github.com/obra/superpowers/tree/main/skills/requesting-code-review | Skill for requesting structured review before integrating changes. |
| receiving-code-review | https://github.com/obra/superpowers/tree/main/skills/receiving-code-review | Skill for handling review feedback without applying changes blindly. |
| Addy Osmani Agent Skills | https://github.com/addyosmani/agent-skills | Production-grade engineering skill pack for specification, planning, incremental implementation, testing, review, simplification, and shipping. |
| addy-test-driven-development | https://github.com/addyosmani/agent-skills/tree/main/skills/test-driven-development | Source-qualified TDD skill with red-green-refactor, test pyramid guidance, and behavior-first verification. |
| code-simplification | https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification | Skill for simplifying working code while preserving behavior and reducing unnecessary complexity. |
| incremental-implementation | https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation | Skill for delivering changes in small verified vertical slices instead of large risky rewrites. |
| code-review-and-quality | https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality | Skill for reviewing changes across correctness, readability, architecture, security, and performance. |
| debugging-and-error-recovery | https://github.com/addyosmani/agent-skills/tree/main/skills/debugging-and-error-recovery | Skill for reproducing, localizing, reducing, fixing, and guarding against bugs or failing builds. |
| GStack | https://github.com/garrytan/gstack | Virtual engineering team pack with planning, review, QA, design, security, benchmarking, release, and Codex second-opinion workflows. |
| gstack-review | https://github.com/garrytan/gstack/tree/main/review | GStack command for staff-engineer review of real diffs, production risks, completeness gaps, and test coverage. |
| pr-review-expert | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/pr-review-expert | Skill for systematic pull request review with blast-radius analysis, security scanning, and coverage deltas. |
| gh-address-comments | https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments | Codex skill for resolving actionable comments in GitHub pull requests. |
| gh-fix-ci | https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci | Codex skill for investigating and fixing failing GitHub Actions checks. |
| yeet | https://github.com/openai/skills/tree/main/skills/.curated/yeet | Codex skill for publishing changes with commit, push, and pull request flow. |
| git-commit-pr-message | https://github.com/psenger/ai-agent-skills/tree/main/skills/git-commit-pr-message | Skill for generating commit and pull request messages from the real diff. |
| readme-writer | https://github.com/psenger/ai-agent-skills/tree/main/skills/readme-writer | Skill for creating usage-focused README files with setup and maintenance context. |

## Python

| Skill | Link | What it is |
|---|---|---|
| modern-python | https://github.com/trailofbits/skills/tree/main/plugins/modern-python | Skill for modern Python practices, typing, structure, and security. |
| property-based-testing | https://github.com/trailofbits/skills/tree/main/plugins/property-based-testing | Skill for creating tests based on properties and invariants. |
| mutation-testing | https://github.com/trailofbits/skills/tree/main/plugins/mutation-testing | Skill for evaluating whether tests detect defective code changes. |
| testing-handbook-skills | https://github.com/trailofbits/skills/tree/main/plugins/testing-handbook-skills | Collection of testing practices for Python projects and general systems. |
| static-analysis | https://github.com/trailofbits/skills/tree/main/plugins/static-analysis | Skill for static analysis and code issue investigation. |
| jupyter-notebook | https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook | Codex skill for working with notebooks, cells, and interactive analysis. |
| hatch-pet | https://github.com/openai/skills/tree/main/skills/.curated/hatch-pet | Codex skill for Python projects packaged with Hatch. |
| pyright-lsp plugin | https://claude.com/plugins/pyright-lsp | Claude Code plugin for Pyright-backed Python and TypeScript language-server analysis. |

## UX/UI

| Skill | Link | What it is |
|---|---|---|
| shadcn | https://github.com/shadcn-ui/ui/tree/main/skills/shadcn | Skill for using shadcn/ui components with consistent patterns. |
| frontend-design | https://github.com/anthropics/skills/tree/main/skills/frontend-design | Claude skill for designing front-end interfaces with strong visual focus. |
| frontend-skill | https://officialskills.sh/openai/skills/frontend-skill | OpenAI skill for composition-first frontend implementation that avoids generic AI-generated interfaces. |
| frontend-ui-engineering | https://github.com/addyosmani/agent-skills/tree/main/skills/frontend-ui-engineering | Skill for production UI components, state, responsiveness, accessibility, and integration quality. |
| design-critique | https://github.com/psenger/ai-agent-skills/tree/main/skills/design-critique | Skill for reviewing UI, visual hierarchy, clarity, and design consistency. |
| gstack-design-review | https://github.com/garrytan/gstack/tree/main/design-review | GStack command for live visual audits, source fixes, and before/after screenshot evidence. |
| gstack-plan-design-review | https://github.com/garrytan/gstack/tree/main/plan-design-review | GStack command for reviewing design plans before implementation against hierarchy, interaction, and consistency. |
| figma | https://github.com/openai/skills/tree/main/skills/.curated/figma | Codex skill for general Figma workflows. |
| figma-implement-design | https://github.com/openai/skills/tree/main/skills/.curated/figma-implement-design | Codex skill for turning Figma designs into implementation. |
| figma-create-design-system-rules | https://github.com/openai/skills/tree/main/skills/.curated/figma-create-design-system-rules | Codex skill for generating design system rules from Figma. |
| figma-generate-design | https://github.com/openai/skills/tree/main/skills/.curated/figma-generate-design | Codex skill for generating visual proposals with Figma. |
| canvas-design | https://github.com/anthropics/skills/tree/main/skills/canvas-design | Claude skill for visual compositions in canvas and design artifacts. |
| web-artifacts-builder | https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder | Claude skill for creating interactive web artifacts. |

## Product

| Skill | Link | What it is |
|---|---|---|
| pm-skills | https://github.com/product-on-purpose/pm-skills | Product skill collection for discovery, delivery, measurement, and iteration. |
| deliver-prd | https://github.com/product-on-purpose/pm-skills/tree/main/skills/deliver-prd | Skill for creating structured, actionable PRDs. |
| deliver-user-stories | https://github.com/product-on-purpose/pm-skills/tree/main/skills/deliver-user-stories | Skill for converting needs into clear user stories. |
| deliver-acceptance-criteria | https://github.com/product-on-purpose/pm-skills/tree/main/skills/deliver-acceptance-criteria | Skill for writing testable acceptance criteria. |
| define-problem-statement | https://github.com/product-on-purpose/pm-skills/tree/main/skills/define-problem-statement | Skill for framing a product problem before choosing a solution. |
| define-opportunity-tree | https://github.com/product-on-purpose/pm-skills/tree/main/skills/define-opportunity-tree | Skill for organizing opportunities, solutions, and experiments. |
| measure-experiment-design | https://github.com/product-on-purpose/pm-skills/tree/main/skills/measure-experiment-design | Skill for designing product experiments with metrics. |
| prd-development | https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills/prd-development | Product management skill for developing PRDs and aligning scope. |
| roadmap-planning | https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills/roadmap-planning | Skill for structuring roadmaps with priorities and dependencies. |
| prioritization-advisor | https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills/prioritization-advisor | Skill for supporting product initiative prioritization. |

## Scrum Master / Agile

| Skill | Link | What it is |
|---|---|---|
| workshop-facilitation | https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills/workshop-facilitation | Skill for facilitating workshops, decisions, and team alignment. |
| iterate-retrospective | https://github.com/product-on-purpose/pm-skills/tree/main/skills/iterate-retrospective | Skill for running retrospectives and recording learnings. |
| iterate-refinement-notes | https://github.com/product-on-purpose/pm-skills/tree/main/skills/iterate-refinement-notes | Skill for organizing backlog refinement notes and decisions. |
| tool-foundation-sprint-basics | https://github.com/product-on-purpose/pm-skills/tree/main/skills/tool-foundation-sprint-basics | Skill for structuring sprint basics and delivery cadence. |
| tool-foundation-sprint-brief | https://github.com/product-on-purpose/pm-skills/tree/main/skills/tool-foundation-sprint-brief | Skill for preparing a sprint brief with context and goals. |
| user-story-splitting | https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills/user-story-splitting | Skill for splitting large stories into smaller deliverable slices. |
| user-story-mapping-workshop | https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills/user-story-mapping-workshop | Skill for facilitating story mapping with journeys, backlog, and releases. |
| foundation-meeting-agenda | https://github.com/product-on-purpose/pm-skills/tree/main/skills/foundation-meeting-agenda | Skill for creating focused agendas for ceremonies and meetings. |
| foundation-meeting-recap | https://github.com/product-on-purpose/pm-skills/tree/main/skills/foundation-meeting-recap | Skill for summarizing decisions, actions, and follow-ups after meetings. |

## Clean Architecture

| Skill | Link | What it is |
|---|---|---|
| solid | https://github.com/ramziddin/solid-skills/tree/main/skills/solid | Skill for applying SOLID, TDD, and clean architecture to code. |
| arch-lens | https://github.com/psenger/ai-agent-skills/tree/main/skills/arch-lens | Skill for reviewing architecture, coupling, and modularity. |
| senior-architect | https://github.com/alirezarezvani/claude-skills/tree/main/engineering-team/skills/senior-architect | Skill for architecture decisions, trade-offs, system design, dependency analysis, and ADRs. |
| api-and-interface-design | https://github.com/addyosmani/agent-skills/tree/main/skills/api-and-interface-design | Skill for contract-first APIs, module boundaries, versioning, payload design, and interface ergonomics. |
| review-api-design | https://github.com/psenger/ai-agent-skills/tree/main/skills/review-api-design | Skill for reviewing API contracts, ergonomics, and consistency. |
| api-design-reviewer | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/api-design-reviewer | Skill for reviewing REST APIs, conventions, versioning, breaking changes, and design scorecards. |
| migration-architect | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/migration-architect | Skill for zero-downtime migrations, compatibility validation, rollback planning, and stakeholder coordination. |
| deprecation-and-migration | https://github.com/addyosmani/agent-skills/tree/main/skills/deprecation-and-migration | Skill for safely sunsetting old systems, migrating users, preserving compatibility, and planning rollback. |
| observability-designer | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/observability-designer | Skill for production metrics, logs, traces, SLOs, alerting, dashboards, and diagnosis strategy. |
| spec-to-code-compliance | https://github.com/trailofbits/skills/tree/main/plugins/spec-to-code-compliance | Skill for checking whether implementation follows the specification. |
| entry-point-analyzer | https://github.com/trailofbits/skills/tree/main/plugins/entry-point-analyzer | Skill for mapping entrypoints and critical system surfaces. |
| differential-review | https://github.com/trailofbits/skills/tree/main/plugins/differential-review | Skill for differential review focused on introduced changes and risks. |
| handoff | https://github.com/psenger/ai-agent-skills/tree/main/skills/handoff | Skill for creating clear technical handoffs between agents or people. |

## AI Architecture

| Skill | Link | What it is |
|---|---|---|
| claude-api | https://github.com/anthropics/skills/tree/main/skills/claude-api | Claude skill for working with the Anthropic API and integrations. |
| mcp-builder | https://github.com/anthropics/skills/tree/main/skills/mcp-builder | Claude skill for building MCP servers and exposing tools to agents. |
| openai-docs | https://github.com/openai/skills/tree/main/skills/.system/openai-docs | Codex skill for consulting official OpenAI documentation. |
| chatgpt-apps | https://github.com/openai/skills/tree/main/skills/.curated/chatgpt-apps | Codex skill for creating apps and integrations for ChatGPT. |
| cli-creator | https://github.com/openai/skills/tree/main/skills/.curated/cli-creator | Codex skill for creating reusable CLIs for technical workflows. |
| agentic-skeleton-dir-structure | https://github.com/psenger/ai-agent-skills/tree/main/skills/agentic-skeleton-dir-structure | Skill for structuring agentic projects with directories and responsibilities. |
| create-a-skill | https://github.com/psenger/ai-agent-skills/tree/main/skills/create-a-skill | Skill for creating new skills that follow the Agent Skills standard. |
| skill-creator | https://github.com/anthropics/skills/tree/main/skills/skill-creator | Claude skill for creating and improving reusable skills. |
| workflow-skill-design | https://github.com/trailofbits/skills/tree/main/plugins/workflow-skill-design | Skill for designing workflow skills with clear scope and triggers. |
| Vercel Agent Skills | https://github.com/vercel-labs/agent-skills | Vercel's official collection for agents, web apps, and modern workflows. |
| Awesome Agent Skills | https://github.com/VoltAgent/awesome-agent-skills | Broad directory of skills for Claude Code, Codex, Gemini CLI, and Cursor. |
| Composio Awesome Claude Skills | https://github.com/ComposioHQ/awesome-claude-skills | Discovery index for Claude skills, tools, and workflow resources that should be verified at their original source. |
| alirezarezvani/claude-skills | https://github.com/alirezarezvani/claude-skills | Large multi-tool skill library for Codex, Claude Code, Gemini CLI, Cursor, engineering, product, compliance, and operations. |
| antfu skills | https://github.com/antfu/skills | Personal curated collection of reusable agentic skills. |
| context-engineering | https://github.com/addyosmani/agent-skills/tree/main/skills/context-engineering | Skill for curating rules files, session context, and project knowledge so agents use the right information. |
| source-driven-development | https://github.com/addyosmani/agent-skills/tree/main/skills/source-driven-development | Skill for grounding framework and library decisions in current official documentation. |
| doubt-driven-development | https://github.com/addyosmani/agent-skills/tree/main/skills/doubt-driven-development | Skill for adversarially reviewing non-trivial decisions before confident but unverified assumptions stand. |
| planning-and-task-breakdown | https://github.com/addyosmani/agent-skills/tree/main/skills/planning-and-task-breakdown | Skill for decomposing large requests into ordered, verifiable implementation tasks. |
| gstack-plan-eng-review | https://github.com/garrytan/gstack/tree/main/plan-eng-review | GStack command for engineering-plan review covering data flow, failure modes, security concerns, and tests. |
| gstack-codex | https://github.com/garrytan/gstack/tree/main/codex | GStack command for cross-model second opinion and Codex review of plans or implementations. |

## AI Engineering

| Skill | Link | What it is |
|---|---|---|
| AI Engineering Toolkit | https://github.com/sickn33/antigravity-awesome-skills/tree/main/plugins/antigravity-awesome-skills-claude/skills/ai-engineering-toolkit | Collection for prompt evals, RAG, agent security, and context management. |
| Agent Verifier | https://github.com/aurite-ai/agent-verifier | Collection for verifying quality, security, language, and agent patterns. |
| verification | https://github.com/aurite-ai/agent-verifier/tree/main/skills/verification | Skill for auditing agent outputs before accepting results. |
| verify-quality | https://github.com/aurite-ai/agent-verifier/tree/main/skills/verify-quality | Skill for reviewing the quality of agent-produced deliverables. |
| verify-security | https://github.com/aurite-ai/agent-verifier/tree/main/skills/verify-security | Skill for checking security risks in agent responses and changes. |
| ai-engineer-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/ai-engineer-skill | Skill for applied AI engineering across systems and integrations. |
| llm-architect-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/llm-architect-skill | Skill for designing LLM, agent, and pipeline architecture. |
| mlops-engineer-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/mlops-engineer-skill | Skill for operationalizing models, pipelines, and ML monitoring. |

## Security

| Skill | Link | What it is |
|---|---|---|
| Trail of Bits Skills | https://github.com/trailofbits/skills | Skill collection for security research, audits, and review workflows. |
| security-best-practices | https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices | Codex skill for applying security best practices in projects. |
| security-threat-model | https://github.com/openai/skills/tree/main/skills/.curated/security-threat-model | Codex skill for creating threat models and mapping risks. |
| security-ownership-map | https://github.com/openai/skills/tree/main/skills/.curated/security-ownership-map | Codex skill for mapping owners of risks and security surfaces. |
| skill-security-auditor | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/skill-security-auditor | Skill for auditing third-party skills before installation for command injection, exfiltration, prompt injection, and supply-chain risk. |
| supply-chain-risk-auditor | https://github.com/trailofbits/skills/tree/main/plugins/supply-chain-risk-auditor | Skill for auditing dependency and supply chain risks. |
| semgrep-rule-creator | https://github.com/trailofbits/skills/tree/main/plugins/semgrep-rule-creator | Skill for creating Semgrep rules that detect unsafe patterns. |
| insecure-defaults | https://github.com/trailofbits/skills/tree/main/plugins/insecure-defaults | Skill for identifying dangerous defaults in configuration and code. |
| c-review | https://github.com/trailofbits/skills/tree/main/plugins/c-review | Skill for security and correctness review in C code. |
| variant-analysis | https://github.com/trailofbits/skills/tree/main/plugins/variant-analysis | Skill for searching variants of a known vulnerability. |

## Browser / E2E

| Skill | Link | What it is |
|---|---|---|
| playwright | https://github.com/openai/skills/tree/main/skills/.curated/playwright | Codex skill for browser automation and end-to-end testing. |
| playwright-interactive | https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive | Codex skill for assisted browser interaction and page exploration. |
| playwright-skill | https://github.com/lackeyjb/playwright-skill/tree/main/skills/playwright-skill | Claude skill for writing and running Playwright automations. |
| webapp-testing | https://github.com/anthropics/skills/tree/main/skills/webapp-testing | Claude skill for testing web applications through browser flows. |
| screenshot | https://github.com/openai/skills/tree/main/skills/.curated/screenshot | Codex skill for capturing and analyzing interface screenshots. |
| browser-testing-with-devtools | https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools | Skill for inspecting live browser runtime state through Chrome DevTools, DOM, console, network, and performance data. |
| browserbase-ui-test | https://officialskills.sh/browserbase/skills/ui-test | Browserbase skill for browser UI testing workflows with hosted browser automation. |

## Documents / Office

| Skill | Link | What it is |
|---|---|---|
| pdf OpenAI | https://github.com/openai/skills/tree/main/skills/.curated/pdf | Codex skill for reading, extracting, and working with PDFs. |
| pdf Anthropic | https://github.com/anthropics/skills/tree/main/skills/pdf | Claude skill for PDF processing and editing. |
| docx | https://github.com/anthropics/skills/tree/main/skills/docx | Claude skill for creating and editing Word documents. |
| xlsx | https://github.com/anthropics/skills/tree/main/skills/xlsx | Claude skill for working with Excel spreadsheets. |
| pptx | https://github.com/anthropics/skills/tree/main/skills/pptx | Claude skill for creating and editing PowerPoint presentations. |
| doc-coauthoring | https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring | Claude skill for structured document coauthoring and review. |
| notion-knowledge-capture | https://github.com/openai/skills/tree/main/skills/.curated/notion-knowledge-capture | Codex skill for capturing knowledge in Notion. |
| notion-research-documentation | https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation | Codex skill for organizing research and documentation in Notion. |
| notion-spec-to-implementation | https://github.com/openai/skills/tree/main/skills/.curated/notion-spec-to-implementation | Codex skill for converting Notion specifications into implementation. |

## Data / Analytics

| Skill | Link | What it is |
|---|---|---|
| csv-data-summarizer | https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill | Claude skill for summarizing CSVs, detecting missing data, and generating visualizations. |
| data-analyst-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/data-analyst-skill | Skill for data analysis, SQL, BI, and actionable reporting. |
| csv-data-wrangler-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/csv-data-wrangler-skill | Skill for cleaning, transforming, and preparing tabular CSV data. |
| data-scientist-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/data-scientist-skill | Skill for statistical analysis, modeling, and data experimentation. |
| database-optimizer-skill | https://github.com/belokonm/claude-supercode-skills/tree/main/database-optimizer-skill | Skill for reviewing queries, indexes, and database performance. |
| measure-dashboard-requirements | https://github.com/product-on-purpose/pm-skills/tree/main/skills/measure-dashboard-requirements | Skill for specifying dashboards, metrics, and analytics needs. |
| measure-instrumentation-spec | https://github.com/product-on-purpose/pm-skills/tree/main/skills/measure-instrumentation-spec | Skill for defining events, properties, and product instrumentation. |
| measure-experiment-results | https://github.com/product-on-purpose/pm-skills/tree/main/skills/measure-experiment-results | Skill for interpreting product experiment results. |
| measure-okr-grader | https://github.com/product-on-purpose/pm-skills/tree/main/skills/measure-okr-grader | Skill for evaluating OKRs and metric quality. |
| foundation-okr-writer | https://github.com/product-on-purpose/pm-skills/tree/main/skills/foundation-okr-writer | Skill for writing OKRs connected to measurable outcomes. |
| vault-scribe | https://github.com/psenger/ai-agent-skills/tree/main/skills/vault-scribe | Skill for recording structured knowledge in Markdown vaults. |

## Installation Notes

Install only the skills needed for the active project. The catalog intentionally keeps broad indexes separate from original skill sources.

- Addy Osmani pack: `npx skills add addyosmani/agent-skills`
- Addy Osmani focused skills: `npx skills add addyosmani/agent-skills --skill <skill-name>`
- Addy Osmani code-simplify command: install the Addy pack, then use `/code-simplify`.
- Superpowers focused skills: `npx skills add obra/superpowers --skill <skill-name>`
- OpenAI focused skills: `npx skills add openai/skills --skill <skill-name>`
- GStack for Claude Code: `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`
- GStack for Codex: clone GStack and run `./setup --host codex`.
- alirezarezvani/claude-skills for Codex: `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex`
- alirezarezvani/claude-skills for Claude Code: `/plugin marketplace add alirezarezvani/claude-skills`
- OpenAI frontend skill: `npx skills add https://github.com/openai/skills --skill frontend-skill`
- Browserbase UI test skill: `npx skills add https://github.com/browserbase/skills --skill ui-test`
- pyright-lsp plugin for Claude Code: `/plugin install pyright-lsp@claude-plugins-official`
