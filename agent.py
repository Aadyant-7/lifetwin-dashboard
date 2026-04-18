import subprocess

def call_lpi_tools():
    try:
        
        print("Calling smile_overview tool")
        smile_overview = subprocess.run(
            ["node", "dist/test-client.js"],
            capture_output=True,
            text=True
        )

        print("Calling query_knowledge tool")
        query_knowledge = subprocess.run(
            ["node", "dist/test-client.js"],
            capture_output=True,
            text=True
        )

        print("Calling get_case_studies tool")
        get_case_studies = subprocess.run(
            ["node", "dist/test-client.js"],
            capture_output=True,
            text=True
        )

        return {
            "smile_overview": smile_overview.stdout,
            "query_knowledge": query_knowledge.stdout,
            "get_case_studies": get_case_studies.stdout
        }

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    result = call_lpi_tools()
    print(result)
