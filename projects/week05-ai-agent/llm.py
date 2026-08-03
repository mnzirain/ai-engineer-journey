from llms.huggingface import HuggingFaceLLM


def get_llm():
    """
    Returns the configured language model.

    In the future this function can switch between:
    - Hugging Face
    - OpenAI
    - Ollama
    - Azure OpenAI
    """

    return HuggingFaceLLM()