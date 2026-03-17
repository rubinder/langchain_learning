from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display
from rich import print

class NumberState(TypedDict):
    number: int
    result: int

def abs_node(state: NumberState) -> NumberState:
    """If negative: take absolute value"""
    state["result"] = abs(state["number"])
    return state


def square_node(state: NumberState) -> NumberState:
    """If positive: square the number"""
    state["result"] = state["number"] ** 2
    return state


def zero_node(state: NumberState) -> NumberState:
    """If zero: leave as zero"""
    state["result"] = 0
    return state


def route_by_sign(state: NumberState) -> str:
    """Choose next node based on the sign of the number"""
    if state["number"] > 0:
        return "positive_branch"
    elif state["number"] < 0:
        return "negative_branch"
    else:
        return "zero_branch"


# Build the graph
graph = StateGraph(NumberState)

# Add our transformation nodes
graph.add_node("square_node", square_node)
graph.add_node("abs_node", abs_node)
graph.add_node("zero_node", zero_node)

# A passthrough router node
# graph.add_node("router", lambda s: s)


def passthrough_router(state):
    return state


graph.add_node("router", passthrough_router)

# Link start → router
graph.add_edge(START, "router")

# Conditional edges from router into each branch
graph.add_conditional_edges(
    "router",
    route_by_sign,
    {"positive_branch": "square_node", "negative_branch": "abs_node", "zero_branch": "zero_node"},
)

# All branches lead to END
graph.add_edge("square_node", END)
graph.add_edge("abs_node", END)
graph.add_edge("zero_node", END)

# Compile into an executable app
app = graph.compile()

graph_img = Image(app.get_graph().draw_mermaid_png())
display(graph_img)
# save the graph to a file
with open("../output/05-Conditional_Routing.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
# Mermaid is a popular diagramming syntax that can be rendered in many tools
with open("../output/05-Conditional_Routing.mmd", "w") as f:
    f.write(app.get_graph().draw_mermaid())

# Test it out:
for test_number in [5, -3, 0]:
    state: NumberState = {"number": test_number, "result": None}  # type: ignore
    out = app.invoke(state)
    print(f"Input: {test_number:>2} → Result: {out['result']}")