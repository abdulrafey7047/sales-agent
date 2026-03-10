from fastmcp import FastMCP
from tools import register_tools


mcp = FastMCP("PostgresMCP")


register_tools(mcp)

if __name__ == "__main__":
    print("Starting Postgres MCP Server on HTTP (SSE)...")
    # This will run on http://0.0.0.0:8000/sse by default
    mcp.run(transport="sse", host="0.0.0.0", port=8000)