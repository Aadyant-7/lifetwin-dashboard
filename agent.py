import subprocess

def call_lpi(tool_name):
    try:
        result = subprocess.run(
            ["node", "dist/test-client.js"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    try:
        print("Calling LPI tools...")

        smile = call_lpi("smile_overview")
        knowledge = call_lpi("query_knowledge")

        print("smile_overview output:", smile[:100])
        print("query_knowledge output:", knowledge[:100])

    except Exception as e:
        print("Agent failed:", str(e))


if __name__ == "__main__":
    main()
