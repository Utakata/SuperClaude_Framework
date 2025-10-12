---
description: "Optimizes code for performance and memory usage."
---

# Optimize Command

Optimizes code for performance, memory usage, and other quality metrics.

## Usage

```
/sc:optimize <target> [flags]
```

## Arguments

- `target`: The file or directory to optimize.

## Flags

- `--type <type>`: Specify the optimization type (`performance`, `memory`, `readability`).
- `--level <level>`: Specify the optimization level (`light`, `medium`, `heavy`).
- `--dry-run`: Show the proposed changes without applying them.
- `--persona-performance`: Activate the performance engineer agent.

## Behavior

When you execute `/sc:optimize $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and optimization flags from `$ARGUMENTS`.
2.  **Analyze Target**: Profile the target code to identify performance bottlenecks or areas for improvement.
3.  **Activate Agents**: Engage the `@agent-performance` to suggest optimization strategies.
4.  **Apply Optimizations**: Apply the selected optimizations to the code.
5.  **Validate Changes**: Run tests to ensure that the optimizations have not introduced any regressions.
6.  **Report Results**: Provide a summary of the optimizations applied and the resulting performance improvements.

## Integration Points

-   **Agent Personas**: Primarily activates `@agent-performance` for expert optimization advice.
-   **Profiling Tools**: Integrates with profiling tools to identify performance bottlenecks.

## Examples

```bash
# Optimize a file for performance
/sc:optimize src/utils.js --type performance

# Perform a heavy memory optimization on a directory
/sc:optimize src/components/ --type memory --level heavy

# Dry run readability optimizations
/sc:optimize src/ --type readability --dry-run
```

## Output Format

The command's output includes:
-   **Optimization Summary**: A list of the optimizations that were applied.
-   **Performance Metrics**: A comparison of performance metrics before and after the optimization.
-   **Code Diff**: A diff of the changes that were made to the code.
-   **Validation Results**: The results of the tests that were run to validate the changes.
