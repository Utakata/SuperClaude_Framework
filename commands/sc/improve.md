---
description: "Improves code by applying optimizations and best practices."
---

# Improve Command

Improves the quality of the code by applying optimizations, refactoring, and adhering to best practices.

## Usage

```
/sc:improve <target> [flags]
```

## Arguments

- `target`: The file or directory to improve.

## Flags

- `--type <type>`: Specify the improvement type (`performance`, `readability`, `maintainability`).
- `--level <level>`: Specify the improvement level (`light`, `medium`, `heavy`).
- `--dry-run`: Show the proposed changes without applying them.
- `--persona-performance-engineer`: Activate the performance engineer agent.
- `--persona-refactoring-expert`: Activate the refactoring expert agent.

## Behavior

When you execute `/sc:improve $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and improvement flags from `$ARGUMENTS`.
2.  **Analyze Code**: Analyze the code to identify areas for improvement.
3.  **Activate Agents**: Engage the appropriate agents (`@agent-performance-engineer`, `@agent-refactoring-expert`) to suggest improvements.
4.  **Apply Improvements**: Apply the selected improvements to the code.
5.  **Validate Changes**: Run tests to ensure that the improvements have not introduced any regressions.
6.  **Report Results**: Provide a summary of the improvements that were made.

## Integration Points

-   **Agent Personas**: Activates `@agent-performance-engineer` and `@agent-refactoring-expert` for specialized advice.
-   **Static Analysis Tools**: Integrates with static analysis tools to identify areas for improvement.

## Examples

```bash
# Improve the performance of a file
/sc:improve src/utils.js --type performance

# Improve the readability of a directory
/sc:improve src/components/ --type readability --level medium

# Dry run maintainability improvements
/sc:improve src/ --type maintainability --dry-run
```

## Output Format

The command's output includes:
-   **Improvement Summary**: A list of the improvements that were made.
-   **Code Diff**: A diff of the changes that were made to the code.
-   **Test Results**: The results of the tests that were run to verify the changes.
-   **Code Quality Metrics**: A comparison of code quality metrics before and after the improvements.
