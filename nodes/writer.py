import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from state import GraphState

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-3.1-flash-lite',
    google_api_key=os.getenv('GOOGLE_API_KEY'),
    temperature=0.7
)

WRITER_PROMPT = """
You are an IELTS Writing Task 2 expert.

Write a Band 7+ IELTS essay.

Question:
{question}

Previous feedback:
{feedback}

Requirements:
- Introduction
- Body Paragraph 1
- Body Paragraph 2
- Conclusion

If feedback is empty, write a fresh essay.
Otherwise, improve the essay based on the feedback.
"""

def writer_node(state: GraphState):
    
    prompt = WRITER_PROMPT.format(
        question=state['user_prompt'],
        feedback=state['feedback']
    )
    
    response = llm.invoke(prompt)
    
    state['essay'] = response.content
    
    return state
