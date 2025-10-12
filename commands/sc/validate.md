---
description: "Validates code against a set of rules or standards."
---

# Validate Command

Validates code for correctness, completeness, and compliance with a set of rules or standards.

## Usage

```
/sc:validate <target> [flags]
```

## Arguments

- `target`: The file or directory to validate.

## Flags

- `--rules <file>`: A file containing custom validation rules.
- `--format <format>`: The output format (`json`, `html`, `text`).
- `--fix`: Automatically fix validation errors.
- `--persona-quality-engineer`: Activate the quality engineer agent.

## Behavior

When you execute `/sc:validate $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and validation flags from `$ARGUMENTS`.
2.  **Load Rules**: Load the validation rules from the specified file or from a default configuration.
3.  **Activate Agents**: Engage the `@agent-quality-engineer` to perform the validation.
4.  **Run Validation**: Run the validation checks on the target code.
5.  **Generate Report**: Generate a report of the validation findings in the specified format.
6.  **Apply Fixes (if specified)**: If `--fix` is present, automatically apply fixes for the validation errors.

## Integration Points

-   **Agent Personas**: Activates `@agent-quality-engineer` and `@agent-security` for expert validation.
-   **Linters and Static Analysis Tools**: Integrates with linters and static analysis tools to perform validation.

## Examples

```bash
# Validate a file against a set of rules
/sc:validate src/auth.js --rules ./.validation-rules.json

# Validate a directory and automatically fix errors
/sc:validate src/api/ --fix

# Validate the entire project and generate an HTML report
/sc:validate . --format html
```

## Output Format

The command's output includes:
-   **Validation Report**: A report of the validation findings.
-   **Error List**: A list of validation errors.
-   **Suggestions**: Suggestions for fixing the errors.
-   **Code Diff**: A diff of the changes that were made to the code (if `--fix` was used).
