🚀 RCA Agent – Agentic Root Cause Analysis System (LangGraph + RAG)

An AI-powered Root Cause Analysis (RCA) Agent built using LangGraph, LangChain, ChromaDB, and FastAPI.
The system analyzes system or application errors and automatically generates Root Cause, Impact, and Fix recommendations using Retrieval-Augmented Generation (RAG).

This project demonstrates real-world GenAI engineering, including agent orchestration, stateful workflows, vector search, and API-based integration.

📌 Problem Statement

In large-scale and distributed systems, identifying the true root cause of failures is often:

• Time-consuming
• Dependent on manual log analysis
• Prone to human error

Traditional monitoring and alerting tools typically:
• Show what failed
• But rarely explain why it failed or how to fix it

As systems grow in complexity, this gap becomes a major bottleneck for SRE and DevOps teams.

💡 Solution Overview

This project addresses the problem by building an intelligent, agentic RCA system that:

• Understands error descriptions in natural language
• Retrieves relevant historical incidents and logs using semantic search
• Reasons over retrieved context using an LLM
• Produces structured, human-readable RCA insights

The result is a production-style AI agent that assists engineers in faster and more reliable incident analysis.

✅ What This Project Does

• Accepts system or application error descriptions as input
• Retrieves semantically similar historical incidents using ChromaDB
• Uses an LLM to generate:
– Root Cause
– Impact
– Recommended Fix
• Validates output quality and retries when responses are insufficient
• Exposes results through a FastAPI REST endpoint for easy integration

🧠 System Architecture (High Level)

User / UI
↓
FastAPI REST Endpoint
↓
LangGraph Agent Workflow
• Retrieval (ChromaDB + Embeddings)
• Reasoning (LLM)
• Validation
• Retry Logic
↓
Structured RCA Response (JSON)

🧩 Key Components

• LangGraph for stateful, graph-based agent orchestration
• LangChain for retrieval and LLM coordination
• ChromaDB for vector-based semantic search over incident logs
• FastAPI for exposing the RCA agent as a production-ready API
• Retry & validation logic to ensure response quality

🎯 Use Cases

• Incident root cause analysis for SRE teams
• Faster debugging of production failures
• AI-assisted log and incident investigation
• Prototyping self-healing or autonomous ops systems
• Demonstrating agentic GenAI patterns in real-world scenarios

🌟 Project Highlights

• Agentic, state-driven workflow using LangGraph
• Retrieval-Augmented Generation for grounded reasoning
• Automatic validation and retry mechanism
• Clean API-first design for UI or tool integration
• Production-oriented architecture

🏁 Summary

This project showcases how agentic AI systems can be applied to real operational problems.
By combining retrieval, reasoning, and structured workflows, the RCA Agent demonstrates a scalable approach to building intelligent systems for incident analysis and decision support.
