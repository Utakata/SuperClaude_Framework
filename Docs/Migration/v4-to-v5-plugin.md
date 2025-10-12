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
[Detailed troubleshooting guide]

## Support Period
- v4.x: Supported until April 2025 (6-month support window)
- v5.x: Current and actively developed
