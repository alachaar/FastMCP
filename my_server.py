from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()

## This is a simple FastMCP server that defines a tool called "greet"
## The greet tool takes a name as input and returns a greeting message
## To use a different transport e.g HTTP :
## mcp.run(transport="http",host="127.0.0.1",port=8000)