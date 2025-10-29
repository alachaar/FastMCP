import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))


## FastMCP clients are asynchronous, so we need to use asyncio.run to run the client
## We must enter a client context (async with client:) before using the client
## You can make multiple client calls within the same context