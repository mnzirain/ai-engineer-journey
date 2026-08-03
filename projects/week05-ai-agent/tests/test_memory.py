import sys
from pathlib import Path

# Allow Python to find the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from memory import AgentMemory

memory = AgentMemory()

memory.remember_name("My name is Mike")

print(memory.get_name())