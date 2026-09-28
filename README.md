# genpark-lu-decomposition-partial-pivoting-skill

[![GitHub Stars](https://img.shields.io/github/stars/alphaparkinc/genpark-lu-decomposition-partial-pivoting-skill?style=social)](https://github.com/alphaparkinc/genpark-lu-decomposition-partial-pivoting-skill)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-0%20(pure%20standard%20library)-brightgreen.svg)](client.py)
[![MCP Ready](https://img.shields.io/badge/MCP-Ready-purple.svg)](mcp_server.py)

> **Gaussian elimination with row partial pivoting (PLU decomposition) and linear system solver**

Part of the **GenPark Autonomous Agent Matrix**, developed for production AI agents operating across numerical, financial, and scientific computing stacks.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[Matrix / Linear System Inputs] --> B[genpark-lu-decomposition-partial-pivoting-skill]
    B --> C[Pure Python Standard Library Numerical Engine]
    C --> D[Decomposed Matrices / Eigenvalues / Solution Vector]
    B --> E[MCP Protocol Endpoint stdio]
    E --> F[Cursor / Claude Desktop / Windsurf Integration]
```

## 🚀 Quickstart

### Native Python Execution
```bash
python example_usage.py
```

### Standard Library Verification
```python
from client import *
```

### MCP Server (Claude Desktop / Cursor)
```json
{
  "mcpServers": {
    "genpark-lu-decomposition-partial-pivoting-skill": {
      "command": "python",
      "args": ["-m", "genpark_lu_decomposition_partial_pivoting_skill.mcp_server"]
    }
  }
}
```

## 📄 License
MIT License.
