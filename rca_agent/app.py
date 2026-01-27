from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from rca_agent.schemas import RCARequest, RCAResponse
from rca_agent.graph import rca_graph

app = FastAPI(title="RCA LangGraph Agent")


@app.post("/rca", response_model=RCAResponse)
async def get_rca(req: RCARequest):
    initial_state = {
        "query": req.error,
        "context": "",
        "answer": "",
        "retries": 0
    }

    result = await run_in_threadpool(rca_graph.invoke, initial_state)
    return {"result": result["answer"]}
