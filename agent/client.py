from google import genai
from abc import ABC
from abc import abstractmethod 
#this is an inteface that all providers should inherit
class LLMClient(ABC):
# TODO add tools interface
    @abstractmethod
    def chat(message:str):
        pass


class GemeniClient(LLMClient):
    def __init__(self,model:str):
        self.client = genai.Client()
        self.model = model
    def chat(self,message:str):
        response = self.client.models.generate_content(
            model = self.model , 
            contents = message
        )

class QwenClient(LLMClient):
    def __init__():
        pass
    def chat(message:str,model:str):
        pass


        

