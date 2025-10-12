#!/bin/bash
# SuperClaude Plugin Integration Test Suite (File Structure Verification)

echo "🧪 Running SuperClaude Plugin Integration Tests (File Structure Verification)..."
EXIT_CODE=0

# Test 1: Plugin Manifest
echo "Test 1: Plugin Manifest Files"
if [ -f ".claude-plugin/plugin.json" ] && [ -f ".claude-plugin/marketplace.json" ]; then
    echo "  ✅ Plugin manifest files found"
else
    echo "  ❌ Plugin manifest files not found"
    EXIT_CODE=1
fi

# Test 2: Commands Directory
echo "Test 2: Commands Directory and Files"
if [ -d "commands" ] && [ -f "commands/implement.md" ] && [ -f "commands/design.md" ]; then
    echo "  ✅ Commands directory and key files found"
else
    echo "  ❌ Commands directory or key files not found"
    EXIT_CODE=1
fi

# Test 3: Agents Directory
echo "Test 3: Agents Directory and Files"
if [ -d "agents" ] && [ -f "agents/architect.md" ] && [ -f "agents/data.md" ]; then
    echo "  ✅ Agents directory and key files found"
else
    echo "  ❌ Agents directory or key files not found"
    EXIT_CODE=1
fi

# Test 4: MCP Configuration
echo "Test 4: MCP Configuration File"
if [ -f ".mcp.json" ]; then
    echo "  ✅ MCP configuration file found"
else
    echo "  ❌ MCP configuration file not found"
    EXIT_CODE=1
fi

# Test 5: Hooks Configuration
echo "Test 5: Hooks Configuration File"
if [ -f "hooks/hooks.json" ]; then
    echo "  ✅ Hooks configuration file found"
else
    echo "  ❌ Hooks configuration file not found"
    EXIT_CODE=1
fi

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo "🎉 All file structure integration tests passed!"
    exit 0
else
    echo "🔥 Some file structure integration tests failed."
    exit 1
fi
