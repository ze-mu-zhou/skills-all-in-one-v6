#!/usr/bin/env python3
"""
Skill Advisor V6 - Provides skill recommendations with flexible adjustment
Outputs reference skill chains and decision guide, Claude selects based on actual situation
"""
import sys

# Reference skill chains (not mandatory)
REFERENCE_CHAINS = {
    "frontend": {
        "keywords": ["frontend", "UI", "interface", "component", "React", "Vue", "CSS", "HTML", "page"],
        "full_chain": ["content-research-writer", "mcp-builder", "frontend-design", "webapp-testing"],
        "minimal": ["frontend-design"],
        "optional": ["theme-factory", "canvas-design", "algorithmic-art"],
    },
    "backend": {
        "keywords": ["backend", "API", "endpoint", "service", "server"],
        "full_chain": ["content-research-writer", "mcp-builder", "postgresql", "python-testing-patterns", "test-driven-development"],
        "minimal": ["python-testing-patterns"],
        "optional": ["rag-implementation", "distributed-tracing"],
    },
    "fullstack": {
        "keywords": ["fullstack", "full-stack", "complete", "system", "application", "project", "website"],
        "full_chain": ["content-research-writer", "mcp-builder", "postgresql", "python-testing-patterns", "frontend-design", "webapp-testing", "github-actions-templates"],
        "minimal": ["mcp-builder", "python-testing-patterns", "frontend-design"],
        "optional": ["prometheus-configuration", "distributed-tracing"],
    },
    "debug": {
        "keywords": ["bug", "debug", "fix", "issue", "error", "problem"],
        "full_chain": ["systematic-debugging", "test-driven-development", "finishing-a-development-branch"],
        "minimal": ["systematic-debugging"],
        "optional": [],
    },
    "ai": {
        "keywords": ["RAG", "LLM", "AI", "vector", "embedding", "intelligent", "chatbot"],
        "full_chain": ["content-research-writer", "mcp-builder", "postgresql", "rag-implementation", "python-testing-patterns"],
        "minimal": ["rag-implementation"],
        "optional": ["distributed-tracing"],
    },
    "devops": {
        "keywords": ["deploy", "deployment", "CI/CD", "devops", "docker", "k8s", "kubernetes"],
        "full_chain": ["terraform-module-library", "github-actions-templates", "prometheus-configuration", "distributed-tracing"],
        "minimal": ["github-actions-templates"],
        "optional": ["helm-chart-scaffolding"],
    },
}

def detect_type(text):
    text_lower = text.lower()
    for task_type, config in REFERENCE_CHAINS.items():
        if any(kw.lower() in text_lower for kw in config["keywords"]):
            return task_type, config
    return "fullstack", REFERENCE_CHAINS["fullstack"]

def print_advice(task_type, config):
    print(f"\n{'='*60}")
    print(f"Task Type: {task_type.upper()}")
    print(f"{'='*60}\n")

    print("Reference Skill Chain (flexible adjustment allowed):\n")
    print("Full Chain:")
    for i, skill in enumerate(config["full_chain"], 1):
        print(f"  {i}. {skill}")

    print(f"\nMinimal Approach (simple tasks):")
    for skill in config["minimal"]:
        print(f"  - {skill}")

    if config["optional"]:
        print(f"\nOptional Extensions:")
        for skill in config["optional"]:
            print(f"  + {skill}")

    print(f"\n{'='*60}")
    print("Decision Guide:")
    print("- Clear requirements -> Can skip content-research-writer")
    print("- Simple feature -> Use minimal approach")
    print("- Complex system -> Use full chain")
    print("- Flexibly select and adjust based on actual situation")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    task_type, config = detect_type(user_input)
    print_advice(task_type, config)
