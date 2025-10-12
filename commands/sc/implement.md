---
description: "Feature and code implementation with intelligent persona activation and MCP integration"
---

# Implement Command

Generates feature and code implementations with intelligent persona activation and MCP integration.

## Usage

```
/sc:implement <feature-description> [flags]
```

## Arguments

- `feature-description`: A description of the feature to implement

## Flags
- `--type`: Specify the implementation type (component, api, service, feature)
- `--framework`: Specify the framework to use (react, vue, express)
- `--safe`: Enable safe mode for the implementation
- `--with-tests`: Include tests with the implementation

## Behavior

When you execute `/sc:implement $ARGUMENTS`:

1. **Parse Arguments**: Extract feature description and flags from `$ARGUMENTS`
2. **Analyze Requirements**: Examine implementation requirements and detect technology context
3. **Plan Implementation**: Choose approach and activate relevant personas for domain expertise
4. **Generate Code**: Create implementation code with framework-specific best practices
5. **Validate and Test**: Apply security and quality validation throughout development
6. **Integrate and Document**: Update documentation and provide testing recommendations

## Integration Points

- **Context7 MCP**: Framework patterns and official documentation for React, Vue, Angular, Express
- **Magic MCP**: Auto-activated for UI component generation and design system integration
- **Sequential MCP**: Complex multi-step analysis and implementation planning
- **Playwright MCP**: Testing validation and quality assurance integration
- **Agent Personas**: Apply domain expertise (architect, frontend, backend, security, qa)

## Examples

```bash
# React Component Implementation
/sc:implement "user profile component" --type component --framework react

# API Service Implementation
/sc:implement "user authentication API" --type api --safe --with-tests

# Full-Stack Feature
/sc:implement "payment processing system" --type feature --with-tests

# Framework-Specific Implementation
/sc:implement "dashboard widget" --framework vue
```

## Output Format

Implementation results include:
- **Code**: The generated code for the feature
- **Tests**: The generated tests for the feature
- **Documentation**: The generated documentation for the feature
- **Validation Results**: The results of the security and quality validation
