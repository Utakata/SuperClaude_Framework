---
description: "Extracts data from a file, string, or URL."
---

# Extract Command

Extracts data from a file, string, or URL using a regular expression or a JSON path.

## Usage

```
/sc:extract <source> [flags]
```

## Arguments

- `source`: The source to extract data from (a file path, a string, or a URL).

## Flags

- `--pattern <regex>`: A regular expression to use for extraction.
- `--json-path <path>`: A JSON path to use for extraction.
- `--file <path>`: The file to extract from.
- `--url <url>`: The URL to extract from.
- `--persona-data-engineer`: Activate the data engineer agent.

## Behavior

When you execute `/sc:extract $ARGUMENTS`:

1.  **Parse Arguments**: Extract the source and extraction flags from `$ARGUMENTS`.
2.  **Read Content**: Read the content from the specified source.
3.  **Activate Agents**: Engage the `@agent-data-engineer` to perform the extraction.
4.  **Extract Data**: Extract the data using the specified pattern or path.
5.  **Format Output**: Format the extracted data as a list or a table.

## Integration Points

-   **Agent Personas**: Activates `@agent-data-engineer` for expert data extraction.
-   **Regular Expression Engines**: Integrates with regular expression engines to perform pattern matching.
-   **JSON Path Libraries**: Integrates with JSON path libraries to extract data from JSON objects.

## Examples

```bash
# Extract all email addresses from a file
/sc:extract --file contacts.txt --pattern "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"

# Extract the value of a key from a JSON file
/sc:extract --file data.json --json-path "$.name"

# Extract all links from a URL
/sc:extract --url https://example.com --pattern "<a href=\\"(.*?)\\""
```

## Output Format

The command's output includes:
-   **Extracted Data**: The data that was extracted.
-   **Match Count**: The number of matches that were found.
-   **Source**: The source from which the data was extracted.
