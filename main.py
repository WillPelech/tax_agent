import yaml
from agent.agent import buildClient
from agent.prompt import base_prompt 
from fastmcp import Client 
import asyncio

async def main():
    with open("config.yaml") as f: 
        config = yaml.safe_load(f)
    model_client = buildClient(config)
    response = model_client.chat(base_prompt)
    mcp_client = Client("mcp_server/server.py")

    async with mcp_client:
        response = await model_client.generate_content(
                "call mcp tool test",  
                tools=[mcp_client.session]  # Pass the FastMCP client session
            )
        
        print(response.text)

    print(response)
    




if __name__ == "__main__":
    asyncio.run(main())
