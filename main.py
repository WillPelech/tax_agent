import yaml
from agent.agent import buildClient
from agent.prompt import base_prompt
import asyncio
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

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            response = await model_client.generate_content(
                "Use get_file_contents to read the file at test_data/sample.txt and summarize what is in it. give an in detail summary",
                tools=[session]
            )
            if isinstance(response, list):
                print(response[-1]["content"])
            else:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
