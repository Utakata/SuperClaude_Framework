---
description: Comprehensive code and architecture analysis with multi-dimensional insights
---

# Analyze Command

Performs deep analysis of code, architecture, security, and performance aspects using Sequential MCP for multi-step reasoning.

## Usage

```
/sc:analyze <target> [flags]
```

## Arguments

- `target`: File, directory, or project to analyze

## Flags

- `--code`: Focus on code quality and structure
- `--architecture`: Analyze system architecture and design patterns
- `--security`: Security vulnerability assessment
- `--performance`: Performance bottleneck identification
- `--persona-<type>`: Apply specialized agent perspective
- `--seq`: Enable Sequential MCP for complex reasoning
- `--c7`: Enable Context7 for documentation lookup
- `--uc`: Ultra-compressed output mode

## Behavior

When you execute `/sc:analyze $ARGUMENTS`:

1. **Parse Arguments**: Extract target and flags from `$ARGUMENTS`
2. **Select Analysis Mode**: Determine analysis focus (code/architecture/security/performance)
3. **Activate Tools**:
   - Sequential MCP for multi-step analysis
   - Context7 MCP if framework detected
   - Appropriate persona agent based on focus
4. **Execute Analysis**:
   - Structural analysis (components, dependencies, patterns)
   - Quality metrics (complexity, maintainability, test coverage)
   - Security assessment (vulnerabilities, compliance)
   - Performance profiling (bottlenecks, optimization opportunities)
5. **Generate Report**: Structured findings with actionable recommendations

## Integration Points

- **Sequential MCP**: Multi-step reasoning for complex analysis
- **Context7 MCP**: Framework-specific best practices lookup
- **Agent Personas**: Apply domain expertise (architect, security, performance)
- **Rules**: Evidence-based methodology (RULES.md)

## Examples

```bash
# Basic code analysis
/sc:analyze src/auth.py

# Architecture deep-dive with Sequential MCP
/sc:analyze project/ --architecture --seq

# Security audit with security persona
/sc:analyze app/ --security --persona-security

# Comprehensive analysis (all dimensions)
/sc:analyze . --code --architecture --security --performance
```

## Output Format

Analysis results include:
- **Summary**: High-level findings and severity levels
- **Detailed Findings**: Categorized issues with evidence
- **Metrics**: Quantitative measures (complexity, coverage, etc.)
- **Recommendations**: Prioritized action items
- **References**: Links to relevant documentation (via Context7)
