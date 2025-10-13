# MCP Server Configuration Guide

## Overview
SuperClaude integrates 8 MCP servers for enhanced capabilities. This guide provides details on their purpose, configuration, and how to use them effectively.

## 1. Sequential Thinking (`sequential-thinking`)
- **Purpose**: Enables multi-step reasoning, complex planning, and systematic analysis. Ideal for tasks like designing architecture or formulating a detailed plan.
- **Trigger**: Activated by commands like `/sc:design`, `/sc:plan`, or flags like `--seq`.
- **API Key**: Not required.

## 2. Context7 (`context7`)
- **Purpose**: Provides up-to-date documentation and context for various frameworks and libraries. Essential for writing code that uses external dependencies.
- **Trigger**: Activated automatically when `import` statements or framework-specific keywords are detected.
- **API Key**: `TWENTYFIRST_API_key` (optional, for premium features).

## 3. Magic (`magic`)
- **Purpose**: Specialized in UI generation and frontend component creation.
- **Trigger**: Activated during UI-related tasks, such as `/sc:implement --type component`.
- **API Key**: Not required.

## 4. Playwright (`playwright`)
- **Purpose**: Enables browser automation for end-to-end testing, web scraping, and UI validation.
- **Trigger**: Activated by testing commands like `/sc:test --type e2e`.
- **API Key**: Not required.

## 5. Morphllm (`morphllm-fast-apply`)
- **Purpose**: Provides advanced, large-scale language model operations and transformations.
- **Trigger**: Used in complex refactoring or bulk content generation tasks.
- **API Key**: `MORPH_API_KEY` (required).

## 6. Serena (`serena`)
- **Purpose**: Manages session memory and context persistence, allowing for conversations that span multiple interactions.
- **Trigger**: Activated automatically at the start of a session to manage memory.
- **API Key**: Not required. The `SERENA_MEMORY_PATH` is configured automatically.

## 7. Tavily (`tavily`)
- **Purpose**: Powers the deep research capabilities of the `/sc:research` command by providing web search results.
- **Trigger**: Activated by the `/sc:research` command.
- **API Key**: `TAVILY_API_KEY` (required).

## 8. Firecrawl (`firecrawl`)
- **Purpose**: Used for web scraping and extracting structured content from websites.
- **Trigger**: Can be activated during research or data gathering tasks.
- **API Key**: `FIRECRAWL_API_KEY` (required).

## Setup and Configuration

### Required API Keys
To use the full capabilities of SuperClaude, you will need to set the following environment variables:
- `TAVILY_API_KEY`: For web search in `/sc:research`.
- `FIRECRAWL_API_KEY`: For web scraping.
- `MORPH_API_KEY`: For advanced LLM transformations.

### Automatic Connection
By default, SuperClaude will attempt to auto-connect to all configured MCP servers when your Claude Code session starts. Servers that require an API key will be disabled if the key is not found.

### Troubleshooting
- **MCP Connection Errors**: Ensure Node.js v18+ is installed and accessible in your path. For Windows users, the framework uses a `cmd /c` wrapper for compatibility.
- **API Key Errors**: Double-check that your environment variables are set correctly and that the API keys are valid.
- **Server Crashes**: Check the logs in your Claude Code workspace for error messages from the specific MCP server.
