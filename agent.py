import subprocess

def call_lpi(tool):
    try:
        command = ["node", "dist/test-client.js", tool]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        return result.stdout

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    try:
        smile_overview = call_lpi("smile_overview")
        query_knowledge = call_lpi("query_knowledge")

        combined = smile_overview + query_knowledge

        print("Agent Output:")
        print(combined[:200])

    except Exception as e:
        print("Failure:", str(e))


if __name__ == "__main__":
    main()
