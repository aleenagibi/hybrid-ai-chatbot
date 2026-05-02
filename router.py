def route_query(query):
    query = query.lower()

    if "data" in query or "user" in query:
        return "api"
    elif "ai" in query or "machine learning" in query:
        return "rag"
    else:
        return "llm"