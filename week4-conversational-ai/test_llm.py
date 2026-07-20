from llm import LLM

llm = LLM()

question = """
Translate the following sentence into French:

Hello, how are you today?
"""

answer = llm.generate(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)