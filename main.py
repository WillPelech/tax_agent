import yaml
from agent.agent import buildClient
from agent.prompt import base_prompt
import asyncio

async def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    model_client = buildClient(config)
    response = model_client.chat(base_prompt)

    response = model_client.generate_content(
        "call get_file_contents tool test",
        tools=None
    )
    if isinstance(response, list):
        print(response[-1]["content"])
    else:
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
