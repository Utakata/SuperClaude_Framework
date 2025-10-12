---
description: "Assists with troubleshooting and debugging issues."
---

# Troubleshoot Command

Helps diagnose and resolve problems, debug code, and troubleshoot issues.

## Usage

```
/sc:troubleshoot <issue-description> [flags]
```

## Arguments

- `issue-description`: A clear and concise description of the issue.

## Flags

- `--file <path>`: The file where the issue is occurring.
- `--dir <path>`: The directory where the issue is occurring.
- `--type <type>`: The type of issue (`bug`, `performance`, `security`, `connection`).
- `--persona-root-cause-analyst`: Activate the root cause analyst agent.

## Behavior

When you execute `/sc:troubleshoot $ARGUMENTS`:

1.  **Parse Arguments**: Extract the issue description and flags from `$ARGUMENTS`.
2.  **Gather Context**: Ask clarifying questions to gather more information about the issue.
3.  **Analyze Symptoms**: Analyze the symptoms of the issue to form a hypothesis.
4.  **Propose Solutions**: Propose a set of steps to diagnose and resolve the issue.
5.  **Guide Debugging**: Guide the user through the debugging process.

## Integration Points

-   **Agent Personas**: Activates `@agent-root-cause-analyst`, `@agent-security`, and `@agent-performance` for specialized troubleshooting.
-   **Logging and Monitoring Tools**: Integrates with logging and monitoring tools to gather information about the issue.

## Examples

```bash
# Troubleshoot a bug in a file
/sc:troubleshoot "User login is failing with a 500 error" --file src/auth.js --type bug

# Troubleshoot a performance issue in a directory
/sc:troubleshoot "The dashboard is loading slowly" --dir src/dashboard/ --type performance

# Troubleshoot a connection issue
/sc:troubleshoot "Cannot connect to the database" --type connection
```

## Output Format

The command's output includes:
-   **Hypothesis**: A hypothesis about the root cause of the issue.
-   **Diagnostic Steps**: A list of steps to diagnose the issue.
-   **Proposed Solution**: A proposed solution to the issue.
-   **Clarifying Questions**: A list of questions to gather more information.
