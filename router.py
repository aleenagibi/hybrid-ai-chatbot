def route_query(query):

    query = query.lower().strip()

    career_keywords = [
        "career",
        "job",
        "resume",
        "skill",
        "interview",
        "profession"
    ]

    wellbeing_keywords = [
        "stress",
        "sad",
        "anxiety",
        "tired",
        "mental",
        "depressed"
    ]

    # Career route
    for word in career_keywords:
        if word in query:
            return "career"

    # Wellbeing route
    for word in wellbeing_keywords:
        if word in query:
            return "wellbeing"

    # Default route
    return "general"