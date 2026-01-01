# Skills All-in-One v6

A comprehensive meta-skill that coordinates 30 development skills for Claude Code.

## Overview

This meta-skill provides intelligent coordination across 6 major development categories:

- **Frontend Development**: UI/UX design, web applications, algorithmic art
- **Backend Development**: APIs, databases, Python/TypeScript development
- **DevOps & Infrastructure**: Kubernetes, Terraform, CI/CD, monitoring
- **Testing & Quality**: TDD, webapp testing, systematic debugging
- **Documentation & Research**: Content writing, meeting insights, lead research
- **Specialized Tools**: PDF manipulation, MCP builders, Git workflows

## Features

- **Automated Installation**: One-command setup for all 30 skills
- **Intelligent Recommendations**: Context-aware skill chain suggestions
- **Flexible Selection**: Adapt skill chains based on project needs
- **Status Monitoring**: Real-time tracking of installed skills
- **Windows Compatible**: ASCII-safe encoding for cross-platform support

## Installation

1. Copy the `skills-all-in-one-v6` folder to your Claude skills directory:
   ```
   C:\Users\{username}\.claude\skills\
   ```

2. Run the skill manager to install all skills:
   ```bash
   python scripts/skill_manager.py
   ```

3. Check installation status:
   ```bash
   python scripts/skill_manager.py --check
   ```

## Usage

### In Claude Code

Simply invoke the skill when starting a new project:
```
/skills-all-in-one-v6
```

The skill will:
1. Analyze your project requirements
2. Recommend appropriate skill chains
3. Execute necessary skills automatically

### Skill Advisor

Get recommendations for specific task types:
```bash
python scripts/skill_advisor.py "your task description"
```

Example:
```bash
python scripts/skill_advisor.py "build a React dashboard"
```

## Skill Categories

### Frontend Development (6 skills)
- frontend-design
- canvas-design
- algorithmic-art
- theme-factory
- webapp-testing
- finishing-a-development-branch

### Backend Development (7 skills)
- python-development
- javascript-typescript
- typescript-advanced-types
- database-design
- postgresql
- llm-application-dev
- rag-implementation

### DevOps & Infrastructure (8 skills)
- kubernetes-operations
- helm-chart-scaffolding
- terraform-module-library
- cloud-infrastructure
- cicd-automation
- github-actions-templates
- distributed-tracing
- prometheus-configuration

### Testing & Quality (4 skills)
- test-driven-development
- python-testing-patterns
- systematic-debugging
- security-compliance

### Documentation & Research (3 skills)
- content-research-writer
- meeting-insights-analyzer
- lead-research-assistant

### Specialized Tools (5 skills)
- mcp-builder
- pdf-skills
- document-skills
- using-git-worktrees
- subagent-driven-development

## Reference Skill Chains

### Frontend Development
**Full Chain**: content-research-writer → mcp-builder → frontend-design → webapp-testing
**Minimal**: frontend-design

### Backend Development
**Full Chain**: content-research-writer → database-design → python-development → test-driven-development
**Minimal**: python-development

### DevOps & Infrastructure
**Full Chain**: content-research-writer → cloud-infrastructure → kubernetes-operations → prometheus-configuration
**Minimal**: kubernetes-operations

## Decision Guide

- **Clear requirements** → Skip content-research-writer
- **Simple feature** → Use minimal approach
- **Complex system** → Use full chain
- **Flexibly select and adjust** based on actual situation

## Requirements

- Python 3.6+
- Git
- Claude Code environment
- Access to skill repositories:
  - anthropics/skills
  - ComposioHQ/awesome-claude-skills
  - wshobson/agents
  - obra/superpowers

## License

MIT License - See individual skill repositories for their respective licenses.

## Contributing

This is a meta-skill that coordinates existing skills. To contribute:
1. Improve skill chain recommendations
2. Add new skill integrations
3. Enhance the advisor algorithm
4. Report issues or suggest improvements

## Credits

Created with Claude Code and coordinating skills from:
- Anthropic
- ComposioHQ
- wshobson
- obra

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
