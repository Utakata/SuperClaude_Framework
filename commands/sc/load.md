---
description: "Loads data into a destination, such as a database or a file."
---

# Load Command

Loads data into a destination, such as a database, a file, or a data warehouse.

## Usage

```
/sc:load <source> [flags]
```

## Arguments

- `source`: The data to load (a file path or a string).

## Flags

- `--to <destination>`: The destination to load the data into.
- `--table <table>`: The table to load the data into (for databases).
- `--file <path>`: The file to load the data from.
- `--append`: Append the data to the destination instead of overwriting.
- `--persona-data-engineer`: Activate the data engineer agent.

## Behavior

When you execute `/sc:load $ARGUMENTS`:

1.  **Parse Arguments**: Extract the source and loading flags from `$ARGUMENTS`.
2.  **Read Data**: Read the data from the specified source.
3.  **Activate Agents**: Engage the `@agent-data-engineer` to perform the loading operation.
4.  **Load Data**: Load the data into the specified destination.
5.  **Verify Load**: Verify that the data was loaded correctly.
6.  **Report Results**: Provide a summary of the loading operation.

## Integration Points

-   **Agent Personas**: Activates `@agent-data-engineer` for expert data loading.
-   **Database Connectors**: Integrates with database connectors to load data into databases.
-   **File I/O Libraries**: Integrates with file I/O libraries to load data into files.

## Examples

```bash
# Load data from a CSV file into a PostgreSQL database
/sc:load --file data.csv --to "postgresql://user:pass@host:port/db" --table users

# Append data from a JSON file to another file
/sc:load --file data.json --to output.json --append

# Load a string into a variable
/sc:load "Hello, World!" --to my_variable
```

## Output Format

The command's output includes:
-   **Status Message**: A message indicating whether the data was loaded successfully.
-   **Record Count**: The number of records that were loaded.
-   **Destination**: The destination where the data was loaded.
