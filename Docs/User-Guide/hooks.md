# SuperClaude Hooks Guide

## Overview
Hooks allow you to automate actions at key points in your workflow.

## Available Hooks
- `pre-write`: Before files are written
- `post-write`: After files are written
- `pre-commit`: Before Git commits
- `post-command`: After slash commands execute

## Configuration
Edit `hooks/hooks.json` to customize hook behavior.

## Examples

### Example 1: Auto-format Python code before writing

To automatically format your Python files with `black` every time a file is written, you can use the `pre-write` hook.

**`hooks/hooks.json`:**
```json
{
  "version": "1.0.0",
  "hooks": {
    "pre-write": {
      "name": "Format Before Write",
      "enabled": true,
      "actions": [
        {
          "name": "python-formatter",
          "condition": "file.extension === '.py'",
          "command": "black {file}",
          "continueOnError": false
        }
      ]
    }
  }
}
```

### Example 2: Run tests after writing to a source file

To automatically trigger `pytest` after you modify a Python file in your `src/` directory, you can use the `post-write` hook.

**`hooks/hooks.json`:**
```json
{
  "version": "1.0.0",
  "hooks": {
    "post-write": {
      "name": "Run Tests After Write",
      "description": "Automatically run tests after code changes",
      "enabled": true,
      "actions": [
        {
          "name": "pytest",
          "condition": "file.path.includes('src/') && file.extension === '.py'",
          "command": "pytest tests/",
          "continueOnError": true
        }
      ]
    }
  }
}
```
