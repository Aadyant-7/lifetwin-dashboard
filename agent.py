# Simulated LPI tool calls

def smile_overview():
    return "SMILE: sensing → modeling → integration → learning → execution"

def query_knowledge(query):
    return f"Knowledge result for: {query}"

def analyze_patterns(data):
    if data["sleep"] < 6:
        return "Low sleep detected"
    return "Stable pattern"


def get_insight(sleep, energy, stress):
    # Error handling
    if sleep is None or energy is None or stress is None:
        return "Error: Missing input values"

    if sleep < 0 or energy < 0 or stress < 0:
        return "Error: Invalid negative values"

    # Tool usage
    smile = smile_overview()
    knowledge = query_knowledge("personal health digital twin")
    pattern = analyze_patterns({"sleep": sleep})

    # Insight
    if sleep < 6 and energy < 5:
        insight = "Energy dip expected. Take a break."
    else:
        insight = "Metrics look stable."

    return {
        "insight": insight,
        "reasoning": pattern,
        "tools_used": ["smile_overview", "query_knowledge", "analyze_patterns"]
    }


# Example run
if __name__ == "__main__":
    result = get_insight(5, 4, 6)
    print(result)
