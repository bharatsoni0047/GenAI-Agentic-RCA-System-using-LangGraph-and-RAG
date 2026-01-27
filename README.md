🚀 RCA Agent – LangGraph-Based Root Cause Analysis System

An AI-powered Root Cause Analysis (RCA) Agent built using LangGraph, LangChain, ChromaDB, and FastAPI, designed to analyze system/application errors and generate clear root cause, impact, and fix recommendations using Retrieval Augmented Generation (RAG).

This project demonstrates real-world GenAI engineering, including agent orchestration, vector search, and API integration.

Problem Statement:-

In large-scale systems, identifying the root cause of errors from logs and historical incidents is time-consuming and error-prone.

Traditional monitoring tools::-
--Show what failed
--But rarely explain why it failed or how to fix it

This project solves that by building an intelligent RCA agent that:

--Understands error context
--Searches historical incident data
--Generates human-readable RCA insights

✅ What This Project Does:-

Accepts a system/application error description as input
Retrieves semantically similar historical incidents using a vector database
Uses an LLM to generate:
Root Cause
Impact



User / UI
   |
   |  (POST /rca)
   v
FastAPI
   |
   v
LangGraph Agent
   ├── Retrieval (ChromaDB + Embeddings)
   ├── Reasoning (LLM)
   ├── Validation
   └── Retry Logic
   |
   v
RCA Response (JSON)

Recommended Fix

Returns results via a FastAPI REST endpoint for easy UI or tool integration
