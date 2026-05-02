# Hybrid AI System (LLM + RAG + API + Router)

## What this is

This project is not just a chatbot.

It is a **hybrid AI system** that dynamically decides how to respond using:

* **LLM** → for reasoning and natural language generation
* **RAG** → for grounded, document-based answers
* **API Layer** → for executing actions / returning structured data
* **Router** → for selecting the correct pathway

---

## Why this matters

Most student projects:

* Use only an LLM
* Or only a document chatbot

This system demonstrates how **real-world AI assistants are built**:

> A decision-based architecture that routes queries to the right intelligence source.

---

## System Architecture

```text id="arch1"
User → UI → FastAPI Backend
                ↓
             Router
      ┌────────┼────────┐
      ↓        ↓        ↓
     RAG      API      LLM
      ↓        ↓        ↓
   Context   Data    Reasoning
      ↓        ↓        ↓
        Final Response
```

---

## How it works

### 1. User Query

User sends input through UI

---

### 2. Routing Logic

The system classifies the query into:

* Document-based → RAG
* Action/data → API
* General → LLM

---

### 3. Execution Layer

| Path | Function                               |
| ---- | -------------------------------------- |
| RAG  | Retrieves relevant context using FAISS |
| API  | Returns structured backend data        |
| LLM  | Generates natural responses            |

---

### 4. Response Generation

Final output is returned with a **source label**:

* `"RAG"`
* `"API"`
* `"LLM"`

---

## Project Structure

```text id="arch2"
Chatbot/
├── main.py          # FastAPI entry point
├── router.py        # Routing logic
├── api/             # API layer
├── rag/             # Retrieval system
├── data/            # Knowledge base
├── frontend/        # UI
└── requirements.txt
```

---

## Example Queries

| Query                       | Path |
| --------------------------- | ---- |
| "What is machine learning?" | RAG  |
| "Get user data"             | API  |
| "Tell me a joke"            | LLM  |

---

## Tech Stack

**Backend**

* FastAPI

**AI**

* Groq (LLM)
* Sentence Transformers
* FAISS

**Frontend**

* HTML, CSS, JavaScript

---

## Running Locally

```bash id="run1"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

```text id="run2"
frontend/index.html
```

---

## Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* AI system routing
* Hybrid architecture design
* LLM + structured data integration

---

## Current Stage

✔️ Phase 1 complete:

* Functional hybrid system
* UI integration
* Routing implemented

---

## Next (Phase 2)

* Modular AI system (domain-based modules)
* Decision engine (structured outputs)
* File upload → dynamic RAG
* Deployment

---

## 💡 Takeaway

This project focuses on **how AI systems are designed**, not just how they respond.

---
