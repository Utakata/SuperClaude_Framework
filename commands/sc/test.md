---
description: "Executes unit, integration, and end-to-end tests."
---

# Test Command

Runs unit, integration, and end-to-end tests for the project.

## Usage

```
/sc:test [flags]
```

## Arguments

*(None)*

## Flags

- `--type <type>`: Specify the test type to run (`unit`, `integration`, `e2e`).
- `--file <path>`: Run tests for a specific file.
- `--dir <path>`: Run tests for a specific directory.
- `--watch`: Watch for file changes and re-run tests automatically.
- `--coverage`: Generate a test coverage report.
- `--persona-qa`: Activate the QA specialist agent for test analysis.

## Behavior

When you execute `/sc:test $ARGUMENTS`:

1.  **Parse Arguments**: Extract test flags from `$ARGUMENTS`.
2.  **Identify Test Runner**: Detect the testing framework used in the project (e.g., `pytest`, `jest`, `go test`).
3.  **Construct Test Command**: Build the appropriate command-line instruction for the detected test runner.
4.  **Execute Tests**: Run the tests and capture the output.
5.  **Generate Coverage (if specified)**: If `--coverage` is present, generate a coverage report.
6.  **Report Results**: Display a summary of the test results, including passed, failed, and skipped tests.

## Integration Points

-   **Agent Personas**: Activates `@agent-qa` for analyzing test failures and suggesting fixes.
-   **CI/CD Systems**: A critical component of the CI pipeline to ensure code quality before deployment.

## Examples

```bash
# Run all unit tests
/sc:test --type unit

# Run integration tests for a specific file
/sc:test --type integration --file src/api/auth.test.js

# Run all tests in a directory and generate a coverage report
/sc:test --dir tests/ --coverage

# Watch for changes and re-run e2e tests
/sc:test --type e2e --watch
```

## Output Format

The command's output includes:
-   **Test Runner Output**: The standard output from the testing framework.
-   **Test Summary**: A summary of passed, failed, and skipped tests.
-   **Coverage Report**: A report showing the percentage of code covered by tests (if requested).
-   **Error Details**: Detailed stack traces and error messages for failed tests.
