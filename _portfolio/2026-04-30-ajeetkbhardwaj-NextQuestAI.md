---
title: "NextQuestAI: Deep Research Multi-Agent System"
excerpt: "NextQuestAI is a high-performance, multi-agent research orchestrator powered by LangGraph and NVIDIA NIM.<br/><img src='/images/portfolio/NextQuest.png' alt='NextQuestAI Architecture'/>"
collection: portfolio
date: 2026-04-30
url: "https://github.com/ajeetkbhardwaj/NextQuestAI"
category: "AI Systems"
---

## 🚀 NextQuestAI Overview
**NextQuestAI** is a high-performance, multi-agent research orchestrator powered by **LangGraph** and **NVIDIA NIM**. It transforms simple queries into comprehensive, verified research reports by coordinating specialized agents for planning, searching, scraping, and fact-verification.

## 🌟 Key Features
* **🚦 Intelligent Routing:** Automatically determines if a query needs live web research or can be answered directly.
* **📊 Semantic Fact Ranking:** Filters through massive amounts of scraped data to extract only the highest-quality, most relevant facts.
* **🛡️ Agentic Self-Correction (Fact Verification):** A dedicated Verifier agent cross-checks every claim against source data to eliminate hallucinations.
* **🔋 Multi-Provider Support:** Optimized for **NVIDIA NIM** (low-latency enterprise AI inference), with fallbacks for HuggingFace, OpenRouter, and Gemini.
* **💾 Persistent Research History:** Powered by a local SQLite database, allowing you to resume research sessions at any time.

## 🏗️ Architecture & The Research Pipeline
The system utilizes a swarm of 8+ specialized AI agents working in harmony:
1. **Router:** Determines the path (Direct Answer vs. Deep Research).
2. **Planner:** Decomposes the query into a structured research plan.
3. **Search & Scrape:** Executes parallel web searches (via Tavily) and content extraction.
4. **Analyzer & Ranker:** Filters facts by relevance using semantic similarity.
5. **Synthesizer:** Assembles the final report with full source attribution and citations.
6. **Verifier:** Fact-checks and validates the synthesized claims.

## 🛠️ Tech Stack
| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Orchestration** | `LangGraph 0.2+` | State-machine based multi-agent flow |
| **Inference** | `NVIDIA NIM` | High-performance LLM execution |
| **UI Framework** | `Streamlit 1.32+` | Interactive research dashboard |
| **Web Search** | `Tavily API` | AI-optimized search results |
| **Database** | `SQLite` | Persistent research history |
| **Deployment** | `HF Spaces` | Cloud-native hosting |

## 🚀 Setup & Deployment
NextQuestAI supports **Bring Your Own Key (BYOK)** and is optimized for deployment on Hugging Face Spaces using the Streamlit or Docker SDK.

### Local Installation
**1. Clone the repository:**
```bash
git clone https://github.com/ajeetkbhardwaj/NextQuestAI.git
cd NextQuestAI
```

**2. Install dependencies and configure environment:**
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your NVIDIA_API_KEY
```

**3. Run the Application:**
```bash
streamlit run app.py
```

---

<!-- AUTO-TEAM-START -->
## 👥 Team Roster for `ajeetkbhardwaj/NextQuestAI`

* **👑 Team Leader:**
  * <img src='https://avatars.githubusercontent.com/ajeetkbhardwaj?v=4&s=50' width='25' style='border-radius:50%; vertical-align:middle'/> **ajeetkbhardwaj** (Active Commits)
* **👨‍💻 Team Members:**
  * <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png?s=50' width='25' style='border-radius:50%; vertical-align:middle'/> **Open-Source Contributors** (Active Commits)
<!-- AUTO-TEAM-END -->

---
## 📅 Weekly Plan & Updates
*Write your weekly plan, problems tackled, and achievements here. The automated script will never overwrite this text!*

### 👑 Team Leader Update (Ajeet Kumar)
* **Solved:** [What did you solve?]
* **Working on:** [What are you currently working on?]
* **Next Steps:** [What is next?]

### 👨‍💻 Team Member Updates
* **Solved:** [What did the team solve?]
* **Working on:** [What is the team currently working on?]