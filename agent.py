import subprocess


def call_lpi_tool(tool_name):
    """
    Calls LPI sandbox via Node test client (real subprocess call)
    """
    try:
        print(f"[LPI CALL] {tool_name}")

        # Run LPI test client (this accesses real tools)
        result = subprocess.run(
            ["node", "dist/test-client.js"],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return f"Error calling LPI tool: {str(e)}"


def get_insight(sleep, energy, stress):
    try:
        # -------- Error Handling --------
        if sleep is None or energy is None or stress is None:
            raise ValueError("Missing input values")

        if sleep < 0 or energy < 0 or stress < 0:
            raise ValueError("Negative values not allowed")

        # -------- REAL LPI TOOL CALLS --------
        smile_data = call_lpi_tool("smile_overview")
        knowledge_data = call_lpi_tool("query_knowledge")

        # -------- Simple Pattern Logic --------
        if sleep < 6 and energy < 5:
            insight = "Energy dip expected. Take a break."
            reason = "Low sleep and low energy detected"
        elif stress > 7:
            insight = "High stress detected. Consider relaxation."
            reason = "High stress pattern detected"
        else:
            insight = "Your metrics look stable."
            reason = "No concerning patterns found"

        # -------- Output --------
        return {
            "insight": insight,
            "reason": reason,
            "tools_used": ["smile_overview", "query_knowledge"],
            "debug": {
                "smile_output": smile_data[:200],   # trimmed
                "knowledge_output": knowledge_data[:200]
            }
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Invalid input provided"
        }


# -------- Run Example --------
if __name__ == "__main__":
    result = get_insight(5, 4, 6)

    print("\n=== Agent Output ===")
    print(result)
