from state import GraphState

MAX_ATTEMPTS = 3

def router(state: GraphState) -> str:
    if state["decision"] == "PASS":
        return "pass"

    if state["attempt_count"] >= MAX_ATTEMPTS:
        return "pass"

    state["attempt_count"] += 1

    return "fail"