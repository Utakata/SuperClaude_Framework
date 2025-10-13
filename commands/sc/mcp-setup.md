---
description: "Helps with the setup of recommended MCP servers."
---

# MCP Setup Command

Guides the user through the installation and configuration of recommended MCP servers.

## Usage

```
/sc:mcp-setup [flags]
```

## Arguments

*(None)*

## Flags

- `--list`: List all recommended MCP servers.
- `--install <name>`: Provide installation instructions for a specific MCP server.

## Behavior

When you execute `/sc:mcp-setup $ARGUMENTS`:

1.  **Parse Arguments**: Extract the flags from `$ARGUMENTS`.
2.  **List Servers (if specified)**: If `--list` is present, list the recommended MCP servers from `marketplace.json`.
3.  **Provide Instructions (if specified)**: If `--install <name>` is present, provide detailed installation and configuration instructions for the specified server.
4.  **Default Behavior**: If no flags are provided, explain the purpose of recommended MCP servers and guide the user to use the `--list` or `--install` flags.

## Integration Points

-   **`marketplace.json`**: Reads the `recommendedMcpServers` section to get the list of servers.
-   **`docs/Reference/mcp-setup.md`**: Refers the user to the detailed documentation.

## Examples

```bash
# List recommended servers
/sc:mcp-setup --list

# Get installation instructions for ollama-mcp
/sc:mcp-setup --install ollama-mcp
```

## Output Format

The command's output will be a textual guide that helps the user with the setup process.
