# Synapse System

[![Synapse Protocol](https://img.shields.io/badge/Protocol-Synapse-blueviolet)](GEMINI.md)
[![Dependency: planning-with-files](https://img.shields.io/badge/Dependency-planning--with--files-blue)](https://github.com/OthmanAdi/planning-with-files)

Synapse is a dual-layered cognitive architecture for AI-native software engineering. It implements a decentralized knowledge-sharing ecosystem designed for multi-user collaboration and persistent agent memory.

## 🧠 Architecture

Synapse splits AI cognition into two distinct layers to maximize efficiency and project continuity:

### 1. Cortex (Global Intelligence)
Located in `.gemini/cortex/`.
- **Permanent Wisdom**: Stores engineering standards, technical findings, and architectural decisions.
- **Shared Memory**: Versioned with the repository to ensure all contributors (human and AI) align with the project's "Source of Truth."

### 2. Neuron (Working Memory)
Located in `.gemini/neurons/{user}/{task_id}/`.
- **Private Execution**: Local, task-specific workspaces for active development.
- **Ephemeral State**: Isolated to prevent cross-task pollution and protect user privacy.
- **Distillation**: Task-specific insights are refined in `knowledge.md` before being promoted to the Cortex.

## 🛠 Required Skills

Synapse relies on specialized agent skills for structured execution.

- **[planning-with-files](https://github.com/OthmanAdi/planning-with-files)**: Implements "Manus-style" file-based planning. This is a **core dependency** for maintaining state across complex multi-step tasks.

## 🚀 Getting Started

### Prerequisites
- [Gemini CLI](https://github.com/google/gemini-cli)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/synapse.git
   cd synapse
   ```

2. **Install core skills:**
   ```bash
   gemini skills install https://github.com/OthmanAdi/planning-with-files --path .gemini/skills/planning-with-files
   ```

3. **Initialize your Session:**
   When starting a session, provide your alias (lowercase, no special characters) to initialize your private neuron space.

## 📜 The Synapse Protocol

The project is governed by the [Synapse Manifesto](.gemini/cortex/manifesto.md). Every task follows a structured 4-file pattern managed by the `planning-with-files` skill:
- `task_plan.md`: Strategy & Roadmap
- `progress.md`: Execution Log
- `findings.md`: Research & Insights
- `knowledge.md`: Distilled Manual (Synapse Mandate)

## 🤝 Contributing

Contributions are distilled from Neurons to the Cortex. Please ensure all significant technical findings are promoted to the `atlas.md` within the Cortex.

---
*Built for the next generation of AI-native development.*
