# SuperClaude v4 → v5 (Plugin) Migration Guide

## Overview
SuperClaude v5 adopts Anthropic's official plugin system for easier installation and updates.

## Before You Begin
- **Backup**: Your configurations will be preserved, but a backup is recommended
- **Time**: Migration takes 5-10 minutes
- **Compatibility**: v4 and v5 can coexist during the transition period

## Migration Steps

### Step 1: Check Your Current Installation
```bash
python3 migrate-to-plugin.py --check
```

### Step 2: Backup (Automatic)
```bash
python3 migrate-to-plugin.py --migrate
```
This automatically creates a backup at `~/.claude-v4-backup`

### Step 3: Install Plugin
In Claude Code:
```
/plugin marketplace add SuperClaude-Org/superclaude-plugin-marketplace
/plugin install superclaude-framework
```

### Step 4: Verify Installation
```
/help
```
You should see all 25 SuperClaude commands listed.

## Preserved Configurations
These files are NOT modified during migration:
- Custom `CLAUDE.md` additions
- Personal `.claude/settings.json`
- Project-specific configurations
- MCP server API keys

## Rollback (If Needed)
```bash
python3 migrate-to-plugin.py --rollback
```

## Troubleshooting

### Issue: `/plugin install` fails
- **Cause**: This can happen if the marketplace was not added correctly or if there's a network issue.
- **Solution**:
  1. Ensure you have a stable internet connection.
  2. Verify that the marketplace was added correctly by running `/plugin marketplace list`.
  3. Try removing and re-adding the marketplace:
     ```
     /plugin marketplace remove SuperClaude-Org/superclaude-plugin-marketplace
     /plugin marketplace add SuperClaude-Org/superclaude-plugin-marketplace
     ```

### Issue: Old commands are still showing up
- **Cause**: The migration script may not have fully cleaned up the old files.
- **Solution**:
  1. Manually delete the old command files from `~/.claude/commands/sc/`.
  2. Restart Claude Code.

### Issue: MCP Servers are not connecting
- **Cause**: API keys may not be correctly set as environment variables.
- **Solution**:
  1. Ensure that `TAVILY_API_KEY`, `FIRECRAWL_API_KEY`, etc., are set in your shell's startup file (e.g., `.bashrc`, `.zshrc`).
  2. Restart your terminal and Claude Code to ensure the environment variables are loaded.

## Support Period
- v4.x: Supported until April 2025 (6-month support window)
- v5.x: Current and actively developed
