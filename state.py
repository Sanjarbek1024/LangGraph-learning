from typing import TypedDict, Literal

class GraphState(TypedDict):
    user_prompt: str
    essay: str
    feedback: str
    attempt_count: 1
    decision: Literal['PASS', 'FAIL']
