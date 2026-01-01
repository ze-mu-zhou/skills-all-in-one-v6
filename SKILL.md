---
name: skills-all-in-one-v6
description: Full-stack development skill coordinator (30 skills). Triggers on any development task. [MANDATORY] 1.Run skill_manager.py status to check skills 2.Run skill_advisor.py to get recommendations 3.Select and invoke all necessary skills based on actual needs. Skill chains are reference only, flexible adjustment allowed, but must invoke all skills deemed necessary.
---

# Skills All-in-One V6 - Intelligent Skill Coordinator

## Mandatory Requirements (Must Execute)

### 1. Check Skill Status
```bash
python ~/.claude/skills/skills-all-in-one-v6/scripts/skill_manager.py status
```

### 2. Get Skill Recommendations
```bash
python ~/.claude/skills/skills-all-in-one-v6/scripts/skill_advisor.py "user's complete input"
```

### 3. Flexibly Invoke Skills
Based on skill_advisor recommendations and actual project needs, **autonomously select and invoke all necessary skills**.

**Flexibility Principles:**
- Skill chains are reference only, adjust based on actual situation
- Can select only partial skills (e.g., skip requirement confirmation for simple tasks)
- Can choose other more suitable skills
- Can adjust skill order
- **But must invoke all skills you deem necessary, cannot omit any**

## Reference Skill Chains

### Frontend Development Reference Chain
```
content-research-writer → mcp-builder → frontend-design → webapp-testing
```
**Use Case:** Complete frontend feature development
**Can Simplify To:** frontend-design (simple component)
**Can Extend To:** + theme-factory (needs theme) + canvas-design (needs drawing)

### Backend Development Reference Chain
```
content-research-writer → mcp-builder → postgresql → python-testing-patterns → test-driven-development
```
**Use Case:** Complete backend API development
**Can Simplify To:** python-testing-patterns (simple feature)
**Can Extend To:** + rag-implementation (AI feature)

### Debug/Fix Reference Chain
```
systematic-debugging → test-driven-development → finishing-a-development-branch
```
**Use Case:** Bug fixing
**Can Simplify To:** systematic-debugging (quick locate)

### AI/RAG Reference Chain
```
content-research-writer → mcp-builder → postgresql → rag-implementation → python-testing-patterns
```

### DevOps Reference Chain
```
terraform-module-library → github-actions-templates → prometheus-configuration → distributed-tracing
```

### Blockchain Reference Chain
```
content-research-writer → solidity-security → test-driven-development
```

## Skill Selection Guide

### When to Use Requirement Confirmation (content-research-writer)
- ✅ Requirements unclear or complex
- ✅ Involves multiple functional modules
- ❌ Requirements already clear
- ❌ Simple code modification

### When to Use Architecture Design (mcp-builder)
- ✅ New API or system
- ✅ Involves frontend-backend interaction
- ❌ Pure frontend UI adjustment
- ❌ Simple utility function

### When to Use Database Design (postgresql)
- ✅ Involves data persistence
- ✅ Complex data relationships
- ❌ Pure frontend display
- ❌ Stateless service

### When to Use Testing (test-driven-development/webapp-testing)
- ✅ Core business logic
- ✅ Complex interaction flow
- ❌ Simple style adjustment
- ❌ Prototype validation

## 30 Available Skills

**Frontend(10):** frontend-design, artifacts-builder, canvas-design, webapp-testing, algorithmic-art, slack-gif-creator, theme-factory, image-enhancer, video-downloader, content-research-writer

**Backend(20):** test-driven-development, systematic-debugging, subagent-driven-development, using-git-worktrees, finishing-a-development-branch, mcp-builder, developer-growth-analysis, pdf-skills, meeting-insights-analyzer, lead-research-assistant, terraform-module-library, github-actions-templates, solidity-security, helm-chart-scaffolding, python-testing-patterns, typescript-advanced-types, rag-implementation, prometheus-configuration, postgresql, distributed-tracing

## Decision Examples

**User:** "Help me write a simple React button component"
**Analysis:** Clear requirement, no backend needed, simple component
**Selection:** frontend-design (1 skill only)

**User:** "Help me implement a user login system"
**Analysis:** Involves frontend-backend, database, security
**Selection:** mcp-builder → postgresql → python-testing-patterns → frontend-design → webapp-testing (5 skills)

**User:** "How to fix this bug"
**Analysis:** Debugging issue
**Selection:** systematic-debugging (1 skill)

**User:** "Help me build a RAG chatbot"
**Analysis:** AI application, involves architecture, database, RAG
**Selection:** content-research-writer → mcp-builder → postgresql → rag-implementation → python-testing-patterns (5 skills)
