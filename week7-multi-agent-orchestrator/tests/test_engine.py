import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine import OrchestratorEngine

engine = OrchestratorEngine()

examples = [

    "Hello my name is Mike 20 + 30",

    "What is my name?",

]

for message in examples:

    print("=" * 50)

    print("User:", message)

    result = engine.run(message)

    print("Response:", result.response)