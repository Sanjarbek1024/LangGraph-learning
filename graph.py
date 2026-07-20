from langgraph.graph import StateGraph, START, END

from state import GraphState
from nodes.writer import writer_node
from nodes.checker import checker_node
from nodes.router import router


graph_builder = StateGraph(GraphState)

# Nodes
graph_builder.add_node("writer", writer_node)
graph_builder.add_node("checker", checker_node)

# Edges
graph_builder.add_edge(START, "writer")
graph_builder.add_edge("writer", "checker")

graph_builder.add_conditional_edges(
    "checker",
    router,
    {
        "pass": END,
        "fail": "writer",
    },
)

graph = graph_builder.compile()