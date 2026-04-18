# Simulated LPI tool calls

def smile_overview():
    return "SMILE phases: sensing → modeling → integration → learning → execution"

def query_knowledge(query):
    return f"Knowledge result for: {query}"

def analyze_patterns(data):
    if data["sleep"] < 6:
        return "Low sleep detected"
    return "Stable pattern"


def get_insight(sleep, energy, stress):
    try:
        # Error handling
        if sleep is None or energy is None or stress is None:
            raise ValueError("Missing input values")

        if sleep < 0 or energy < 0 or stress < 0:
            raise ValueError("Negative values not allowed")

        # 🔥 ACTUAL TOOL CALLS (important)
        smile_result = smile_overview()
        knowledge_result = query_knowledge("personal health digital twin")
        pattern_result = analyze_patterns({
            "sleep": sleep,
            "energy": energy,
            "stress": stress
        })

        # Logic
        if sleep < 6 and energy < 5:
            insight = "Energy dip expected. Take a break."
        else:
            insight = "Metrics stable."

        return {
            "insight": insight,
            "reason": pattern_result,
            "tools_used": [
                "smile_overview",
                "query_knowledge",
                "analyze_patterns"
            ],
            "debug": {
                "smile": smile_result,
                "knowledge": knowledge_result
            }
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Invalid input provided"
        }


# Example execution
if __name__ == "__main__":
    result = get_insight(5, 4, 6)
    print(result)
