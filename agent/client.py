from google import genai
from abc import ABC
from abc import abstractmethod 
import ollama

#this is an inteface that all providers should inherit
class LLMClient(ABC):
# TODO add tools interface
    @abstractmethod
    def chat(self,message:str)->str:
        pass


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

class QwenClient(LLMClient):
    def __init__(self, model:str):
        self.model = model
    def chat(self,message)-> str:
        response = ollama.chat(
        model=self.model,
        messages=[{"role": "user", "content": message}]
        )
        return response.message.content or ""

        

