from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Module descriptions
modules = {

    "career": """
    career guidance jobs resume interview skills profession future
    career confusion learning roadmap technology choices
    frontend backend AI machine learning cloud computing
    skill development internships placements software engineering
    """,

    "wellbeing": """
    stress anxiety sadness emotions burnout loneliness depression
    overthinking mental exhaustion emotional support self doubt
    """,

    "general": """
    casual conversation random questions jokes facts explanations
    greetings coding concepts general knowledge
    """
}

# Convert module descriptions into embeddings
module_embeddings = {
    key: model.encode(value)
    for key, value in modules.items()
}


def semantic_route(query):

    # Query embedding
    query_embedding = model.encode(query)

    similarities = {}

    # Compare similarity with each module
    for module, embedding in module_embeddings.items():

        score = cosine_similarity(
            [query_embedding],
            [embedding]
        )[0][0]

        similarities[module] = score

    # Select highest similarity
    best_module = max(similarities, key=similarities.get)

    print("SIMILARITIES:", similarities)
    print("BEST MODULE:", best_module)

    return best_module