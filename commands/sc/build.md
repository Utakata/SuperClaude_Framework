---
description: "Executes project builds and compilation."
---

# Build Command

Compiles the project, runs build scripts, and packages the application for deployment.

## Usage

```
/sc:build [flags]
```

## Arguments

*(None)*

## Flags

- `--env <name>`: Specify the build environment (e.g., `production`, `development`, `staging`).
- `--platform <name>`: Specify the target platform (e.g., `docker`, `serverless`, `web`).
- `--clean`: Perform a clean build, removing previous build artifacts before starting.
- `--verbose`: Show detailed output from the build process.

## Behavior

When you execute `/sc:build $ARGUMENTS`:

1.  **Parse Arguments**: Extract build flags from `$ARGUMENTS`.
2.  **Prepare Environment**: Set up the specified environment (`--env`) and platform (`--platform`).
3.  **Clean Build (if specified)**: If `--clean` is present, remove existing build artifacts.
4.  **Run Build Scripts**: Execute the project's build scripts (e.g., `npm run build`, `make`, `mvn package`).
5.  **Package Artifacts**: Collect and package the build outputs (e.g., binaries, compressed assets).
6.  **Report Status**: Output the results of the build, indicating success or failure and the location of artifacts.

## Integration Points

-   **Agent Personas**: Activates `@agent-devops` for build process management. May involve `@agent-backend` or `@agent-frontend` depending on the project type.
-   **CI/CD Systems**: Designed to be a key step in a CI/CD pipeline.

## Examples

```bash
# Build the project for the production environment
/sc:build --env production

# Perform a clean build for a Docker platform
/sc:build --platform docker --clean

# Build for staging with detailed logs
/sc:build --env staging --verbose
```

## Output Format

The command's output typically includes:
-   **Build Logs**: Real-time output from the build tools.
-   **Status Message**: A final message indicating success or failure.
-   **Artifact Path**: The path to the generated build artifacts.
-   **Build Metrics**: Information on build duration and artifact size.
