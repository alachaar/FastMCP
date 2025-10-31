# Scenario 2 : FastAPI -> FastMCP with streamable http

# FASTAPI :
* uvicorn.run(app, host="localhost", port=8002) : run the app on localhost
* python3 fastapi-mcp_calculator.py: run the api server
* http://localhost:8002/docs : acceder a l'API on swagguer

# FASTMCP : 
* mcp = FastApiMCP(app,name="CalculatorMCP") : transformer FastAPI app to FastMCP app
* mcp.mount_http() : to run the mcp with http
* python3 fastapi-mcp_calculator.py: run the mcp server (obligatoire) on http://localhost:8002
* npx @modelcontextprotocol/inspector http://localhost:8002/mcp : test the server et il faut mettre streamable 