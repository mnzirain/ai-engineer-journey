import sys
from pathlib import Path

# Allow Python to find the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from registry import ToolRegistry

registry = ToolRegistry()

print()

calculator = registry.get_tool("calculator")
greeting = registry.get_tool("greeting")

print(calculator.execute("20 + 30"))
print(greeting.execute())