---
description: "Monitors the application for performance, errors, and security."
---

# Monitor Command

Monitors the application for performance, errors, and security issues in a specified environment.

## Usage

```
/sc:monitor <environment> [flags]
```

## Arguments

- `environment`: The environment to monitor (e.g., `production`, `staging`).

## Flags

- `--type <type>`: The type of monitoring to perform (`performance`, `errors`, `security`).
- `--dashboard <url>`: The URL of the monitoring dashboard.
- `--alerts <level>`: Configure alerts for a specific severity level (e.g., `critical`, `high`).
- `--persona-devops-architect`: Activate the DevOps architect agent.

## Behavior

When you execute `/sc:monitor $ARGUMENTS`:

1.  **Parse Arguments**: Extract the environment and monitoring flags from `$ARGUMENTS`.
2.  **Connect to Monitoring Service**: Connect to the monitoring service for the specified environment.
3.  **Activate Agents**: Engage the `@agent-devops-architect`, `@agent-security`, or `@agent-performance` based on the monitoring type.
4.  **Fetch Data**: Fetch monitoring data, such as performance metrics, error logs, and security alerts.
5.  **Analyze Data**: Analyze the data to identify trends, anomalies, and potential issues.
6.  **Report Findings**: Provide a summary of the monitoring findings.

## Integration Points

-   **Agent Personas**: Activates `@agent-devops-architect`, `@agent-security`, and `@agent-performance` for expert analysis.
-   **Monitoring Tools**: Integrates with monitoring tools like `Prometheus`, `Grafana`, `Sentry`, and `Datadog`.

## Examples

```bash
# Monitor the performance of the production environment
/sc:monitor production --type performance

# Monitor errors in the staging environment
/sc:monitor staging --type errors

# Configure critical security alerts for the production environment
/sc:monitor production --type security --alerts critical
```

## Output Format

The command's output includes:
-   **Monitoring Summary**: A summary of the monitoring findings.
-   **Key Metrics**: Key performance indicators (KPIs) and other metrics.
-   **Alerts**: A list of active alerts.
-   **Recommendations**: Recommendations for addressing any identified issues.
