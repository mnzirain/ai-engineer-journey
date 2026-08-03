import sys
from pathlib import Path

# Allow Python to find the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools import CalculatorTool, GreetingTool

calculator = CalculatorTool()
greeting = GreetingTool()

print()

print("Calculator Test")
print("----------------")
print(calculator.execute("20 + 30"))
print(calculator.execute("12 * 8"))
print(calculator.execute("100 / 5"))

print()

print("Greeting Test")
print("-------------")
print(greeting.execute())