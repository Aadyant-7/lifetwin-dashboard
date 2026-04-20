import json
import subprocess
import sys
import select


def call_tool(proc, tool_name, args=None):
    if args is None:
        args = {}

    try:
        # Detect if process already crashed
        if proc.poll() is not None:
            return "[ERROR] LPI server process crashed"

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

        # Timeout handling (5 seconds)
        ready, _, _ = select.select([proc.stdout], [], [], 5)
        if not ready:
            return "[ERROR] LPI server timeout"

        response = proc.stdout.readline()

        if not response:
            return "[ERROR] No response from LPI server"

        data = json.loads(response)

        if "error" in data:
            return f"[ERROR] {data['error'].get('message', 'Unknown error')}"

        return data.get("result", {}).get("content", [{}])[0].get("text", "[EMPTY RESULT]")

    except json.JSONDecodeError:
        return "[ERROR] Invalid JSON response from LPI"
    except Exception as e:
        return f"[ERROR] Tool call failed: {str(e)}"


def sanitize_output(output, fallback):
    if not output or "[ERROR]" in output or len(output.strip()) < 5:
        return fallback
    return output


def run():
    try:
        # Handle empty input
        if len(sys.argv) < 2:
            user_query = "default query: digital twin health insights"
        else:
            user_query = sys.argv[1].strip()

        if not user_query:
            user_query = "fallback query: sleep and energy"

        # Start MCP server
        proc = subprocess.Popen(
            ["node", "dist/src/index.js"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # INIT handshake
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

        proc.stdin.write(json.dumps({
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }) + "\n")
        proc.stdin.flush()

        # 🔥 REAL MCP TOOL CALLS
        smile = call_tool(proc, "smile_overview")
        knowledge = call_tool(proc, "query_knowledge", {"query": user_query})
        cases = call_tool(proc, "get_case_studies")

        # Safe termination
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()

        # Output validation
        smile = sanitize_output(smile, "[Fallback] Unable to retrieve SMILE overview")
        knowledge = sanitize_output(knowledge, "[Fallback] Knowledge unavailable")
        cases = sanitize_output(cases, "[Fallback] No case studies found")

        # Final output
        print("\n--- Agent Output ---\n")
        print(smile[:100])
        print(knowledge[:100])
        print(cases[:100])

    except Exception as e:
        print("[FATAL ERROR]", str(e))


if __name__ == "__main__":
    run()
