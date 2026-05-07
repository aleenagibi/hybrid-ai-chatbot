def generate_decision(module, result):

    # Career module formatting
    if module == "career":

        return {
            "type": "Career Guidance",

            "analysis": result["analysis"],

            "recommendations": result["suggestions"],

            "next_action": result["action"],

            "priority": "Medium"
        }

    # Wellbeing module formatting
    elif module == "wellbeing":

        return {
            "type": "Wellbeing Support",

            "analysis": result["analysis"],

            "recommendations": result["suggestions"],

            "next_action": result["action"],

            "priority": "High"
        }

    # General module
    else:

        return {
            "type": "General Response",

            "response": result["response"],

            "priority": "Low"
        }