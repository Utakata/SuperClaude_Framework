---
description: "Design support for system architecture and APIs"
---

# Design Command

Provides design support for system architecture, APIs, and components.

## Usage

```
/sc:design <target> [flags]
```

## Arguments

- `target`: The subject of the design (e.g., "user authentication API", "scalable e-commerce platform")

## Flags

- `--type`: Specify the design type (architecture, api, component, database)
- `--format`: Define the output format (diagram, spec, code)
- `--persona-architect`: Apply the System Architect persona
- `--seq`: Enable Sequential MCP for complex design reasoning

## Behavior

When you execute `/sc:design $ARGUMENTS`:

1. **Parse Arguments**: Extract the design target and flags from `$ARGUMENTS`.
2. **Analyze Requirements**: Gather functional and non-functional requirements for the design.
3. **Activate Tools**:
   - Activate the `@agent-architect` for architectural design.
   - Use Sequential MCP for complex planning and trade-off analysis.
4. **Generate Design Artifacts**:
   - Create architecture diagrams (e.g., using Mermaid).
   - Generate API specifications.
   - Outline component structures.
5. **Present Options**: Propose multiple design options with trade-off analysis.

## Integration Points

- **Sequential MCP**: For multi-step reasoning in complex design tasks.
- **Agent Personas**: Primarily `@agent-architect`, but also `@agent-backend` or `@agent-frontend` depending on the `--type`.
- **Principles**: Adheres to SOLID, DRY, KISS from `PRINCIPLES.md`.

## Examples

```bash
# Design a system architecture
/sc:design "scalable e-commerce platform" --type architecture

# Design a REST API
/sc:design "user management API" --type api --format spec

# Design a component with the architect persona
/sc:design "real-time notification component" --type component --persona-architect
```

## Output Format

Design results may include:
- **Architecture Diagrams**: Mermaid diagrams.
- **API Specifications**: OpenAPI/Swagger specs.
- **Component Specifications**: Descriptions of component responsibilities and interfaces.
- **Trade-off Analysis**: Pros and cons of different design choices.
- **Implementation Roadmap**: A high-level plan for implementing the design.
