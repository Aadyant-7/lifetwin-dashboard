# Simple mock agent for LifeTwin

def get_insight(sleep, energy, stress):
    # Basic error handling
    if sleep is None or energy is None or stress is None:
        return "Invalid input: Missing values"

    if sleep < 0 or energy < 0 or stress < 0:
        return "Invalid input: Values cannot be negative"

    # Simulated LPI tool usage
    tools_used = ["smile_overview", "query_knowledge", "analyze_patterns"]

    # Basic logic
    if sleep < 6 and energy < 5:
        insight = "Your energy may drop in the afternoon. Consider rest."
    elif stress > 7:
        insight = "High stress detected. Try relaxation techniques."
    else:
        insight = "Your metrics look stable."

    return {
        "insight": insight,
        "tools_used": tools_used
    }


# Example run
if __name__ == "__main__":
    result = get_insight(5, 4, 6)
    print(result)
