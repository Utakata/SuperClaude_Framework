<div align="center">

# 📦 SuperClaude Installation Guide

<p align="center">
  <img src="https://img.shields.io/badge/version-4.1.6-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20|%20macOS%20|%20Windows-orange?style=for-the-badge" alt="Platform">
</p>


</div>

---

## 🚀 **Installation**

### **Stable Release (Recommended)**

Install the latest stable version of SuperClaude from PyPI:

```bash
pip install superclaude
```

This is the recommended method for most users.

### **Development Setup**

If you plan to contribute to the project, you should install it in editable mode from a local clone of the repository.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
    cd SuperClaude_Framework
    ```

2.  **Install with development dependencies:**
    ```bash
    make install
    ```
    This command uses `uv` to create a virtual environment and install the package in editable mode (`-e`) along with all dependencies required for testing and development.

## ✅ **Verification**

To verify that the installation was successful, you can run the built-in health check:

```bash
make verify
```

This command will run a series of checks to ensure that the CLI is working and the pytest plugin is correctly installed and discoverable.

You can also run the test suite to ensure everything is functioning as expected:

```bash
make test
```

---

## 🔧 **Troubleshooting**

<details>
<summary><b>Virtual Environment Issues</b></summary>

If you encounter issues with `make install` or `make verify`, ensure your virtual environment is set up correctly. You can manually create and manage it:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # On Linux/macOS
# .\.venv\Scripts\activate  # On Windows

# Install in editable mode
pip install -e ".[dev]"
```

</details>

<details>
<summary><b>`make` command not found</b></summary>

If the `make` command is not available on your system (common on Windows):

- **Windows**: You may need to install `make` through a package manager like Chocolatey (`choco install make`) or use the commands from the `Makefile` directly (e.g., `uv pip install -e ".[dev]"` instead of `make install`).
- **Linux/macOS**: Ensure build-essential tools are installed. For Debian/Ubuntu, use `sudo apt-get install build-essential`.

</details>

<details>
<summary><b>Missing Python or pip</b></summary>

Ensure you have Python 3.10+ and pip installed.

- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update
  sudo apt install python3.10 python3-pip python3.10-venv
  ```
- **macOS:**
  ```bash
  brew install python@3.10
  ```
- **Windows:**
  - Download from [python.org](https://python.org).
  - Make sure to check "Add Python to PATH" during installation.

</details>

---

## 📚 **Next Steps**

After successfully installing the framework, a good next step is to explore the available agents and commands.

<div align="center">

### **Explore the Framework**

<table>
<tr>
<th>🌱 Start Here</th>
<th>🌿 Expand Skills</th>
<th>🌲 Master Framework</th>
</tr>
<tr>
<td valign="top">

**First Steps:**
- Read the main [**README.md**](../../README.md) for an overview.
- Explore the [**`docs`**](../../docs) directory for detailed documentation.

</td>
<td valign="top">

**Core Components:**
- Learn about the available [**Agents**](../user-guide/agents.md).
- Understand the different [**Behavioral Modes**](../user-guide/modes.md).

</td>
<td valign="top">

**For Contributors:**
- Review the [**Technical Architecture**](../developer-guide/technical-architecture.md).
- Read the [**Contributing Guide**](../../CONTRIBUTING.md).

</td>
</tr>
</table>

</div>