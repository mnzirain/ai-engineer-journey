import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from registry import AgentManager

manager = AgentManager()

agents = [

    "GreetingAgent",

    "CalculatorAgent",

    "MemoryAgent",

    "KnowledgeAgent"

]

for name in agents:

    print("=" * 40)

    print("Requested:", name)

    print("Returned:", manager.get_agent(name).name)