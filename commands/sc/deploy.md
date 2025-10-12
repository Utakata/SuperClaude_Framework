---
description: "Deploys the application to various environments."
---

# Deploy Command

Deploys the application to a specified environment, such as production, staging, or testing.

## Usage

```
/sc:deploy <environment> [flags]
```

## Arguments

- `environment`: The target environment for the deployment (e.g., `production`, `staging`).

## Flags

- `--version <version>`: Specify a specific version to deploy.
- `--platform <platform>`: Specify the deployment platform (e.g., `docker`, `serverless`, `web`).
- `--canary`: Perform a canary deployment.
- `--persona-devops-architect`: Activate the DevOps architect agent.

## Behavior

When you execute `/sc:deploy $ARGUMENTS`:

1.  **Parse Arguments**: Extract the environment and deployment flags from `$ARGUMENTS`.
2.  **Fetch Artifacts**: Fetch the build artifacts for the specified version.
3.  **Activate Agents**: Engage the `@agent-devops-architect` to manage the deployment process.
4.  **Execute Deployment**: Deploy the application to the target environment.
5.  **Verify Deployment**: Run health checks to ensure that the deployment was successful.
6.  **Report Status**: Provide a summary of the deployment status.

## Integration Points

-   **Agent Personas**: Primarily activates `@agent-devops-architect` for managing the deployment process.
-   **CI/CD Systems**: Integrates with CI/CD systems to automate deployments.
-   **Cloud Providers**: Interacts with cloud provider APIs to deploy the application.

## Examples

```bash
# Deploy the latest version to production
/sc:deploy production

# Deploy a specific version to staging
/sc:deploy staging --version v1.2.3

# Perform a canary deployment to production
/sc:deploy production --canary

# Deploy to a Docker platform with the DevOps architect
/sc:deploy production --platform docker --persona-devops-architect
```

## Output Format

The command's output includes:
-   **Deployment Logs**: Real-time output from the deployment tools.
-   **Status Message**: A final message indicating success or failure.
-   **Endpoint URL**: The URL of the deployed application.
-   **Verification Results**: The results of the health checks.
