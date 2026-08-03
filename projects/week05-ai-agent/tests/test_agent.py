import sys
from pathlib import Path

# Allow Python to find the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from agent import AIAgent

agent = AIAgent()

tests = [
    "Hello",
    "My name is Mike",
    "What is my name?",
    "20 + 30",
    "calculate 12 * 8",
    "What is Artificial Intelligence?",
]

print()

for question in tests:

    print("=" * 60)

    print("User:", question)

    answer = agent.chat(question)

    print("Agent:", answer)

    print()