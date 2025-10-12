---
description: "Reviews code in pull requests and commits."
---

# Review Command

Reviews code for quality, correctness, and adherence to best practices in pull requests and commits.

## Usage

```
/sc:review <target> [flags]
```

## Arguments

- `target`: The pull request URL, commit hash, or file/directory to review.

## Flags

- `--level <level>`: Specify the review level (`light`, `medium`, `deep`).
- `--focus <area>`: Specify the review focus (`security`, `performance`, `style`, `logic`).
- `--auto-apply`: Automatically apply suggested changes.
- `--persona-qa`: Activate the QA specialist agent.
- `--persona-security`: Activate the security engineer agent.

## Behavior

When you execute `/sc:review $ARGUMENTS`:

1.  **Parse Arguments**: Extract the target and review flags from `$ARGUMENTS`.
2.  **Fetch Code**: Fetch the code to be reviewed from the specified source.
3.  **Analyze Code**: Analyze the code for potential issues based on the specified focus.
4.  **Activate Agents**: Engage the appropriate agents (`@agent-qa`, `@agent-security`) to provide expert feedback.
5.  **Generate Feedback**: Generate a review with comments, suggestions, and code snippets.
6.  **Apply Changes (if specified)**: If `--auto-apply` is present, apply the suggested changes to the code.

## Integration Points

-   **Agent Personas**: Activates `@agent-qa`, `@agent-security`, and other relevant agents.
-   **Version Control Systems**: Integrates with Git to review pull requests and commits.

## Examples

```bash
# Perform a deep review of a pull request
/sc:review https://github.com/org/repo/pull/123 --level deep

# Review a commit with a focus on security
/sc:review a1b2c3d4 --focus security --persona-security

# Automatically apply style suggestions to a directory
/sc:review src/ --focus style --auto-apply
```

## Output Format

The command's output includes:
-   **Review Summary**: A summary of the review findings.
-   **Feedback List**: A list of comments and suggestions.
-   **Code Snippets**: Code snippets with suggested changes.
-   **Action Items**: A list of action items for the author.
