---
description: "Transforms data from one format to another."
---

# Transform Command

Transforms data from one format to another, such as CSV to JSON, or XML to YAML.

## Usage

```
/sc:transform <source> [flags]
```

## Arguments

- `source`: The data to transform (a file path or a string).

## Flags

- `--from <format>`: The source format of the data.
- `--to <format>`: The target format for the data.
- `--file <path>`: The file to transform.
- `--output <path>`: The file to write the transformed data to.
- `--persona-data-engineer`: Activate the data engineer agent.

## Behavior

When you execute `/sc:transform $ARGUMENTS`:

1.  **Parse Arguments**: Extract the source and transformation flags from `$ARGUMENTS`.
2.  **Read Data**: Read the data from the specified source.
3.  **Activate Agents**: Engage the `@agent-data-engineer` to perform the transformation.
4.  **Transform Data**: Transform the data from the source format to the target format.
5.  **Write Data**: Write the transformed data to the specified output file or to the console.

## Integration Points

-   **Agent Personas**: Activates `@agent-data-engineer` for expert data transformation.
-   **Data Transformation Libraries**: Integrates with data transformation libraries and tools.

## Examples

```bash
# Transform a CSV file to JSON
/sc:transform --file data.csv --from csv --to json --output data.json

# Transform an XML string to YAML
/sc:transform "<person><name>John</name></person>" --from xml --to yaml

# Transform a file to JSON and output to the console
/sc:transform data.xml --to json
```

## Output Format

The command's output includes:
-   **Transformed Data**: The data in the target format.
-   **Status Message**: A message indicating whether the transformation was successful.
-   **Output Path**: The path to the output file (if specified).
