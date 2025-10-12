---
description: "Explains code in plain English."
---

# Explain Command

Explains a piece of code, a concept, or a file in a clear and concise way.

## Usage

```
/sc:explain <topic> [flags]
```

## Arguments

- `topic`: The topic to explain (e.g., a concept, a file path, or a code snippet).

## Flags

- `--level <level>`: The level of detail for the explanation (`simple`, `detailed`, `expert`).
- `--file <path>`: The file to explain.
- `--code <snippet>`: The code snippet to explain.
- `--persona-learning-guide`: Activate the learning guide agent.

## Behavior

When you execute `/sc:explain $ARGUMENTS`:

1.  **Parse Arguments**: Extract the topic and explanation flags from `$ARGUMENTS`.
2.  **Analyze Topic**: Analyze the topic to be explained.
3.  **Activate Agents**: Engage the `@agent-learning-guide` to provide a clear and concise explanation.
4.  **Generate Explanation**: Generate an explanation tailored to the specified level of detail.
5.  **Format Output**: Format the explanation with examples, analogies, and visuals.

## Integration Points

-   **Agent Personas**: Primarily activates `@agent-learning-guide` for educational explanations.
-   **Code Analysis Tools**: Integrates with code analysis tools to understand the code being explained.

## Examples

```bash
# Explain a concept in simple terms
/sc:explain "React hooks" --level simple

# Provide a detailed explanation of a file
/sc:explain src/auth.js --level detailed

# Explain a code snippet
/sc:explain --code "const [count, setCount] = useState(0);"
```

## Output Format

The command's output includes:
-   **Explanation**: The explanation of the topic.
-   **Code Examples**: Code examples to illustrate the concept.
-   **Analogies**: Analogies to help understand the concept.
-   **Visuals**: Diagrams and charts to visualize the concept.
