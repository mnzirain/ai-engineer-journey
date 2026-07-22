import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from engine import WorkflowEngine

engine = WorkflowEngine()

conversation = [

    "Hello",

    "My name is Mike",

    "What is my name?",

    "20 + 30",

    "What is my name?",

]

for message in conversation:

    print()

    print("=" * 60)

    print("User:", message)

    state = engine.run(message)

    print()

    print("Memory:", state.memory)

    print("Response:", state.response)