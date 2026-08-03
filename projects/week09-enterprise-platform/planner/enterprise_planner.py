def enterprise_planner(state):

    message = state["messages"][-1].content.lower()

    print(f"Planner received: {message}")

    if "remember" in message or "my name" in message:
        route = "memory"

    elif "translate" in message:
        route = "translation"

    elif any(symbol in message for symbol in ["+", "-", "*", "/"]):
        route = "calculator"

    elif any(word in message for word in ["hello", "hi", "hey"]):
        route = "greeting"

    else:
        route = "knowledge"

    print(f"Selected workflow: {route}")

    return {
        "route": route
    }