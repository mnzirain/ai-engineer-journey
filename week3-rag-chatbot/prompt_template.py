"""
Prompt templates for the RAG chatbot.
"""


def build_prompt(question: str, context: str) -> str:
    """
    Build the prompt sent to the language model.
    """

    return f"""
You are an AI assistant.

Answer the user's question using ONLY the information provided below.

If the answer cannot be found in the provided information, reply:

"I cannot find the answer in the supplied document."

------------------------
DOCUMENT
------------------------

{context}

------------------------
QUESTION
------------------------

{question}

------------------------
ANSWER
------------------------
"""