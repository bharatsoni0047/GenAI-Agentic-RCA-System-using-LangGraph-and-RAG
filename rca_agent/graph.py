from typing import TypedDict

from langgraph.graph import StateGraph, END

from rca_agent.retriever import get_retriever
from rca_agent.config import llm


class RCAState(TypedDict):
    query: str
    context: str
    answer: str
    retries: int


retriever = get_retriever()


# STEP 1: Retrieve documents
def retrieve_docs(state: RCAState):
    docs = docs = retriever.invoke(state["query"])
    context = "\n".join(d.page_content for d in docs)
    return {
        **state,
        "context": context
    }


# STEP 2: Generate RCA using LLM
def generate_rca(state: RCAState):
    prompt = f"""
You are an expert Site Reliability Engineer.

Context:
{state["context"]}

Error:
{state["query"]}

Provide:
1. Root Cause
2. Impact
3. Fix
"""
    response = llm.invoke(prompt)
    answer = response.content if hasattr(response, "content") else str(response)

    return {
        **state,
        "answer": answer
    }


# STEP 3: Validate output
def validate(state: RCAState):
    if len(state["answer"]) < 100 and state["retries"] < 2:
        return "retry"
    return "done"


# STEP 4: Retry handler
def retry(state: RCAState):
    return {
        **state,
        "retries": state["retries"] + 1
    }


# BUILD LANGGRAPH
graph = StateGraph(RCAState)

graph.add_node("retrieve", retrieve_docs)
graph.add_node("generate", generate_rca)
graph.add_node("retry", retry)

graph.set_entry_point("retrieve")

graph.add_edge("retrieve", "generate")
graph.add_conditional_edges(
    "generate",
    validate,
    {
        "retry": "retry",
        "done": END
    }
)
graph.add_edge("retry", "retrieve")

rca_graph = graph.compile()
