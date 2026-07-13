---
title: "AutoResearch: Autonomous ML Research Framework"
collection: portfolio
date: 2026-05-01
excerpt: "Autonomous machine learning research framework for AI agents"
url: "https://github.com/ajeetkbhardwaj/automlresearch"
category: "AI Systems"
---

## 🔬 AutoResearch Overview
**AutoResearch** is an agents and device-agnostic autonomous machine learning research framework that enables AI agents to independently conduct end-to-end experiments. Unlike traditional AutoML tools, AutoResearch provides a complete research loop where agents can modify code, run experiments, evaluate results, and learn from a persistent semantic memory.

## 🌟 Key Features
* **🤖 Advanced Agent Integration:** Built-in protocols for advanced agentic systems like Claude Code, OpenCode, and OpenClaw.
* **🧠 Semantic Research Memory:** Long-term RAG-based memory using ChromaDB allows agents to learn from every past experiment.
* **📈 Industrial Observability:** Native integration with Weights & Biases (W&B) for real-time metric tracking and artifact management.
* **⚡ High-Performance Backends:** Native support for Apple MLX, JAX, and PyTorch (CUDA/MPS/CPU).
* **🚀 Distributed Scaling:** Parallelize research across clusters using Ray.
* **🛡️ Robust Orchestration:** SQL-backed metadata management and automatic Git-based experiment versioning.

## 🏗️ Architecture
AutoResearch acts as the **Research Platform (The Orchestrator)** while the AI system acts as the **Brain (The Agent)**.

## 🚀 Quick Start
Clone and navigate to the directory then:

**1. Install**
```bash
pip install .
```

**2. Initialize a Project**
```bash
autoresearch init my_research --name "Optimizing-Transformer"
cd my_research
```

**3. Run with an External Agent (e.g., Claude Code)**
Configure your `autoresearch.yaml`:
```yaml
agent:
  type: "external"
  command: "claude-code"
```
Then start the autonomous loop:
```bash
autoresearch run
```

## 🛰️ Autopilot Mode (Pro)
For high-throughput research, AutoResearch supports a fully autonomous "Autopilot" mode. This allows the framework to automatically drive interactive CLI agents like OpenCode or Claude Code by feeding them prompts and auto-exiting sessions once the code is optimized.

## 📊 Comparison: AutoResearch vs. Traditional AutoML

| Feature | Traditional AutoML | AutoResearch |
| :--- | :--- | :--- |
| **Scope** | Hyperparameter tuning only | Full code & architecture modification |
| **Agent Control** | Fixed search space | AI decides what to change |
| **Learning** | Grid/Bayesian search | Semantic memory (RAG) of past results |
| **Device Support** | Varies by tool | Native MLX, JAX, CUDA, MPS |
| **Integration** | Limited to configs | Direct integration with Claude Code/GPT |

---

<!-- AUTO-TEAM-START -->
## 👥 Team Roster for `ajeetkbhardwaj/automlresearch`

* **👑 Team Leader:**
  * <img src='https://avatars.githubusercontent.com/ajeetkbhardwaj?v=4&s=50' width='25' style='border-radius:50%; vertical-align:middle'/> **ajeetkbhardwaj** (Active Commits)
* **👨‍💻 Team Members:**
  * <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png?s=50' width='25' style='border-radius:50%; vertical-align:middle'/> **Open-Source Contributors** (Active Commits)
<!-- AUTO-TEAM-END -->

---
## 📅 Weekly Plan & Updates

### 👑 Team Leader Update (Ajeet Kumar)
* **Solved:** Configured `autopilot: true` in the `autoresearch.yaml` file so the framework can automatically drive the agents unattended.
* **Completed:** Implemented the long-term semantic memory (RAG) using ChromaDB, allowing the agents to reference previous runs.
* **Next Steps:** Optimize the SQL-backed metadata management for faster Git-based experiment versioning.

### 👨‍💻 Team Member Updates
* **Solved:** Fixed the Weights & Biases (W&B) integration for real-time metric tracking.
* **Working on:** Parallelizing the research environments across clusters using Ray.