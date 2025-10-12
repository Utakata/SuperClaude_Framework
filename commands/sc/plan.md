---
description: "Creates a project plan with tasks, milestones, and timelines."
---

# Plan Command

Creates a project plan for a new feature or project, including tasks, milestones, and timelines.

## Usage

```
/sc:plan <project-name> [flags]
```

## Arguments

- `project-name`: The name of the project or feature to plan.

## Flags

- `--template <name>`: Specify a project plan template to use.
- `--format <format>`: Specify the output format (`markdown`, `pdf`, `gantt`).
- `--team <members>`: Specify the team members to assign to the project (comma-separated).
- `--persona-requirements-analyst`: Activate the requirements analyst agent.

## Behavior

When you execute `/sc:plan $ARGUMENTS`:

1.  **Parse Arguments**: Extract the project name and planning flags from `$ARGUMENTS`.
2.  **Define Scope**: Work with the user to define the project's scope, goals, and deliverables.
3.  **Activate Agents**: Engage the `@agent-requirements-analyst` and `@agent-system-architect` to help with planning.
4.  **Create Tasks**: Break down the project into smaller, manageable tasks.
5.  **Estimate Effort**: Estimate the time and effort required for each task.
6.  **Generate Plan**: Generate the project plan in the specified format.

## Integration Points

-   **Agent Personas**: Activates `@agent-requirements-analyst`, `@agent-system-architect`, and `@agent-socratic-mentor` for expert planning assistance.
-   **Project Management Tools**: Can be integrated with project management tools like Jira and Trello.

## Examples

```bash
# Create a project plan for a new feature
/sc:plan "User Authentication"

# Use a template to create a project plan in PDF format
/sc:plan "E-commerce Website" --template "e-commerce" --format pdf

# Assign team members to a project
/sc:plan "Mobile App" --team "Alice,Bob,Charlie"
```

## Output Format

The command's output includes:
-   **Project Plan**: The generated project plan.
-   **Task List**: A list of tasks with estimates and assignments.
-   **Gantt Chart**: A Gantt chart showing the project timeline (if requested).
-   **Milestones**: A list of project milestones.
