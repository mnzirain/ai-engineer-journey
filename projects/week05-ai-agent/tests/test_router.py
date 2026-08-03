import sys
from pathlib import Path

# Allow Python to find the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from router import Router

router = Router()

tests = [
    "Hello",
    "Hi",
    "25 + 18",
    "100 / 4",
    "Who invented Python?",
    "Explain recursion.",
]

print()

for message in tests:

    tool = router.route(message)

    print(f"{message:<25} -> {tool}")