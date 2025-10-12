---
description: "Refactors code to resolve debt and improve structure."
---

# Refactor Command

Restructures existing computer code, changing the factoring, without changing its external behavior.

## Usage

```
/sc:refactor <target> [flags]
```

## Arguments

- `target`: The file or directory to refactor.

## Flags

- `--level <level>`: Specify the refactoring level (`light`, `medium`, `heavy`).
- `--rules <file>`: Provide a file with custom refactoring rules.
- `--dry-run`: Show the proposed changes without applying them.
- `--persona-refactoring-expert`: Activate the refactoring expert agent.

## Behavior

When you execute `/sc:refactor $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and refactoring flags from `$ARGUMENTS`.
2.  **Analyze Code**: Statically analyze the target code to identify code smells, anti-patterns, and areas for improvement.
3.  **Suggest Refactorings**: Propose a set of refactoring operations based on the analysis.
4.  **Apply Changes (if not dry-run)**: Apply the selected refactorings to the code.
5.  **Verify Changes**: Run tests to ensure that the refactoring has not changed the external behavior of the code.
6.  **Report Results**: Provide a summary of the refactorings that were applied.

## Integration Points

-   **Agent Personas**: Activates `@agent-refactoring-expert` for specialized refactoring knowledge.
-   **Static Analysis Tools**: Integrates with static analysis tools to identify refactoring opportunities.

## Examples

```bash
# Perform a medium-level refactoring on a file
/sc:refactor src/utils.js --level medium

# Dry run a heavy refactoring on a directory
/sc:refactor src/components/ --level heavy --dry-run

# Apply custom refactoring rules
/sc:refactor src/ --rules ./.refactor-rules.json
```

## Output Format

The command's output includes:
-   **Refactoring Summary**: A list of the refactorings that were applied.
-   **Code Diff**: A diff of the changes that were made to the code.
-   **Test Results**: The results of the tests that were run to verify the changes.
-   **Code Quality Metrics**: A comparison of code quality metrics before and after the refactoring.
