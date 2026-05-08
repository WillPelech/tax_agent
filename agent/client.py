from google import genai
from abc import ABC
from abc import abstractmethod
from typing import Any
import ollama
from fastmcp import ClientSession

#this is an inteface that all providers should inherit
class LLMClient(ABC):
# TODO add tools interface
    @abstractmethod
    def chat(self,message:str)->str:
        pass
    @abstractmethod
    def generate_content(self, message: str, tools: ClientSession) -> Any:
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
    def generate_content(self,message:str,tools:ClientSession):
        return self.client.models.generate_content(
            model=self.model,
            contents=message,
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=tools,  # Pass the FastMCP client session
            )
        )
class QwenClient(LLMClient):
    def __init__(self, model:str):
        self.model = model
    def chat(self,message)-> str:
        response = ollama.chat(
        model=self.model,
        messages=[{"role": "user", "content": message}]
        )
        return response.message.content or ""
    def generate_content(self,message:str,tools):
        raise NotImplementedError("QwenClient does not support tool use")
        

