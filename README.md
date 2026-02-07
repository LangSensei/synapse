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

### 2. Neuron (Execution History)
Located in `.gemini/neurons/{user}/spikes/{spike_id}/`.
- **Spike Workspace**: Spike-specific workspaces for active development.
- **Learning History**: These directories are committed to the repository to provide a transparent log of how decisions were made and spikes executed.
- **Distillation**: Spike-specific insights are refined in `knowledge.md` before being promoted to the Cortex.

## 🛠 Required Skills

Synapse relies on specialized agent skills for structured execution.

- **[planning-with-files](https://github.com/OthmanAdi/planning-with-files)**: Implements "Manus-style" file-based planning. This is a **core dependency** for maintaining state across complex multi-step spikes.

## 🚀 Getting Started

### Prerequisites
- [Gemini CLI](https://github.com/google/gemini-cli)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LangSensei/synapse.git
   cd synapse
   ```

2. **Install core skills:**
   ```bash
   gemini skills install https://github.com/OthmanAdi/planning-with-files --path .gemini/skills/planning-with-files
   ```

3. **Initialize your Session:**
   When starting a session, provide your alias (lowercase, no special characters) to initialize your private neuron space.

## 📜 The Synapse Protocol

The project is governed by the [Synapse Manifesto](.gemini/cortex/manifesto.md). Every spike follows a structured 4-file pattern managed by the `planning-with-files` and `knowledge-with-files` skills:
- `spike_plan.md`: Strategy & Roadmap
- `progress.md`: Execution Log
- `findings.md`: Research & Insights
- `knowledge.md`: Distilled Manual (Synapse Mandate)

## 🤝 Contributing

Contributions are distilled from Neurons to the Cortex. Please ensure all significant technical findings are promoted to the `atlas.md` within the Cortex.

---
*Built for the next generation of AI-native development.*
