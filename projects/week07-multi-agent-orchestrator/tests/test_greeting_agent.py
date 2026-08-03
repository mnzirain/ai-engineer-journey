import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from engine import OrchestratorEngine

engine = OrchestratorEngine()

examples = [

    "Hello",

    "20 + 30"

]

for message in examples:

    print("=" * 50)

    print("User:", message)

    result = engine.run(message)

    print("Response:", result.response)