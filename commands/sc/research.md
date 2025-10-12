---
description: "Performs deep research with up to 5 hops."
---

# Research Command

Performs deep research on a topic, with the ability to follow up to 5 hops of references.

## Usage

```
/sc:research <topic> [flags]
```

## Arguments

- `topic`: The topic to research.

## Flags

- `--depth <hops>`: Specify the number of hops for the research (1-5).
- `--sources <sources>`: Specify the sources to use (e.g., `web`, `docs`, `articles`).
- `--format <format>`: Specify the output format (e.g., `summary`, `report`, `list`).
- `--persona-learning-guide`: Activate the learning guide agent.

## Behavior

When you execute `/sc:research $ARGUMENTS`:

1.  **Parse Arguments**: Extract the topic and research flags from `$ARGUMENTS`.
2.  **Initial Search**: Perform an initial search on the topic.
3.  **Hop and Gather**: Follow references and gather information up to the specified depth.
4.  **Synthesize Information**: Synthesize the gathered information into a coherent response.
5.  **Format Output**: Format the response according to the specified format.

## Integration Points

-   **Tavily MCP**: For web search capabilities.
-   **Firecrawl MCP**: For web scraping and content extraction.
-   **Agent Personas**: Activates `@agent-learning-guide` to structure the research process.

## Examples

```bash
# Perform a deep research on a topic
/sc:research "serverless architecture" --depth 3

# Research a topic using specific sources
/sc:research "React hooks" --sources "web,docs"

# Get a summary of a topic
/sc:research "JWT authentication" --format summary
```

## Output Format

The command's output includes:
-   **Summary**: A summary of the research findings.
-   **Detailed Report**: A detailed report with references and sources.
-   **List of Links**: A list of relevant links.
-   **Key Concepts**: A list of key concepts and definitions.
