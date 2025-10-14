# SuperClaude Framework

<div align="center">

![SuperClaude Logo](https://img.shields.io/badge/SuperClaude-v4.2-blue)
![Claude Code Compatible](https://img.shields.io/badge/Claude_Code-Plugin_System-green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Meta-programming framework that transforms Claude Code into a structured development platform**

[Quick Start](#-quick-installation) •
[Support](#-support-the-project) •
[Features](#-whats-new-in-v4) •
[Docs](#-documentation) •
[Contributing](#-contributing)

</div>

---

## 🚀 Migration to Claude Code Plugin System

**✅ PR #422: Successfully migrated to official Claude Code Plugin System**

SuperClaude Framework has been completely restructured to align with the official Claude Code plugin architecture, providing better integration, maintainability, and extensibility.

### 🎯 New Architecture Highlights

| Component | Count | Description |
|-----------|-------|-------------|
| **Slash Commands** | 25 | Specialized development tools |
| **AI Agents** | 15 | Domain-specific expertise |
| **Behavioral Modes** | 7 | Adaptive context handling |
| **MCP Servers** | 8 | External integrations |

### 📁 New Directory Structure

```
SuperClaude_Framework/
├── .claude-plugin/        # Plugin metadata
├── commands/sc/           # Slash commands (/sc:*)
├── agents/                # Specialized AI agents
├── hooks/                 # Lifecycle hooks
├── scripts/               # Automation scripts
├── docs/                  # Documentation
└── memory/                # Context persistence
```

### 🔧 Configuration Files

- `plugin.json` - Plugin manifest
- `.mcp.json` - MCP server configurations
- `hooks.json` - Hook definitions
- `marketplace.json` - Marketplace metadata

📖 **Migration Guide**: See [MIGRATION.md](./MIGRATION.md) for detailed migration instructions from v3 to v4.

---

## 📦 Quick Installation

SuperClaude is a meta-programming configuration framework that transforms Claude Code into a structured development platform through behavioral instruction injection and component orchestration.

> **Note**: This project is not affiliated with or endorsed by Anthropic.
> Claude Code is a product built and maintained by [Anthropic](https://www.anthropic.com/).

### Installation Methods

| Method | Command | Best For |
|--------|---------|----------|
| 🐍 pipx | `pipx install SuperClaude && pipx upgrade SuperClaude && SuperClaude install` | ✅ Recommended - Linux/macOS |
| 📦 pip | `pip install SuperClaude && pip upgrade SuperClaude && SuperClaude install` | Traditional Python environments |
| 🌐 npm | `npm install -g @bifrost_inc/superclaude && superclaude install` | Cross-platform, Node.js users |

### ⚠️ IMPORTANT: Upgrading from V3

If you have SuperClaude V3 installed, **uninstall it first**:

```bash
# Remove V3 files and directories
rm ~/.claude/*.md ~/.claude/*.json ~/.claude/commands/ -rf

# Install V4
pipx install SuperClaude && pipx upgrade SuperClaude && SuperClaude install
```

✅ **Preserved during upgrade**:
- ✓ Custom slash commands (outside `commands/sc/`)
- ✓ Custom content in `CLAUDE.md`
- ✓ Claude Code config files (`.claude.json`, `.credentials.json`, `settings.json`)
- ✓ Custom agents and user files

⚠️ **Note**: `.json` config files from V3 may cause conflicts and should be removed.

### 💡 Troubleshooting PEP 668 Errors

```bash
# Option 1: Use pipx (Recommended)
pipx install SuperClaude

# Option 2: User installation
pip install --user SuperClaude

# Option 3: Virtual environment
python3 -m venv superclaude-env
source superclaude-env/bin/activate
pip install SuperClaude

# Option 4: Force (use with caution)
pip install --break-system-packages SuperClaude
```

---

## 💝 Support the Project

Maintaining SuperClaude requires significant time and resources ($100/month for Claude Max testing alone).

If you find value in SuperClaude, consider supporting:

| One-time | Monthly | Flexible |
|----------|---------|----------|
| [Buy Me a Coffee](https://buymeacoffee.com/superclaud) | [Patreon](https://patreon.com/superclaude) | [GitHub Sponsors](https://github.com/sponsors/SuperClaude-Org) |

**What your support enables**:
- 🔬 Claude Max testing ($100/month)
- ⚡ Feature development
- 📚 Comprehensive documentation
- 🤝 Quick community support
- 🔧 MCP integration testing
- 🌐 Infrastructure costs

> **Note**: The framework stays open source regardless. Contributions through code, documentation, or spreading the word also help! 🙏

---

## ✨ What's New in V4

Version 4 brings significant improvements based on community feedback and real-world usage patterns.

### 🤖 15 Specialized AI Agents

| Frontend | Backend | DevOps | Specialized |
|----------|---------|--------|-------------|
| Frontend Expert | Backend Expert | DevOps Engineer | Security Specialist |
| UI/UX Designer | API Architect | Infrastructure Pro | Performance Engineer |
| Accessibility Pro | Database Expert | CI/CD Expert | Documentation Writer |
|  | Testing Engineer | Monitoring Pro | Code Reviewer |

### 🔌 8 Powerful MCP Servers

| Search & Research | Development | Testing | Memory |
|-------------------|-------------|---------|--------|
| Tavily (Web Search) | Context7 (Docs) | Playwright (Browser) | Serena (Memory) |
| Brave Search | Sequential (Reasoning) | Puppeteer (Automation) | |
|  | Magic (UI Generation) |  | |

### 🎨 7 Adaptive Behavioral Modes

| Mode | Purpose |
|------|---------|
| **Brainstorming** | Creative ideation & exploration |
| **Task Management** | Systematic progress tracking |
| **Token Efficiency** | Compression for large projects |
| **Orchestration** | Multi-tool coordination |
| **Introspection** | Framework self-analysis |
| **Code Review** | Quality & security analysis |
| **Documentation** | Auto-generation & maintenance |

### 🚀 70% Token Reduction Pipeline

- **Smaller framework, bigger projects**: Manage complex codebases efficiently
- **Cost optimization**: Reduce API costs while maintaining quality
- **Performance boost**: Faster responses in resource-constrained environments
- **Smart compression**: Context-aware optimization

### 🔧 Complete Developer Rewrite

- **Plugin-first architecture**: Native Claude Code plugin system
- **Modular design**: Easy extension and customization
- **Type-safe configs**: JSON Schema validation
- **Hook system**: Lifecycle event handling
- **Marketplace ready**: Distribution via official channels

---

## 🔬 Deep Research (v4.2)

SuperClaude v4.2 introduces comprehensive autonomous web research capabilities.

### 🎯 Three Intelligent Strategies

| Strategy | Use Case |
|----------|----------|
| **Fast Track** | Quick facts, simple queries (~2min) |
| **Balanced** | General research, default mode (~5min) |
| **Planning Only** | Research planning without execution |

### 🔄 Research Features

- **Up to 5 iterative searches**: Adaptive depth control
- **Confidence-based validation**: Quality assurance
- **Cross-session intelligence**: Memory persistence
- **Multi-tool coordination**: Tavily, Playwright, Sequential, Serena

### 📝 Usage Examples

```bash
# Basic research with automatic depth
/sc:research "latest AI developments 2024"

# Controlled research depth
/sc:research "quantum computing breakthroughs" --depth exhaustive

# Specific strategy selection
/sc:research "market analysis" --strategy planning-only

# Domain-filtered research
/sc:research "React patterns" --domains "reactjs.org,github.com"
```

### 📊 Research Depth Levels

| Depth | Sources | Hops | Time | Best For |
|-------|---------|------|------|----------|
| **Quick** | 5-10 | 1 | ~2min | Quick facts, simple queries |
| **Standard** | 10-20 | 3 | ~5min | General research (default) |
| **Deep** | 20-40 | 4 | ~8min | Comprehensive analysis |
| **Exhaustive** | 40+ | 5 | ~10min | Academic-level research |

---

## 📚 Documentation

### 🚀 Getting Started
- [**Installation Guide**](Docs/Getting-Started/installation.md) - *Setup instructions*
- [**Quick Start**](Docs/Getting-Started/quick-start.md) - *First steps*
- [**Migration Guide**](MIGRATION.md) - *V3 → V4 migration*

### 📖 User Guides
- [**User Guide**](Docs/superclaude-user-guide.md) - *Complete framework overview*
- [**Commands Guide**](Docs/Reference/commands.md) - *All slash commands*
- [**Agents Guide**](Docs/Reference/agents.md) - *Specialized personas*
- [**Flags Reference**](Docs/Reference/flags.md) - *Behavioral modifiers*
- [**MCP Servers**](Docs/Reference/mcp-servers.md) - *Integration details*

### 🛠️ Developer Resources
- [**Architecture**](Docs/Developer/architecture.md) - *Technical design*
- [**API Reference**](Docs/Developer/api.md) - *Python API*
- [**Plugin Development**](Docs/Developer/plugin-development.md) - *Creating plugins*
- [**Contributing Guide**](CONTRIBUTING.md) - *How to contribute*

### 📋 Reference
- [**Examples Cookbook**](Docs/Reference/examples-cookbook.md) - *Real-world recipes*
- [**FAQ**](Docs/Reference/faq.md) - *Common questions*
- [**Troubleshooting**](Docs/Reference/troubleshooting.md) - *Problem solving*
- [**Changelog**](CHANGELOG.md) - *Version history*

---

## 🤝 Contributing

We welcome contributions of all kinds!

| Priority | Area | Description |
|----------|------|-------------|
| 📝 **High** | **Documentation** | Improve guides, add examples, fix typos |
| 🔧 **High** | **MCP Integration** | Add server configs, test integrations |
| 🎯 **Medium** | **Workflows** | Create command patterns & recipes |
| 🧪 **Medium** | **Testing** | Add tests, validate features |
| 🌐 **Low** | **i18n** | Translate docs to other languages |

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for developers who push boundaries**

[GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) • [Documentation](https://superclaude.org/docs) • [Discord](https://discord.gg/superclaude)

</div>
