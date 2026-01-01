#!/usr/bin/env python3
"""Skill Manager V6"""
import subprocess, json, shutil
from pathlib import Path

SKILLS = {
    "frontend-design": ("anthropics/skills", "skills/frontend-design"),
    "artifacts-builder": ("anthropics/skills", "skills/artifacts-builder"),
    "canvas-design": ("anthropics/skills", "skills/canvas-design"),
    "webapp-testing": ("anthropics/skills", "skills/webapp-testing"),
    "algorithmic-art": ("anthropics/skills", "skills/algorithmic-art"),
    "slack-gif-creator": ("anthropics/skills", "skills/slack-gif-creator"),
    "theme-factory": ("ComposioHQ/awesome-claude-skills", "theme-factory"),
    "image-enhancer": ("ComposioHQ/awesome-claude-skills", "image-enhancer"),
    "video-downloader": ("ComposioHQ/awesome-claude-skills", "video-downloader"),
    "content-research-writer": ("ComposioHQ/awesome-claude-skills", "content-research-writer"),
    "test-driven-development": ("obra/superpowers", "skills/test-driven-development"),
    "systematic-debugging": ("obra/superpowers", "skills/systematic-debugging"),
    "subagent-driven-development": ("obra/superpowers", "skills/subagent-driven-development"),
    "using-git-worktrees": ("obra/superpowers", "skills/using-git-worktrees"),
    "finishing-a-development-branch": ("obra/superpowers", "skills/finishing-a-development-branch"),
    "mcp-builder": ("anthropics/skills", "skills/mcp-builder"),
    "developer-growth-analysis": ("ComposioHQ/awesome-claude-skills", "developer-growth-analysis"),
    "pdf-skills": ("ComposioHQ/awesome-claude-skills", "document-skills/pdf"),
    "meeting-insights-analyzer": ("ComposioHQ/awesome-claude-skills", "meeting-insights-analyzer"),
    "lead-research-assistant": ("ComposioHQ/awesome-claude-skills", "lead-research-assistant"),
    "terraform-module-library": ("wshobson/agents", "plugins/cloud-infrastructure/skills/terraform-module-library"),
    "github-actions-templates": ("wshobson/agents", "plugins/cicd-automation/skills/github-actions-templates"),
    "solidity-security": ("wshobson/agents", "plugins/blockchain-web3/skills/solidity-security"),
    "helm-chart-scaffolding": ("wshobson/agents", "plugins/kubernetes-operations/skills/helm-chart-scaffolding"),
    "python-testing-patterns": ("wshobson/agents", "plugins/python-development/skills/python-testing-patterns"),
    "typescript-advanced-types": ("wshobson/agents", "plugins/javascript-typescript/skills/typescript-advanced-types"),
    "rag-implementation": ("wshobson/agents", "plugins/llm-application-dev/skills/rag-implementation"),
    "prometheus-configuration": ("wshobson/agents", "plugins/observability-monitoring/skills/prometheus-configuration"),
    "postgresql": ("wshobson/agents", "plugins/database-design/skills/postgresql"),
    "distributed-tracing": ("wshobson/agents", "plugins/observability-monitoring/skills/distributed-tracing"),
}

DIR = Path.home() / ".claude" / "skills"

def check(n): return (DIR/n).exists() and (DIR/n/"SKILL.md").exists()

def status():
    ok = [n for n in SKILLS if check(n)]
    miss = [n for n in SKILLS if not check(n)]
    print(f"=== Skills V6: {len(ok)}/30 ===")
    if miss: print(f"Missing: {', '.join(miss[:3])}...")
    else: print("[OK] All installed")
    return {"installed": ok, "missing": miss}

def install(name=None):
    targets = [name] if name else status()["missing"]
    for n in targets:
        if n not in SKILLS: continue
        repo, path = SKILLS[n]
        tmp = DIR / f"_temp_{repo.replace('/','_')}"
        if not tmp.exists():
            subprocess.run(["git","clone",f"https://github.com/{repo}.git",str(tmp)],capture_output=True)
        src, tgt = tmp/path, DIR/n
        if src.exists():
            if tgt.exists(): shutil.rmtree(tgt)
            shutil.copytree(src, tgt)
            print(f"[OK] {n}")

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv)>1 else "status"
    if cmd == "status": status()
    elif cmd == "install": install(sys.argv[2] if len(sys.argv)>2 else None)
