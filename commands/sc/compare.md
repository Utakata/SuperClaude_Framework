---
description: "Compares two files, directories, or code snippets."
---

# Compare Command

Compares two files, directories, or code snippets and highlights the differences.

## Usage

```
/sc:compare <source> <target> [flags]
```

## Arguments

- `source`: The source file, directory, or code snippet to compare.
- `target`: The target file, directory, or code snippet to compare.

## Flags

- `--format <format>`: The output format (`diff`, `table`, `json`).
- `--ignore-whitespace`: Ignore whitespace differences.
- `--brief`: Show a brief summary of the differences.
- `--persona-quality-engineer`: Activate the quality engineer agent.

## Behavior

When you execute `/sc:compare $ARGUMENTS`:

1.  **Parse Arguments**: Extract the source, target, and comparison flags from `$ARGUMENTS`.
2.  **Read Content**: Read the content of the source and target.
3.  **Activate Agents**: Engage the `@agent-quality-engineer` to perform the comparison.
4.  **Compare Content**: Compare the content and identify the differences.
5.  **Format Output**: Format the differences according to the specified format.

## Integration Points

-   **Agent Personas**: Activates `@agent-quality-engineer` for expert comparison.
-   **Diff Tools**: Integrates with diff tools to visualize the differences.

## Examples

```bash
# Compare two files
/sc:compare file1.js file2.js

# Compare two directories and ignore whitespace
/sc:compare dir1/ dir2/ --ignore-whitespace

# Compare two code snippets and show a brief summary
/sc:compare "<code>" "<code>" --brief
```

## Output Format

The command's output includes:
-   **Diff**: The differences between the source and target.
-   **Summary**: A summary of the differences.
-   **Table**: A side-by-side comparison of the source and target.
-   **JSON**: The differences in JSON format.
