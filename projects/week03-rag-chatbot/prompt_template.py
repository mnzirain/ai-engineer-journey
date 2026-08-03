def build_prompt(question: str, context: str) -> str:
    """
    Build a prompt optimized for FLAN-T5.
    """

    return f"""Context:

{context}

Question:

{question}

Answer using only the context above.
If the answer is not in the context, say:

I could not find that information in the uploaded documents.

Answer:"""