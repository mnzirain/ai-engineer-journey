import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from router import Router

router = Router()

plans = [
    ["greeting"],
    ["calculator"],
    ["memory_store"],
    ["memory_retrieve"],
    ["knowledge"]
]

for plan in plans:

    print("=" * 40)
    print("Plan:", plan)
    print("Agent:", router.route(plan))