---
description: "Generates technical documentation and README files."
---

# Document Command

Generates technical documentation, such as README files, API documentation, and code comments.

## Usage

```
/sc:document <target> [flags]
```

## Arguments

- `target`: The file, directory, or project to document.

## Flags

- `--type <type>`: Specify the documentation type (`readme`, `api`, `comments`).
- `--format <format>`: Specify the output format (`markdown`, `html`, `pdf`).
- `--overwrite`: Overwrite existing documentation.
- `--persona-technical-writer`: Activate the technical writer agent.

## Behavior

When you execute `/sc:document $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and documentation flags from `$ARGUMENTS`.
2.  **Analyze Code**: Analyze the code to understand its structure, functionality, and APIs.
3.  **Activate Agents**: Engage the `@agent-technical-writer` to generate clear and concise documentation.
4.  **Generate Documentation**: Create the specified type of documentation in the specified format.
5.  **Write to File**: Write the generated documentation to the appropriate file.

## Integration Points

-   **Agent Personas**: Primarily activates `@agent-technical-writer` for creating high-quality documentation.
-   **Code Analysis Tools**: Integrates with code analysis tools to extract information about the code.

## Examples

```bash
# Generate a README file for the project
/sc:document . --type readme

# Generate API documentation for a directory in HTML format
/sc:document src/api/ --type api --format html

# Add comments to a file and overwrite existing comments
/sc:document src/utils.js --type comments --overwrite
```

## Output Format

The command's output includes:
-   **File Path**: The path to the generated documentation file.
-   **Status Message**: A message indicating whether the documentation was generated successfully.
-   **Preview**: A preview of the generated documentation.
