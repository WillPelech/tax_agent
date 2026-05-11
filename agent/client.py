from google import genai
from abc import ABC
from abc import abstractmethod
from typing import Any
import ollama
from qwen_agent.agents import Assistant
from typing import List, Dict
import os

#this is an inteface that all providers should inherit
class LLMClient(ABC):
# TODO add tools interface
    @abstractmethod
    def chat(self,message:str)->str:
        pass
    @abstractmethod
    async def generate_content(self, message: str, tools: Any) -> Any:
        ...





class GemeniClient(LLMClient):
    def __init__(self,model:str):
        self.client = genai.Client()
        self.model = model
    def chat(self, message: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=message
        )
        return response.text or ""
    async def generate_content(self, message: str, tools: Any):
        return await self.client.aio.models.generate_content(
            model=self.model,
            contents=message,
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=tools,
            )
        )


class QwenClient(LLMClient):
    def __init__(self, model:str):
        self.model = model
        self.llm_config = {
            'model':model
        }
    def chat(self,message)-> str:
        response = ollama.chat(
        model=self.model,
        messages=[{"role": "user", "content": message}]
        )
        return response.message.content or ""
    def generate_content(self, message: str, tools) -> Any:
        server_path = os.path.abspath("mcp_server/server.py")
        mcp_cfg = {
            "mcpServers": {
                "tax_tools": {
                    "command": "python3",
                    "args": [server_path],
                }
            }
        }
        bot = Assistant(
            llm={"model": self.model, "model_server": "http://localhost:11434/v1", "api_key": "EMPTY"},
            function_list=[mcp_cfg],
        )
        messages:List[Dict[str,str]] = [{"role": "user", "content": message}]
        response = []
        for response in bot.run(messages=messages):
            pass
        return response
        

