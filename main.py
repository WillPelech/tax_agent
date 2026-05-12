import yaml
from agent.agent import buildClient
import asyncio
from strategy.react import run
from agent.registry import McpToolRegistry
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    with open("model-config.yaml") as f:
        model_config = yaml.safe_load(f)
    model_client = buildClient(model_config)

    server_params = StdioServerParameters(
        command="python3",
        args=["mcp_server/server.py"],
    )

    user_prompt = input("What tax issues can I help you with")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            mcp_server = McpToolRegistry(session)

            response = await run(model_client, user_prompt, mcp_server)
            print(response)

if __name__ == "__main__":
    asyncio.run(main())
