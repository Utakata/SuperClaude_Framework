---
description: "Integrates the code with third-party services and APIs."
---

# Integrate Command

Integrates the code with third-party APIs, services, or other systems.

## Usage

```
/sc:integrate <service-name> [flags]
```

## Arguments

- `service-name`: The name of the service to integrate with (e.g., `stripe`, `sendgrid`).

## Flags

- `--type <type>`: The integration type (`api`, `database`, `service`).
- `--file <path>`: The file to add the integration code to.
- `--dry-run`: Show the proposed changes without applying them.
- `--persona-backend-architect`: Activate the backend architect agent.

## Behavior

When you execute `/sc:integrate $ARGUMENTS`:

1.  **Parse Arguments**: Extract the service name and integration flags from `$ARGUMENTS`.
2.  **Fetch Documentation**: Fetch the documentation for the specified service.
3.  **Activate Agents**: Engage the `@agent-backend-architect` to design the integration.
4.  **Generate Code**: Generate the code to integrate with the service.
5.  **Write to File**: Write the generated code to the specified file.
6.  **Report Results**: Provide a summary of the integration.

## Integration Points

-   **Agent Personas**: Activates `@agent-backend-architect` and `@agent-system-architect` for expert integration design.
-   **API Client Libraries**: Uses API client libraries and SDKs to simplify integration.

## Examples

```bash
# Integrate with the Stripe API
/sc:integrate stripe --type api --file src/payments.js

# Integrate with a PostgreSQL database
/sc:integrate postgresql --type database

# Dry run an integration with a third-party service
/sc:integrate sendgrid --type service --dry-run
```

## Output Format

The command's output includes:
-   **Code Snippet**: The generated code for the integration.
-   **File Path**: The path to the file where the code was added.
-   **Instructions**: Instructions on how to use the integrated service.
-   **Dependencies**: A list of any new dependencies that were added.
