import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from registry import AgentManager


manager = AgentManager()

print("=" * 40)
print("Discovered Agents")
print("=" * 40)

for agent in manager.list_agents():
    print(agent)