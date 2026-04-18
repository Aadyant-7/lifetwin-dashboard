import json
import subprocess


def call_tool(proc, tool_name, args={}):
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": args
        }
    }

    proc.stdin.write(json.dumps(request) + "\n")
    proc.stdin.flush()

    response = proc.stdout.readline()
    if not response:
        return "No response"

    data = json.loads(response)
    return data.get("result", {}).get("content", [{}])[0].get("text", "")


def run():
    try:
        proc = subprocess.Popen(
            ["node", "dist/src/index.js"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # INIT
        init = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "lifetwin", "version": "1.0"}
            }
        }

        proc.stdin.write(json.dumps(init) + "\n")
        proc.stdin.flush()
        proc.stdout.readline()

        proc.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
        proc.stdin.flush()

        # 🔥 REAL TOOL CALLS
        smile = call_tool(proc, "smile_overview")
        knowledge = call_tool(proc, "query_knowledge", {"query": "sleep and energy"})
        cases = call_tool(proc, "get_case_studies")

        proc.terminate()

        print(smile[:100])
        print(knowledge[:100])
        print(cases[:100])

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    run()
