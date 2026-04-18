import subprocess


def call_lpi_tool(tool_name):
    try:
        result = subprocess.run(
            ["node", "dist/test-client.js", tool_name],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout

    except subprocess.TimeoutExpired:
        return "Timeout while calling LPI"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    try:
        smile_overview_output = call_lpi_tool("smile_overview")
        query_knowledge_output = call_lpi_tool("query_knowledge")

        combined_output = smile_overview_output + query_knowledge_output

        print(combined_output[:200])

    except Exception as e:
        print(f"Agent failed: {str(e)}")


if __name__ == "__main__":
    main()
