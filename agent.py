import subprocess
import json


def call_lpi_tool(tool_name):
    try:
        request = {
            "tool": tool_name,
            "input": {}
        }

        process = subprocess.Popen(
            ["node", "dist/test-client.js"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(json.dumps(request), timeout=10)

        return stdout

    except subprocess.TimeoutExpired:
        return "Timeout while calling LPI"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    try:
        smile_overview = call_lpi_tool("smile_overview")
        query_knowledge = call_lpi_tool("query_knowledge")

        result = smile_overview + query_knowledge

        print(result[:200])

    except Exception as e:
        print(f"Agent failed: {str(e)}")


if __name__ == "__main__":
    main()
