---
description: "Handles database, API, and infrastructure migrations."
---

# Migrate Command

Performs migrations for databases, APIs, or infrastructure.

## Usage

```
/sc:migrate <type> [flags]
```

## Arguments

- `type`: The type of migration to perform (`database`, `api`, `infrastructure`).

## Flags

- `--from <source>`: The source of the migration (e.g., a version number, a platform).
- `--to <target>`: The target of the migration.
- `--dry-run`: Show the proposed changes without applying them.
- `--persona-devops-architect`: Activate the DevOps architect agent.
- `--persona-backend-architect`: Activate the backend architect agent.

## Behavior

When you execute `/sc:migrate $ARGUMENTS`:

1.  **Parse Arguments**: Extract the migration type and flags from `$ARGUMENTS`.
2.  **Plan Migration**: Create a migration plan with a series of steps.
3.  **Activate Agents**: Engage the appropriate agents (`@agent-devops-architect`, `@agent-backend-architect`) to oversee the migration.
4.  **Execute Migration**: Execute the migration plan.
5.  **Verify Migration**: Run tests to ensure that the migration was successful.
6.  **Report Results**: Provide a summary of the migration results.

## Integration Points

-   **Agent Personas**: Activates `@agent-devops-architect` and `@agent-backend-architect` for expert guidance.
-   **Migration Tools**: Integrates with database migration tools (e.g., `alembic`, `flyway`) and infrastructure provisioning tools (e.g., `terraform`, `cloudformation`).

## Examples

```bash
# Migrate the database schema from v1 to v2
/sc:migrate database --from v1 --to v2

# Dry run an API migration
/sc:migrate api --from v1 --to v2 --dry-run

# Migrate infrastructure from AWS to GCP with the DevOps architect
/sc:migrate infrastructure --from aws --to gcp --persona-devops-architect
```

## Output Format

The command's output includes:
-   **Migration Plan**: The steps that will be taken to perform the migration.
-   **Migration Logs**: Real-time output from the migration tools.
-   **Status Message**: A final message indicating success or failure.
-   **Verification Results**: The results of the tests that were run to verify the migration.
