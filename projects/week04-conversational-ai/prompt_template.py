def build_prompt(history, user_message):
    """
    Build a prompt containing the conversation history.
    """

    prompt = (
        "You are a friendly AI assistant.\n"
        "Use the previous conversation to answer naturally.\n\n"
    )

    for message in history:

        if message["role"] == "user":
            prompt += f"User: {message['content']}\n"

        else:
            prompt += f"Assistant: {message['content']}\n"

    prompt += f"\nUser: {user_message}\n"
    prompt += "Assistant:"

    return prompt