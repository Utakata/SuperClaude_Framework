---
description: "Scans for security vulnerabilities."
---

# Scan Command

Scans the codebase for security vulnerabilities and provides a detailed report.

## Usage

```
/sc:scan <target> [flags]
```

## Arguments

- `target`: The file or directory to scan.

## Flags

- `--type <type>`: Specify the scan type (`sast`, `dast`, `sca`).
- `--severity <level>`: Filter by severity level (`critical`, `high`, `medium`, `low`).
- `--format <format>`: Specify the output format (`json`, `html`, `sarif`).
- `--persona-security`: Activate the security engineer agent.

## Behavior

When you execute `/sc:scan $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and scan flags from `$ARGUMENTS`.
2.  **Configure Scanner**: Configure the security scanner based on the specified scan type and severity level.
3.  **Run Scan**: Run the security scan on the target code.
4.  **Analyze Results**: Analyze the scan results to identify and categorize vulnerabilities.
5.  **Generate Report**: Generate a report of the scan findings in the specified format.

## Integration Points

-   **Agent Personas**: Activates `@agent-security` for expert analysis of security vulnerabilities.
-   **Security Scanners**: Integrates with security scanning tools like `snyk`, `semgrep`, and `trivy`.

## Examples

```bash
# Run a SAST scan on a directory
/sc:scan src/ --type sast

# Scan for high-severity vulnerabilities and generate an HTML report
/sc:scan . --severity high --format html

# Run a software composition analysis (SCA) scan
/sc:scan package-lock.json --type sca
```

## Output Format

The command's output includes:
-   **Vulnerability List**: A list of the vulnerabilities that were found.
-   **Severity Level**: The severity level of each vulnerability.
-   **File and Line Number**: The location of each vulnerability.
-   **Remediation Advice**: Advice on how to fix each vulnerability.
-   **CVE Links**: Links to the CVEs for each vulnerability.
