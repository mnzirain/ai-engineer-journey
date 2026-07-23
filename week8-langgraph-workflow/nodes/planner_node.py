def planner_node(state):

    print("Planner Node Executed")

    message = state["messages"][-1].content.lower()

    if any(word in message for word in ["hello", "hi", "hey"]):

        route = "greeting"

    elif any(symbol in message for symbol in ["+", "-", "*", "/"]):

        route = "calculator"

    elif "remember" in message or "my name" in message:

        route = "memory"

    else:

        route = "knowledge"

    return {

        "route": route

    }