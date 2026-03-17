from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

class AgentState(TypedDict):  # Our state schema
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""

    state["message"] = "Hey " + state["message"] + ", how is your day going?"

    return state

graph = StateGraph(AgentState)

graph.set_entry_point("greeter")

graph.add_node("greeter", greeting_node)

graph.set_finish_point("greeter")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

# save the graph to a file
with open("output/03-Graph_Basics.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

result = app.invoke({"message": "Bob"})

result["message"]
