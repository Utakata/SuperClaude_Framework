# Recommended MCP Server Setup Guide

## Overview
This guide provides detailed instructions for setting up recommended MCP (Model Context Protocol) servers that can extend the capabilities of the SuperClaude Framework.

## 1. Ollama MCP (`ollama-mcp`)

### Purpose
The `ollama-mcp` server allows SuperClaude to connect to local language models running via [Ollama](https://ollama.ai/). This is useful for:
- Offline development.
- Using custom or fine-tuned models.
- Reducing reliance on cloud-based APIs.

### Prerequisites
- [Ollama](https://ollama.ai/) installed and running on your local machine.
- A model pulled via `ollama pull <model-name>`.

### Installation
The `ollama-mcp` server is a community-maintained plugin. You can install it via the Claude Code plugin system:

```
/plugin install ollama/ollama-mcp
```

### Configuration
Once installed, you may need to configure the server to point to your local Ollama instance if it's not running on the default port.

1.  **Find the configuration file**: The configuration file is typically located at `~/.claude/plugins/ollama-mcp/config.json`.
2.  **Edit the file**: Modify the `endpoint` URL to match your Ollama setup.

    ```json
    {
      "endpoint": "http://localhost:11434"
    }
    ```

### Usage
Once configured, you can use the `/sc:ask-local` command (or a similar command provided by the plugin) to interact with your local model.

---

*This document will be updated as more recommended MCP servers are added to the marketplace.*
