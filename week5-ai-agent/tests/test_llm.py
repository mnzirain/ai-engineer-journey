import sys
from pathlib import Path

# Allow Python to find the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from llm import LLM

llm = LLM()

prompt = """
Answer this question briefly.

Question:
What is the capital city of France?
"""

print("Question:")
print(prompt)

print()

answer = llm.generate(prompt)

print("Answer:")
print(answer)