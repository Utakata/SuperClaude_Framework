---
description: "Facilitates brainstorming sessions for idea generation and requirement extraction."
---

# Brainstorm Command

Initiates a brainstorming session to explore ideas, extract requirements, and define project scope.

## Usage

```
/sc:brainstorm <topic> [flags]
```

## Arguments

- `topic`: The central topic or idea for the brainstorming session.

## Flags

- `--strategy <name>`: Define the brainstorming strategy (`systematic`, `agile`, `enterprise`).
- `--depth <level>`: Set the exploration depth (`shallow`, `normal`, `deep`).
- `--parallel`: Enable parallel exploration of different facets of the topic.
- `--persona-<type>`: Involve specific agents in the session (e.g., `architect`, `data`, `security`).

## Behavior

When you execute `/sc:brainstorm $ARGUMENTS`:

1.  **Parse Arguments**: Extract the topic and flags from `$ARGUMENTS`.
2.  **Establish Session Goal**: Clarify the objective of the brainstorming session (e.g., feature ideation, problem-solving).
3.  **Activate Agents**: Engage relevant personas to provide diverse perspectives.
4.  **Guide Discussion**: Use Socratic questioning and structured exploration to guide the conversation.
5.  **Synthesize Ideas**: Capture and organize the ideas generated during the session.
6.  **Generate Artifacts**: Produce mind maps, requirement lists, or initial design concepts.

## Integration Points

-   **Sequential MCP**: For structured, multi-step exploration of complex topics.
-   **Serena MCP**: For session management and context persistence across multiple interactions.
-   **Agent Personas**: Involves multiple agents like `@agent-architect`, `@agent-data`, `@agent-security` to provide a holistic view.

## Examples

```bash
# Brainstorm a new feature with a systematic approach
/sc:brainstorm "AI-powered code completion" --strategy systematic --depth deep

# Explore a topic with multiple agents in parallel
/sc:brainstorm "improving application security" --parallel --persona-security --persona-backend

# Brainstorm marketing ideas for a new product
/sc:brainstorm "marketing strategy for a new mobile app" --strategy agile
```

## Output Format

The command's output may include:
-   **Mind Map**: A visual representation of the ideas and their relationships.
-   **Requirement List**: A structured list of functional and non-functional requirements.
-   **Action Items**: A list of next steps and tasks.
-   **Session Transcript**: A record of the brainstorming session.
