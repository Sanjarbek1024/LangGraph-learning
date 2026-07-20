import os
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

from state import GraphState

load_dotenv()


class CheckerResponse(BaseModel):
    decision: Literal["PASS", "FAIL"]
    feedback: str


llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)

structured_llm = llm.with_structured_output(CheckerResponse)

CHECKER_PROMPT = """
You are an official IELTS Writing Task 2 examiner.

Evaluate the essay based on the official IELTS Band Descriptors.

Question:
{question}

Essay:
{essay}

Evaluate the following criteria:

1. Task Response
2. Coherence and Cohesion
3. Lexical Resource
4. Grammatical Range and Accuracy

Instructions:

Return PASS only if ALL of the following are true:

- Estimated IELTS Band >= 7.0
- Grammar contains no major errors
- Vocabulary is appropriate for Band 7+
- The essay fully addresses the question
- The essay has clear coherence and cohesion

Otherwise return FAIL.

- Give detailed feedback explaining exactly what should be improved.
"""


def checker_node(state: GraphState) -> GraphState:
    prompt = CHECKER_PROMPT.format(
        question=state["user_prompt"],
        essay=state["essay"],
    )

    result = structured_llm.invoke(prompt)

    state["decision"] = result.decision
    state["feedback"] = result.feedback

    return state